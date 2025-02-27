import json
from langgraph_agent import graph, State
from fastapi import FastAPI, Request, Response
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import (
    convert_to_openai_messages,
    message_chunk_to_message
)

app = FastAPI(
    title="API for openwebui-pipelines",
    description="API for openwebui-pipelines",
    )

@app.post("/openwebui-pipelines/api")
async def main(inputs: State):
    response = await graph.ainvoke(inputs)
    print(response)
    return response

@app.post("/openwebui-pipelines/api/stream")
async def stream(inputs: State):
    async def event_stream():
        try:
            print(f"\nReceived inputs: {inputs}\n")
            async for event in graph.astream(input=inputs, stream_mode="messages"):
                print(f"\nReceived event: {event}\n")
                # get first element of tuple
                message = message_chunk_to_message(event[0])
                print(f"\nConverted event: {message}\n")
                
                yield convert_to_openai_messages(message)['content']
        except Exception as e:
            print(f"An error occurred: {e}")

    return StreamingResponse(event_stream(), media_type="application/json")

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
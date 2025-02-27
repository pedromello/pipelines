import requests
import json
from typing import List, Union, Generator, Iterator
try:
    from pydantic.v1 import BaseModel
except Exception:
    from pydantic import BaseModel



class Pipeline:

    class Valves(BaseModel):
        pass

    def __init__(self):
        self.id = "LangGraph Agent"
        self.name = "LangGraph Agent"

    async def on_startup(self):
        print(f"on_startup: {__name__}")
        pass

    async def on_shutdown(self):
        print(f"on_shutdown: {__name__}")
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
            ) -> Union[str, Generator, Iterator]:

        url = 'http://127.0.0.1:8000/openwebui-pipelines/api'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = {
            "messages": [[msg['role'], msg['content']] for msg  in messages]
            }
        print("data",data)
        response = requests.post(url, json=data, headers=headers, stream=False)
        print("response",response)
        for line in response.iter_lines():
            if line:
                try:
                    json_line = line.decode()
                    print("json_line",json_line)
                    parsed = json.loads(json_line)  # Convert to JSON
                    print("parsed",parsed)
                    print("parsed['messages']['content']",parsed["messages"]["content"])
                    yield parsed["message"]["content"] + "\n"
                except Exception as e:
                    print(f"Error parsing response: {e}")
                    continue
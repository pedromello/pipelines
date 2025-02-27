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
        self.id = "LangGraph Agent (Stream)"
        self.name = "LangGraph Agent (Stream)"

    async def on_startup(self):
        print(f"on_startup: {__name__}")
        pass

    async def on_shutdown(self):
        print(f"on_shutdown: {__name__}")
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
            ) -> Union[str, Generator, Iterator]:

        url = 'http://127.0.0.1:8000/openwebui-pipelines/api/stream'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = {
            "messages": [[msg['role'], msg['content']] for msg  in messages]
            }
        print("data",data)
        
        response = requests.post(url, json=data, headers=headers, stream=True)
        
        response.raise_for_status()
        
        return response.iter_lines()
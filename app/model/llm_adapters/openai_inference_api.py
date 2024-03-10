
import os
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter
from openai import OpenAI

class OpenAiInference(ILlmAdapter):

    def __init__(self):
        self.__client = OpenAI()

    def query_llm(self,  prompt: str, api_documentation:str) -> str: 
        messages = [{"role": "user", "content": prompt}]
        completion = self.__client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=[api_documentation],
        tool_choice="auto"
        ) 
        return completion.dict()['choices'][0]['message']['tool_calls'][0]['function']['arguments']


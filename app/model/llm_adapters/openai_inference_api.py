
import json
import os
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter
from openai import OpenAI

class OpenAiInference(ILlmAdapter):

    def __init__(self):
        self.__client = OpenAI()

    def query_llm(self,  prompt: str, api_documentation:dict) -> str: 
        if not isinstance(api_documentation, dict):
            raise TypeError('api documentation should be type dict')
        messages = [{"role": "user", "content": prompt}]
        completion = self.__client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=[api_documentation],
        tool_choice="auto"
        ) 
        try:
            llm_response = completion.dict()['choices'][0]['message']['tool_calls'][0]['function']['arguments']
        except Exception as e:
            raise RuntimeError('could not create proper response with given input')
        if not isinstance(json.loads(llm_response), dict):
            raise TypeError('the llm response must me a valid json that can be converted to a dict')
        return llm_response


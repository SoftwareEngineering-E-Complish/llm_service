from typing import Dict
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter

class QueryGenerator:
    def __init__(self, llm_adapter: ILlmAdapter):
        self.__llm = llm_adapter
        
    def generate_api_payload(self, prompt:str, api_documentation:dict) -> str:
        if not isinstance(prompt,str) or not isinstance(api_documentation,dict):
            raise ValueError('The prompt should be a string and the api documentation a dict')
        response = self.__llm.query_llm(prompt, api_documentation)
        return response


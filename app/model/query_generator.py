from typing import Dict
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter

class QueryGenerator:
    def __init__(self, llm_adapter: ILlmAdapter):
        self.__llm = llm_adapter
        
    def generate_api_payload(self, prompt:str, api_documentation:str) -> str:
        response = self.__llm.query_llm(prompt, api_documentation)
        return response


from abc import ABC, abstractmethod


class ILlmAdapter(ABC):

    def __init__(self, model_identifier: str=None):
        pass
    
    @abstractmethod
    def query_llm(self, prompt: str, api_documentation:str) -> str:
        pass

        
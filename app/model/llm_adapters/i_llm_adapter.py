from abc import ABC, abstractmethod


class ILlmAdapter(ABC):
    
    @abstractmethod
    def create_query(self, prompt: str) -> str:
        pass
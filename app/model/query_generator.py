from app.model.llm_adapters.i_llm_adapter import ILlmAdapter

class QueryGenerator:
    def __init__(self, llm_adapter: ILlmAdapter):
        self.__llm = llm_adapter
        
    def generate_sql(self, prompt: str) -> str:
        return self.__llm.create_query(prompt)
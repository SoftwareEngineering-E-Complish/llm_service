
import os
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class HuggingfaceInfereceApi(ILlmAdapter):

    def __init__(self):
        template = """Question: {prompt}
        Answer: return an sql statment
        with which you can directly query the database"""
        prompt = PromptTemplate.from_template(template)
        repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
        llm = HuggingFaceEndpoint(
            repo_id=repo_id, max_length=128, temperature=0.5, token=os.environ.get('HUGGINGFACEHUB_API_TOKEN')
        )
        self.__llm_chain = LLMChain(prompt=prompt, llm=llm)


    def create_query(self, prompt: str) -> str:
        return self.__llm_chain.invoke(prompt)

    

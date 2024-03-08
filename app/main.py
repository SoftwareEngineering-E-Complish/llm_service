from typing import Dict, Union
from fastapi import FastAPI
from app.model.llm_adapters.i_llm_adapter import ILlmAdapter
from app.model.config import llm_adapter

from app.model.query_generator import QueryGenerator
CONTENT_KEY: str = "content"

app = FastAPI()

@app.put("/generates/query")
def create_context(payload: Union[Dict, None]):
    query_generator = QueryGenerator(llm_adapter=llm_adapter())
    return {CONTENT_KEY: query_generator.generate_sql(payload[CONTENT_KEY])}






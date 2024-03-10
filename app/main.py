import argparse
from typing import Dict, Union
from fastapi import FastAPI
from app.model.llm_adapters.llm_mapper import LlmMapper
from app.model.query_generator import QueryGenerator
from app.config import llm_inference_model

QUERY_KEY: str = "query"
API_DOCUMENTATION_KEY: str = "api_documentation"
CONTENT_KEY: str = "content"

llm_adapter = LlmMapper.map(llm_inference_model)

app = FastAPI()

@app.post("/generates/query")
async def create_context(payload: Union[Dict, None]):
    query_generator = QueryGenerator(llm_adapter=llm_adapter)
    response = query_generator.generate_api_payload(payload.get(QUERY_KEY),
                                                    payload.get(API_DOCUMENTATION_KEY)
                                                            )
    return {CONTENT_KEY: response}






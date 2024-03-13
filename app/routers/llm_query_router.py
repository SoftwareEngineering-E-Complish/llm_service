from typing import Dict, Union
from fastapi import APIRouter

from app.services.llm_service import LlmService
from app.utils.constants import API_DOCUMENTATION_KEY, QUERY_KEY

llm_query_router = APIRouter()

llm_service = LlmService()

@llm_query_router.post("/generates/query")
async def create_context(payload: Union[Dict, None]):
    return llm_service.create_query(payload.get(QUERY_KEY),payload.get(API_DOCUMENTATION_KEY) )
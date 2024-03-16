from typing import Dict, Union
from fastapi import APIRouter
from app.utils.llm_response_dto import LlmResponseDto
from app.services.llm_service import LlmService
from app.utils.constants import API_DOCUMENTATION_KEY, QUERY_KEY
import os 
import json
CONSTANT_RESPONSES_MODE = 'constant_response'
PRODUCTION_MODE = 'production'
mode = os.environ.get('TEST_MODE', PRODUCTION_MODE)

llm_query_router = APIRouter()

if not mode==CONSTANT_RESPONSES_MODE:
    llm_service = LlmService()

@llm_query_router.post("/generates/query")
async def create_context(payload: Union[Dict, None]):
    if mode==CONSTANT_RESPONSES_MODE:
        return LlmResponseDto(json.dumps({'location':'Zurich'}))
    else:
        return llm_service.create_query(payload.get(QUERY_KEY),payload.get(API_DOCUMENTATION_KEY))  
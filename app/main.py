from fastapi import FastAPI
from app.routers.llm_query_router import llm_query_router
import logging

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(llm_query_router)









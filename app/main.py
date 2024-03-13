from fastapi import FastAPI
from app.routers.llm_query_router import llm_query_router


app = FastAPI()
app.include_router(llm_query_router)









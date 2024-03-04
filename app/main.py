from typing import Dict, Union
from fastapi import FastAPI

from app.model.query_generator import QueryGenerator

app = FastAPI()

@app.put("/generates/query")
def create_context(payload: Union[Dict, None]):
    query_generator = QueryGenerator()
    query_generator.main(payload)






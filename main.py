from fastapi import FastAPI
from pydantic import BaseModel
from backend.graph import graph
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

class Query(BaseModel):
    user_query: str


@app.post("/recommend")

def recommend_movies(query: Query):
    
    state = {"user_query": query.user_query}

    result = graph.invoke(state)
    
    return result

@app.get("/")
def home():
    return {"status": "running"}
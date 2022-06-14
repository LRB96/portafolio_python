# from fastAPI import fastAPI
from .applications import FastAPI as FastAPI

app = fastAPI

@app.get("/")
def home():
    return {"Hello": "World"}
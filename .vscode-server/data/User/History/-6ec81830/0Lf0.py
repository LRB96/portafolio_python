# from fastAPI import fastAPI
from fastAPI import FastAPI

app = fastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}
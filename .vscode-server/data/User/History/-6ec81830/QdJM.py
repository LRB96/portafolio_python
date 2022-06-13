from fastapi import fastAPI

app = fastAPI()

@app.get("/")
def home():
    return {"Hello" "World"}
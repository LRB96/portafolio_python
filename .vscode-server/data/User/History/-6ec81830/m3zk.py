import fastAPI from fastapi

app = fastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}
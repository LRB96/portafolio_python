from fastAPI import fastAPI

app = fastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}
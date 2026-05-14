from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Assistant Running"}

@app.post("/ask")
def homeOne():
    return {"message": "AI Assistant Running"}
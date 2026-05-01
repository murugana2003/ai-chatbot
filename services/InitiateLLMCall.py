from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello AI Engineer Lead"}

@app.get("/ask")
def ask():
    return {
        "name": "Murugan",
        "target_role": "AI Engineer Lead",
        "skills": ["Python", "LLM", "LangGraph", "AWS", "Docker"]
    }

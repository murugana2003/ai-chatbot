# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define request body structure
class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Hello AI Engineer Lead"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    question = request.question

    # Temporary response (LLM will come later)
    answer = f"You asked: {question}"

    return {"answer": answer}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from fastapi import APIRouter

from pydantic import BaseModel

from services.llm_service import ask_llm

router = APIRouter()

class AskRequest(BaseModel):

    question: str

@router.post("/ask")
async def ask_question(request: AskRequest):

    answer = ask_llm(request.question)

    return {

        "answer": answer

    }
from unittest.mock import sentinel

from fastapi import APIRouter
from pydantic import BaseModel
from pygments.lexers.smalltalk import NewspeakLexer

router = APIRouter()

class MarketRequest(BaseModel):
     company_code: str

@router.get("/marketData")
async def get_market_data(request: MarketRequest):

    return {"company_code": request.company_code}

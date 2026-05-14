from pydantic import BaseModel

class MarketRequest(BaseModel):
    company_code: str

class MarketResponse(BaseModel):
    company_details: str
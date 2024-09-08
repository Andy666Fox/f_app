from  fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

app = FastAPI(
    title='MyApp'
)

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail': exc.errors()})
    )


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str 
    price: float = Field(ge=0)
    amount: float
    
class DegreeType(Enum):
    novice = 'novice'
    advanced = 'advanced'
    expert = 'expert'
    
class Degree(BaseModel):
    id: int 
    created_at: str
    type_degree: DegreeType
    
    
class User(BaseModel):
    id: int 
    role: str 
    name: str
    degree: Optional[List[Degree]] = []


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id')==user_id]

@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
    




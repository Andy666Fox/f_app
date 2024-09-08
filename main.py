from  fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

app = FastAPI(
    title='MyApp'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'John', 'degree': [
        {'id': 1, 'created_at': '2022-01-01', 'type_degree': 'expert'}]},
    
    {'id': 2, 'role': 'trader', 'name': 'Bob'},
    
    {'id': 3, 'role': 'customer', 'name': 'Vasiliy', 'degree': [
        {'id': 3, 'created_at': '2022-01-04', 'type_degree': 'advanced'}]},
    
    {'id': 4, 'role': 'admin', 'name': 'Nadezhda', 'degree': [
        {'id': 4, 'created_at': '2022-01-02', 'type_degree': 'expert'}]},
    
    {'id': 5, 'role': 'trader', 'name': 'Igor', 'degree': [
        {'id': 5, 'created_at': '2022-03-03', 'type_degree': 'novice'}]}
    
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 433, 'amount': 2.87},
    {'id': 2, 'user_id': 1, 'currency': 'AUT', 'side': 'sell', 'price': 12, 'amount': 3.12},
    {'id': 3, 'user_id': 2, 'currency': 'ETH', 'side': 'buy', 'price': 76.8, 'amount': 3.47}
]

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
    degree: Optional[List[Degree]]


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id')==user_id]

@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
    




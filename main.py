from  fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field

app = FastAPI(
    title='MyApp'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'John'},
    {'id': 2, 'role': 'trader', 'name': 'Bob'},
    {'id': 3, 'role': 'customer', 'name': 'Vasiliy'},
    {'id': 4, 'role': 'admin', 'name': 'Nadezhda'},
    {'id': 5, 'role': 'trader', 'name': 'Igor'}
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

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id')==user_id]

@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
    




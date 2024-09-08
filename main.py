from  fastapi import FastAPI

app = FastAPI(
    title='MyApp'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'John'}
]

@app.get('/user/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id')==user_id]


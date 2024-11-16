# python -m uvicorn main:app

from fastapi import FastAPI, Path
from typing import Annotated

users_db = {"0": "Имя: Alex, возраст: 21",
            "1": "Имя: Nick, возраст: 40",
            "2": "Имя: Sveta, возраст: 30"}

app = FastAPI()

@app.get('/users')
async def get_users():
    return users_db

@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> str:
    current_index = str(int(max(users_db, key=int)) + 1)
    users_db[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    users_db[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    users_db.pop(str(user_id))
    return f'User {user_id} has been deleted'




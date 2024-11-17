# python -m uvicorn main:app

from fastapi import FastAPI, Path, HTTPException, Request 
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

users = []

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')

@app.post('/user/{username}/{age}')
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=24)]) -> User:
    if users:
        user_id = users[-1].id + 1
    else:
        user_id = 1

    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(description='Enter user ID', examples=1)],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='UrbanProfi')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=28)]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
        else:
            raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(description='Enter user ID', examples=1)]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user

    raise HTTPException(status_code=404, detail="User was not found")




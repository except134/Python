# python -m uvicorn main:app

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_page() -> str:
    return ("Главная страница")


@app.get("/user/admin")
async def admin_page() -> str:
    return ("Вы вошли как администратор")


@app.get("/user/{user_id}")
async def user_id_page(user_id) -> str:
    return (f"Вы вошли как пользователь № {user_id}")


@app.get("/user")
async def user_page(username: str = "Николай", age: int = "46") -> str:
    return (f"Информация о пользователе. Имя: {username}, возраст: {age}")

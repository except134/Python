from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from Backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from Models import User, Task
from schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()

    if task:
        return task

    raise HTTPException(status_code=404, detail="Task was not found")

@router.post('/create')
async def create_task(user_id: int, db: Annotated[Session, Depends(get_db)], create_task: CreateTask):
    user = db.scalars(select(User).where(User.id == user_id)).first()

    if user:
        db.execute(insert(Task).values(
            title=create_task.title,
            content=create_task.content,
            priority=create_task.priority,
            user_id=user_id,
            slug=slugify(create_task.title)
        ))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

    raise HTTPException(status_code=404, detail="User was not found")

@router.put('/update')
async def update_task(task_id: int, db: Annotated[Session, Depends(get_db)], update_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id)).first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(update(Task).where(Task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

@router.delete('/delete')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))

    if task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deleted successfully!'}

    raise HTTPException(status_code=404, detail="Task was not found")


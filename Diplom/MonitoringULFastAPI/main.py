# python -m uvicorn main:app

from fastapi import FastAPI, Path, HTTPException, Request, Form, APIRouter 
from fastapi.responses import HTMLResponse, FileResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from threading import Thread, Lock
import uvicorn
from settings import *
from getfiles import *
from parser import *
from tgbot import *

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

router_root = APIRouter(prefix='', tags=['root'])

@router_root.get("/", response_class=HTMLResponse)
@router_root.get("/home", name='home', response_class=HTMLResponse)
async def get_home(request: Request, INN: str = ''):
    results = {}
    if INN:
        results = search_results(INN)
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "title": 'Мониторинг ЮЛ', "year": datetime.now().year})

@router_root.get("/contact", name='contact', response_class=HTMLResponse)
async def get_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, 
                                                       "title": 'Мониторинг ЮЛ', 
                                                       "year": datetime.now().year,
                                                       "message":'Мои контакты'})

@router_root.get("/about", name='about', response_class=HTMLResponse)
async def get_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, 
                                                     "title": 'Мониторинг ЮЛ', 
                                                     "year": datetime.now().year,
                                                     "message": 'Мониторинг ЮЛ'})

app.include_router(router_root)

def start_tg_bot():
    bot.polling(none_stop=True, interval=0)

def start_web_app():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == '__main__':
    th2 = Thread(target=start_web_app)
    th2.start()
    start_tg_bot()


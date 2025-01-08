# python -m uvicorn main:app

from fastapi import FastAPI, Path, HTTPException, Request, Form 
from fastapi.responses import HTMLResponse, FileResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
def get_home2(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
def get_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
def get_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)



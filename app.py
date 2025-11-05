
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pyfiglet

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, ascii_art: str = None):
    context = {"request": request, "message": "Hello from FastAPI!", "ascii_art": ascii_art}
    return templates.TemplateResponse("index.html", context)

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, user_text: str = Form(...), font_select: str = Form(...)):
    art = pyfiglet.figlet_format(user_text, font=font_select)
    context = {"request": request, "message": "Generated ASCII Art:", "ascii_art": art}
    return templates.TemplateResponse("index.html", context)

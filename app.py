

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pyfiglet

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Custom font directory
custom_font_dir = "fonts"
custom_fonts = ["ShadowText", "Big", "Cosmike", "Graffiti", "Isometric1", "Standard"]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, ascii_art: str = None):
    font_list = pyfiglet.FigletFont.getFonts() + custom_fonts
    context = {"request": request, "message": "Hello from FastAPI!", "ascii_art": ascii_art, "fonts": font_list}
    return templates.TemplateResponse("index.html", context)

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, user_text: str = Form(...), font_select: str = Form(...)):
    if font_select in custom_fonts:
        custom_font = pyfiglet.Figlet(font=f"{custom_font_dir}/{font_select}.flf")
        art = custom_font.renderText(user_text)
    else:
        art = pyfiglet.figlet_format(user_text, font=font_select)
    font_list = pyfiglet.FigletFont.getFonts() + custom_fonts
    context = {"request": request, "message": "Generated ASCII Art:", "ascii_art": art, "fonts": font_list}
    return templates.TemplateResponse("index.html", context)

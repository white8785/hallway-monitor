"""
Usage: 
    - curl -X POST -d "new_color=red-500" http://localhost:8000/color
    - curl -X POST -d "new_color=green-500" http://localhost:8000/color
"""
from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

color = "green"

@app.get("/color")
async def update_color(new_color: str = "green"):
    global color
    color = new_color
    return {"color": color}

@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "color": color})
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="public/dist"), name="static")

template = Jinja2Templates(directory="public/templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    response = template.TemplateResponse("index.html", {"request": request})
    return response

@app.get("/json")
def obtener_json():
    # Puedes construir el contenido JSON como un diccionario de Python
    contenido_json = {"mensaje": "Hola, este es un JSON de FastAPI"}

    # Luego, lo devuelves utilizando JSONResponse
    return JSONResponse(content=contenido_json)
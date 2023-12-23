from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from funciones import validarFormulario

app = FastAPI()

app.mount("/static", StaticFiles(directory="public/dist"), name="static")

template = Jinja2Templates(directory="public/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    response = template.TemplateResponse("index.html", {"request": request})
    return response


@app.post("/enviar-correo", response_class=HTMLResponse)
def enviarCorreo(
    request: Request,
    nombres: str = Form(""),
    correo: str = Form(""),
    asunto: str = Form(""),
    mensaje: str = Form(""),
):
    datos = {"nombres": nombres, "correo": correo, "asunto": asunto, "mensaje": mensaje}

    #validar el formulario
    is_valid = validarFormulario(datos)
    if is_valid:
        response = template.TemplateResponse("index.html", {"request": request}, status_code=200)
    else:
        response = template.TemplateResponse("index.html", {"request": request}, status_code=400)
    
    return response

@app.get("/json")
def obtener_json():
    # Puedes construir el contenido JSON como un diccionario de Python
    contenido_json = {"mensaje": "Hola, este es un JSON"}

    # Luego, lo devuelves utilizando JSONResponse
    return JSONResponse(content=contenido_json)

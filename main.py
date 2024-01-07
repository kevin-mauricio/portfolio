from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Correo import enviarCorreoCliente, enviarmeNotificacion
from database import get_database
from sqlalchemy.orm import Session

from funciones import insertarMensaje, validarFormulario

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
    db: Session = Depends(get_database)
):
    datos = {"nombres": nombres, "correo": correo, "asunto": asunto, "mensaje": mensaje}

    #validar el formulario
    is_valid = validarFormulario(datos)

    status = is_valid.get("status")
    tipo = is_valid.get("tipo")

    if status:
        response = template.TemplateResponse("index.html", {"request": request}, status_code=200)
        insertarMensaje(datos, db)
        enviarCorreoCliente(datos=datos)
        enviarmeNotificacion(datos=datos)
    else:
        if tipo == "datos_vacios":
            response = template.TemplateResponse("index.html", {"request": request}, status_code=400)
        else:
            #correo invalido
            response = template.TemplateResponse("index.html", {"request": request}, status_code=401)

    return response



@app.get("/json")
def obtener_json():
    # Puedes construir el contenido JSON como un diccionario de Python
    contenido_json = {"mensaje": "Hola, este es un JSON"}

    # Luego, lo devuelves utilizando JSONResponse
    return JSONResponse(content=contenido_json)

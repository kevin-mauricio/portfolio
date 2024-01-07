import re
from sqlalchemy.orm import Session
from models import Mensajes


def validarFormulario(datos):
    # Validar datos vacíos
    if not all(datos.values()):
        return {"status": False, "tipo": "datos_vacios"}

    # Validar formato del correo
    correo = datos.get("correo")
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(patron_correo, correo):
        return {"status": False, "tipo": "correo_invalido"}

    return {"status": True, "tipo": "ok"}

def insertarMensaje(datos, db: Session):
    mensaje = Mensajes(
        nombres=datos.get("nombres"),
        correo=datos.get("correo"),
        asunto=datos.get("asunto"),
        mensaje=datos.get("mensaje")
    )

    try:
        db.add(mensaje)
        db.commit()
        db.refresh()
    except Exception as e:
        db.rollback()
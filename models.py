from click import DateTime
from sqlalchemy import Column, Integer, String, func, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Mensajes(Base):
    __tablename__ = 'mensajes'
    id_mensaje = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(40))
    correo = Column(String(100))
    asunto = Column(String(80))
    mensaje = Column(String)
    fecha_envio = Column(String, server_default=func.now())

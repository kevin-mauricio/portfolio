def validarFormulario(datos):
    for clave, valor in datos.items():
        if not valor:
            return False
    return True
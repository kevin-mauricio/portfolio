import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib


def enviarCorreoCliente(datos):
    try:
        load_dotenv()

        correo_envia = "kmma407@gmail.com"
        contraseña = os.getenv("PASS")

        asunto = f"Confirmación mensaje Portafolio"
        cuerpo = f"""
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Confirmación de Mensaje</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f4;
                            margin: 0;
                            padding: 0;
                        }}

                        .container {{
                            max-width: 600px;
                            margin: 50px auto;
                            background-color: #fff;
                            padding: 20px;
                            border-radius: 8px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }}

                        h1 {{
                            color: #333;
                        }}

                        p {{
                            color: #555;
                        }}

                        .button {{
                            display: inline-block;
                            padding: 10px 20px;
                            font-size: 16px;
                            text-align: center;
                            text-decoration: none;
                            background-color: #4caf50;
                            color: #fff;
                            border-radius: 4px;
                            transition: background-color 0.3s;
                        }}

                        .button:hover {{
                            background-color: #45a049;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Confirmación de mensaje: {datos.get("asunto")}</h1>
                        <p>¡Hola {datos.get("nombres")}!</p>
                        <p>Tu mensaje ha sido recibido con éxito. Agradecemos tu interés y te responderemos lo antes posible.</p>
                        <p>Gracias por contactarnos.</p>
                        <a href="https://kevin-mauricio-portfolio.onrender.com/" class="button">Visita nuestro sitio web</a>
                    </div>
                </body>
                </html>
                """

        correo = EmailMessage()
        correo["From"] = correo_envia
        correo["To"] = datos.get("correo")
        correo["Subject"] = asunto
        correo.add_alternative(cuerpo, subtype="html")

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
            smtp.login(correo_envia, contraseña)
            smtp.sendmail(correo_envia, correo["To"], correo.as_string())
            smtp.quit()

        print("Correo enviado.")
        return True
    except Exception as e:
        print(f"Error al enviar correo: {str(e)}")
        return False

def enviarmeNotificacion(datos):
    try:
        load_dotenv()

        correo_envia = "kmma407@gmail.com"
        contraseña = os.getenv("PASS")

        asunto = datos.get("asunto")
        cuerpo = f"""
                    Nombres: {datos.get("nombres")}\n
                    Correo: {datos.get("correo")}\n
                    Asunto: {datos.get("asunto")}\n
                    Mensaje: {datos.get("mensaje")}\n
                """

        correo = EmailMessage()
        correo["From"] = correo_envia
        correo["To"] = correo_envia
        correo["Subject"] = asunto
        correo.set_content(cuerpo)


        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
            smtp.login(correo_envia, contraseña)
            smtp.sendmail(correo_envia, correo["To"], correo.as_string())
            smtp.quit()

        print("Correo enviado.")
        return True
    except Exception as e:
        print(f"Error al enviar correo: {str(e)}")
        return False
let formulario = document.getElementById("formulario_mensaje");
let botonEnviar = document.getElementById("botonEnviar");
let loader = document.getElementById("loader");

formulario.addEventListener("submit", function (event) {
  event.preventDefault();

  // Get form data
  const formData = new FormData(event.target);

  // Perform form submission using Fetch API
  fetch("/enviar-correo", {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      shiftLoader();

      // Captura el código de estado HTTP
      const status = response.status;

      if (status === 200) {
        // Éxito - Muestra la alerta de éxito
        formulario.reset();
        return Swal.fire({
          icon: "success",
          title: "Formulario enviado con éxito",
          text: "Gracias por tu mensaje.",
        });
      } else if (status === 400) {
        // Error de validación - datos_vacios
        return Swal.fire({
          icon: "error",
          title: "Datos vacios",
          text: "Todos los datos son necesarios para una mejor respuesta.",
        });
      } else if (status === 401) {
        // Error de validación - correo_invalido
        return Swal.fire({
          icon: "error",
          title: "Correo inválido",
          text: "Por favor asegurate de ingresar un correo válido.",
        });
      } else {
        // Otro código de estado - Muestra una alerta genérica
        return Swal.fire({
          icon: "error",
          title: "Error",
          text: "Algo salió mal.",
        });
      }
    })
    .catch((error) => {
        console.error("Error:", error);
        // Muestra una alerta de error si hay un problema con la solicitud
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Algo salió mal!",
        });
    });
    shiftLoader();
});

function shiftLoader() {
  botonEnviar.hidden = !botonEnviar.hidden;
  formulario.hidden = !formulario.hidden;
  loader.hidden = !loader.hidden;
}

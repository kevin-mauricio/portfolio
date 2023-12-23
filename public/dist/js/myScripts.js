let formulario = document.getElementById('formulario_mensaje');

formulario.addEventListener('submit', function (event) {
    event.preventDefault();

    // Get form data
    const formData = new FormData(event.target);

    // Perform form submission using Fetch API
    fetch('/enviar-correo', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        // Captura el código de estado HTTP
        const status = response.status;

        if (status === 200) {
            // Éxito - Muestra la alerta de éxito
            formulario.reset();
            return Swal.fire({
                icon: 'success',
                title: 'Formulario enviado con éxito',
                text: 'Gracias por tu envío.',
            });
        } else if (status === 400) {
            // Error de validación - Muestra la alerta de error de validación
            return Swal.fire({
                icon: 'error',
                title: 'Ups',
                text: 'Todos los datos son necesarios para una mejor respuesta.',
            });
        } else {
            // Otro código de estado - Muestra una alerta genérica
            return Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Algo salió mal.',
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Muestra una alerta de error si hay un problema con la solicitud
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Algo salió mal!',
        });
    });
});
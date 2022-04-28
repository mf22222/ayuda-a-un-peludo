const weatherApiKey = 0; // poner tu api key
let contadorClicks = 0;

$(document).ready(function() {

    $('#imagenPerro').click(function() {
        contadorClicks += 1;
        console.log(contadorClicks);
    })

    $('#joinusName').focusout(function() {
        console.log("Sali del foco")

        if ($('#joinusName')[0].value == '' || $('#joinusName')[0].value == null) {
            document.getElementsByName("joinusNameAlert")[0].classList.remove('hide');
        } else {
            document.getElementsByName("joinusNameAlert")[0].classList.add('hide');
        }
    })
    
    $('#joinus').submit(function(event) {
        console.log("Formulario enviado")
        event.preventDefault();
    });

    if('geolocation' in navigator) {
        /* geolocation is available */
        console.log("available")
        navigator.geolocation.getCurrentPosition((position) => {
            console.log(position.coords.latitude);
            console.log(position.coords.longitude);
            $.get(`https://api.weatherapi.com/v1/current.json?q=${position.coords.latitude},${position.coords.longitude}&key=${weatherApiKey}`, 
            function(data) {
                console.log(data)
            })
        });
    } else {
        /* geolocation IS NOT available */
        console.log("not available")
    }
});


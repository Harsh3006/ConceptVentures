var password = document.getElementById('password');
var toggle_password = document.getElementById('toggle-password');

if (document.getElementById('validation-box')) {
    var validation_box = document.getElementById('validation-box');
    var characters = document.getElementById('characters');
    var upper = document.getElementById('upper');
    var lower = document.getElementById('lower');
    var symbol = document.getElementById('symbol');
    var number = document.getElementById('number');
    password.onkeyup = function() {
        validation_box.style.display = 'block';
        var lowerCase = /[a-z]/g;
        if (password.value.match(lowerCase))
            lower.classList.replace("red", "green");
        else
            lower.classList.replace("green", "red");

        var upperCase = /[A-Z]/g;
        if (password.value.match(upperCase))
            upper.classList.replace("red", "green");
        else
            upper.classList.replace("green", "red");

        var numberCase = /[0-9]/g;
        if (password.value.match(numberCase))
            number.classList.replace("red", "green");
        else
            number.classList.replace("green", "red");

        if (password.value.length >= 8)
            characters.classList.replace("red", "green");
        else
            characters.classList.replace("green", "red");

        var symbolCase = /[!@#$%^&*_=+-]/g;
        if (password.value.match(symbolCase))
            symbol.classList.replace("red", "green");
        else
            symbol.classList.replace("green", "red");
    }
    password.onblur = function() {
        validation_box.style.display = 'none';
    }
}

function showPassword() {
    if (password.type === 'password') {
        password.type = 'text';
        toggle_password.setAttribute("name", "eye-outline");
    } else {
        password.type = 'password';
        toggle_password.setAttribute("name", "eye-off-outline");
    }
}

if (document.getElementById('message')) {
    var message = document.getElementById('message');
    setTimeout(hideMessage, 4000);

    function hideMessage() {
        message.style.display = 'none';
    }
}
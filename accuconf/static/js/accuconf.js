function registerUser() {
    if (validateRegistrationData()) {
        //alert ("Valid");
        //$('#registrationForm').submit();
        /* $.ajax({
         *     method: "POST",
         *     url: "/register",
         *     data: $('#registrationForm').serialize(),
         *     contentType: "application/json"
         * });*/
        return true;
    } else {
        alert ("Invalid");
        return false;
    }
}

function validateRegistrationData() {
    var email = $('#email').val();
    var password = $('#password').val();
    var salutation = $('#salutation').val();
    var firstName = $('#firstname').val();
    var lastName = $('#lastname').val();
    var suffix = $('#suffix').val();
    var phone = $('#phone').val();
    var country = $('#country').val();
    var state = $('#state').val();
    var states = $('#states').val();
    var pincode = $('#pincode').val();
    var question = $('#question').val();
    var captcha = $('#captcha').val();
    var submit = $('#submit');
    if (!isEmail(email)) {
        alert(email);
        return false;
    }
    if (!passwordValid(password)) {
        return false;
    }
    if (!nameValid(firstName) || !nameValid(lastName)) {
        return false;
    }
    if (!phoneValid(phone)) {
        return false;
    }
    if (!stateValid(state)) {
        return false;
    }
    if (!postalCodeValid(pincode)) {
        return false;
    }
    if (!captchaValid(captcha)) {
        return false;
    }
    
    submit.disabled = false;
    return true;
}

function isEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-_])+\.)+([a-zA-Z0-9])+$/;
  return regex.test(email);
}

function passwordValid(password) {
    if (password.length < 8) {
        return false;
    }
    if (!/\d/.test(password)) {
        return false;
    }
    if (!/[a-z]/.test(password)) {
        return false;
    }
    if (!/[A-Z]/.test(password)) {
        return false;
    }
    if (/[^0-9a-zA-Z!@#$%^&*\(\)<>?\|\/\\]/.test(password)) {
        return false;
    }
    return true;
}

function nameValid(name) {
    if (name.length < 1) {
        return false;
    }
}

function phoneValid(phone) {
    if (/[^0-9\-\+]+/.test(phone)) {
        return false;
    }
    return true;
}

function stateValid(state) {
    return true;
}

function postalCodeValid(code) {
    if (/[^0-9a-zA-Z\s]/.test(code)) {
        return false;
    }
    return true;
}

function captchaValid(captcha) {
    if (/\d+/.test(captcha)) {
        return true;
    }
    return false;
}

function notify(message) {
    $("#helpmessage").text(message);
    $("#helpmessage").fadeIn(100)
    //$("#helpmessage").fadeOut(3000);
}

function hidehelp() {
    $("#helpmessage").fadeOut(100);
}

function loadState() {
    var $sel = $('#country');
    var cVal = $('#country').val();
    var cName = $("option:selected", $sel).text()
    $('#states').empty();
    $.each(countryData, function(index) {
        if (countryData[index].alpha3 === cVal) {
            if (countryData[index].hasOwnProperty("regions")) {
                var regions = countryData[index].regions;
                regions.sort(function(a, b) {
                    var aUpper = a.name.toUpperCase();
                    var bUpper = b.name.toUpperCase();
                    if (aUpper < bUpper) {
                        return -1;
                    }
                    if (aUpper > bUpper) {
                        return 1;
                    }
                    return 0;
                });
                $('#state').hide();
                $('#states').show();
                $.each(regions, function(name, value) {
                    $('#states').append('<option value="' + value.code + '">' + value.name + '</option>');
                });
            } else {
                $('#states').hide();
                $('#state').show();
            }

        }
    });
}

function updateState() {
    var state = $('#states').val();
    var state_tb = $('#state');
    if (!$('#state').is(":visible")) {
        $('#state').text(state);
    }
}

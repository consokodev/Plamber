/**
 * Changes standard message in username 'Input' field for signing new user.
 *
 * @param object 'input'
 */
function usernameSignInMessage(input) {
    if (input.validity.patternMismatch) {
        input.setCustomValidity('Имя пользователя должно содержать только\n' +
                                'латинские буквы, цифры, знаки подчеркивания\n' +
                                'и быть длиной не менее 6 и не более 30 символов');
    } else {
        input.setCustomValidity('');
    }
}

/**
 * Changes standard message in password 'Input' field for signing new user.
 *
 * @param object 'input'
 */
function passwordSignInMessage(input) {
    if (input.validity.patternMismatch) {
        input.setCustomValidity('Пароль должен содержать только\n' +
                                'латинские буквы, цифры, знаки подчеркивания\n' +
                                'и быть длиной не менее 6 и не более 16 символов');
    } else {
        input.setCustomValidity('');
    }
}

/**
 * Checks if both of 'Input' password lines are equal.
 */
function checkEqualPassLines() {
    firstInputValue = document.getElementById('firstPass').value;
    secondInputValue = document.getElementById('secondPass').value;

    if (firstInputValue !== secondInputValue) document.getElementById('passWrongMessage').style.display = 'block';
    else document.getElementById('passWrongMessage').style.display = 'none';
}

/**
 * Sends ajax request to check if the user is already exists.
 */
function checkUserNotExists() {
    // Send request only if 'Input' is not empty.
    if ($('#usernameInput').val()) {
        $.ajax({
            url: 'is-user-exists',
            type: 'GET',
            data: {username: $('#usernameInput').val()},

            success: function(json) {
                if (json) {
                    document.getElementById('userExists').style.display = 'block';
                }
                else document.getElementById('userExists').style.display = 'none';
            }
        });
    }
}

/**
 * Sends form only if both of password 'Input' lines are equals and filled.
 *
 * @param object 'event'
 */
function isSignInAvailable(event) {
    isUserExists = document.getElementById('userExists').style.display;
    isLinesEqual = document.getElementById('passWrongMessage').style.display;

    if (isUserExists === 'none' && isLinesEqual === 'none') event.submit();
}
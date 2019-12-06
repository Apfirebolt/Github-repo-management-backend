/**
 * Created by Amit on 06-12-2019, Client side validation for login form
 */

$(document).ready(() => {

    let form = $('form');
    let error = $('.error-container');
    let username = $('#username');
    let password = $('#password');
    let current_errors = [];
    error.hide();

    form.submit(function(e) {
    e.preventDefault();

    // Clear the html contents and hide the error container
    error.html('')
    current_errors = []

    // Get the values for validation
    if(username.val() == '')
        current_errors.push('Username is not defined!');
    if(password.val() == '')
        current_errors.push('Password is not defined!');

    if(current_errors.length > 0) {
        for(let i=0; i<current_errors.length; i++)
            error.append(`<p class="has-text-danger is-centered">${current_errors[i]}</p>`);

        error.fadeIn(1000, () => {
            setTimeout(() => {
                error.fadeOut(1200);
            }, 2000)
        });
    }

    // Submitting the form if no errors
    else
        this.submit();
    });
});
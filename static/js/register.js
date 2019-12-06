/**
 * Created by hp on 06-12-2019.
 */

$(function() {
    let form = $('form');
    let error = $('.error-container');
    let username = $('#id_username');
    let email = $('#id_email');
    let first_name = $('#id_first_name');
    let last_name = $('#id_last_name');
    let password = $('#id_password');
    let current_errors = [];

    form.hide();
    error.hide();
    form.fadeIn(1200, 'swing');

    form.submit(function(e) {
    e.preventDefault();

    // Clear the html contents and hide the error container
    error.html('')
    current_errors = []

    // Get the values for validation
    if(username.val() == '')
        current_errors.push('Username is required!');
    if(email.val() == '')
        current_errors.push('Email is required!');
    if(first_name.val() == '')
        current_errors.push('First Name is required!');
    if(last_name.val() == '')
        current_errors.push('Last Name is required!');
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
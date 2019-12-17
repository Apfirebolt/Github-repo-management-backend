/**
 * Created by Amit on 08-12-2019.
 */

$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie != '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    console.log('Test jquery script loaded', $('.amit'));
    $('#test-button').click(function () {
        $(this).animate({
            left: '250px',
            top: '200px',
            backgroundColor: 'red',
        }, 3000, 'swing', () => {
            console.log('Animation finally completed');
        });
    })

    $('#submit-btn').click((event) => {
        event.preventDefault();
        console.log('Default behaviour prevented!');

        let username = $('#username').val();
        let email = $('#email').val();
        let password = $('#password').val();
        let csrftoken = getCookie('csrftoken');

        let formData = {
            username: username,
            email: email,
            password: password
        }
        console.log('The posted data is : ', formData);

        $.ajax({
            type: 'POST',
            url: `http://localhost:8000/accounts/api/create`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: formData,
            success: function(response) {
                console.log('User successfully created..');
            },
            error: function(error) {
                console.log('Some error occurred!');
            }
        });
    })
});
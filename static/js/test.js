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

    console.log('Test Page loaded!');
    let csrftoken = getCookie('csrftoken');

    let test = $('#test-button').click(function () {
        $.ajax({
          type: "POST",
          url: 'http://localhost:8000/accounts/api/api-token-auth',
          data: {
              username: 'gokun',
              password: '9000power'
          },
          headers: {
                'X-CSRFToken': csrftoken
          },
          success: function(response) {
              console.log('So this was success', response);
          },
          error: function(error) {
              console.log('The request failed : ', error);
          },
        });
    })
});
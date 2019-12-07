/**
 * Created by Amit on 06-12-2019, scripts for the dashboard page
 */

$(document).ready(() => {
    // Function to get csrf token from cookies
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

    let delete_btn = $('.delete-btn');
    let favourite_btn = $('.favourite-btn');
    let unfavourite_btn = $('.unfavourite-btn');
    let current_index = 0;
    let result = $('#info-container');
    let csrftoken = getCookie('csrftoken');

    favourite_btn.click((event) => {
        current_index = event.target.getAttribute('data-store-id');

        $.ajax({
            type: 'PATCH',
            url: `http://localhost:8000/hub/api/star/${current_index}`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
              "is_favorited": true
            },
            success: function(response) {
                // Clear the current html
                result.html('');
                result.append(`
                          <p>Repo was successfully Starred!</p>`
                )
                result.fadeIn(1200, () => {
                    setTimeout(() => {
                        result.fadeOut(1200)
                    }, 2000);
                });
            },
            error: function(error) {
                console.log('Some error occurred!');
                result.html('<p> Some Error Occurred, cannot load data from the server </p>');
            }
        });
    });

    unfavourite_btn.click((event) => {
        current_index = event.target.getAttribute('data-store-id');

        $.ajax({
            type: 'PATCH',
            url: `http://localhost:8000/hub/api/star/${current_index}`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
              "is_favorited": false
            },
            success: function(response) {
                // Clear the current html
                result.html('');
                result.append(`
                          <p class="title has-white-text is-centered">Repo was successfully removed from favourites!</p>`
                )
                result.fadeIn(1200, () => {
                    setTimeout(() => {
                        result.fadeOut(1200)
                    }, 2000);
                });
            },
            error: function(error) {
                console.log('Some error occurred!');
                result.html('<p class="title has-text-white"> Some Error Occurred, cannot load data from the server </p>');
            }
        });
    });

    delete_btn.click((event) => {
        console.log('Delete button clicked..');
        current_index = event.target.getAttribute('data-store-id');

        $.ajax({
            type: 'DELETE',
            url: `http://localhost:8000/hub/api/delete/${current_index}`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                // Clear the current html
                result.html('');
                result.append(`
                          <p class="title has-white-text is-centered">Repo was successfully deleted!</p>`
                )
                result.fadeIn(1200, () => {
                    setTimeout(() => {
                        result.fadeOut(1200)
                    }, 2000);
                });
            },
            error: function(error) {
                console.log('Some error occurred!');
                result.html('<p class="title has-text-white"> Some Error Occurred, cannot load data from the server </p>');
            }
        });
    });

});

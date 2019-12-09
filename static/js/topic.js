$(document).ready(function() {
    console.log('Topic List page loaded!');

    // Function to get CSRF token
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

    let edit = $('.fa-edit');
    let modal = $('.edit-modal');
    let description = $('#edit_description');
    let submit_btn = $('#submit-btn');
    let current_index = 0;
    let csrftoken = getCookie('csrftoken');

    submit_btn.click((event) => {
        $.ajax({
            type: 'PATCH',
            url: `http://localhost:8000/hub/api/edit_description/${current_index}`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: {
              "topic_description": description.val()
            },
            success: function(response) {
                modal.prepend('<p class="has-text-centered has-text-success is-size-3"> Topic Description edited successfully</p>')
            },
            error: function() {
                modal.prepend('<p class="has-text-centered has-text-danger is-size-3">Some Error Occurred, edit operation failed</p>')
            }
        });
        setTimeout(() => {
            modal.fadeOut(1200);
            modal.firstChild('p').remove();
        }, 2000);
    });

    edit.click((event) => {
        modal.fadeIn(1200);
        modal.children("p").remove();
        current_index = event.target.getAttribute('data-store-id');
        console.log('Current index and stored value ', current_index, description);

    });
});
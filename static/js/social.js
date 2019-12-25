/*
 * Created by Amit on 24-12-2019.
 */

$(document).ready(() => {
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

   let parent_container = $('#social_container');
   let current_id = -1;
   let csrftoken = getCookie('csrftoken');

   parent_container.on('click', 'button.accept_request', function(event) {
       current_id = event.target.getAttribute('data-store-id');
       console.log('Accept request button clicked..', current_id);

       $.ajax({
          type: "PUT",
          url: 'http://localhost:8000/accounts/api/add_friend/' + current_id,
          data: {
            user_to: current_id,
            user_from: 1,
            accepted: true
          },
          headers: {
                'X-CSRFToken': csrftoken
          },
          success: function() {
            console.log('Add friend function was success..');
          },
          error: function() {
              console.log('Some error occurred, request failed to execute');
          }
       })
   });

   parent_container.on('click', 'button.cancel_request', function(event) {
       current_id = event.target.getAttribute('data-store-id');
       console.log('Cancel request button clicked..', current_id);
       $.ajax({
          type: "DELETE",
          url: 'http://localhost:8000/accounts/api/add_friend/' + current_id,

          headers: {
                'X-CSRFToken': csrftoken
          },
          success: function() {
            console.log('Successfully deleted the friend request..');
          },
          error: function() {
              console.log('Some error occurred, request failed to execute');
          }
       })
   });
});



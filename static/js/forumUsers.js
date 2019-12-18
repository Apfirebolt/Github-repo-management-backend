/**
 * Created by Amit on 17-12-2019.
 */

$(document).ready(function() {
   console.log('Jquery loaded on the forum users page..');

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

   let username = $('#search_name');
   let email = $('#search_email');
   let search_btn = $('#search-btn');
   let parent_container = $('.forum-user-container');
   let container = $('.search-container');
   let username_text = '';
   let email_text = '';
   let current_user = -1;
   let csrftoken = getCookie('csrftoken');

   username.on('keyup', function(event) {
       username_text = event.target.value;
   });

   email.on('keyup', function(event) {
       email_text = event.target.value;
   })

   parent_container.on('click', 'button.follow-btn', function(event) {
       current_user = event.target.getAttribute('data-store-id');
       console.log('Follow button clicked!!', current_user, csrftoken);

       $.ajax({
          type: "POST",
          url: 'http://localhost:8000/accounts/api/follow',
          data: {
            following: current_user,
          },
           headers: {
                'X-CSRFToken': csrftoken
          },
          success: function() {
              console.log('This was a success!');
              event.target.classList.add("is-danger");
              $(event.target).text('Unfollow');
          },
          error: function() {
              console.log('Some error occurred, request failed to execute');
          }
       })
   });

   search_btn.on('click', function () {
       $.ajax({
          type: "GET",
          url: 'http://localhost:8000/accounts/api/list',
          data: {
            username: username_text,
            email: email_text
          },
          success: function(res) {
              console.log('So this was success', res[0]);
              let content = '';
              for(let i=0; i<res.length; i++)
              {
                  content += `
                        <div class="item-container">
                            <div class="card">
                              <div class="card-image">
                                <figure class="image is-4by3">
                                  <img alt="Placeholder image" src=${res[i].profile_image}>
                                </figure>
                              </div>
                              <div class="card-content">
                                <div class="media">
                                  <div class="media-left">
                                    <figure class="image is-48x48">
                                      <img alt="Placeholder image" src=${res[i].profile_image}>
                                    </figure>
                                  </div>
                                  <div class="media-content">
                                    <p class="title is-4">${res[i].username}</p>
                                    <p class="subtitle is-6">${res[i].email}</p>
                                  </div>
                                </div>
            
                                <div class="content">
                                    <button class="button follow-btn" data-store-id=${res[i].id}>Follow</button>
                                    <button class="button is-dark add-btn" data-store-id=${res[i].id}>Add Friend</button>
                                    <button class="button is-link" data-store-id=${res[i].id}>View</button>
                                </div>
                              </div>
                            </div>
                        </div>
                        `;
              }
              parent_container.html(content);
          },
          error: function(error) {
              console.log('The request failed : ', error);
          },
        });
   });

   container.animate({
       "opacity": '1',
   }, 1200);

});

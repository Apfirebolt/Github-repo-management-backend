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

   // Function to get API data
   function successFunction(response) {

      console.log('So this was success', response);
      let content = '';
      let res = response.user_data;
      let follow_array = response.follow_data_array;
      let friend_array = response.friend_data_array;
      let accepted_friends = response.friend_accepted_array;

      let follow_class_names = ['button', 'follow-btn'];
      let unfollow_class_names = ['button', 'unfollow-btn', 'is-danger'];

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
                            <button class="${follow_array.indexOf(res[i].id) != -1 ? unfollow_class_names.join(' ') : 
                            follow_class_names.join(' ') }" data-store-id=${res[i].id}>
                            ${follow_array.indexOf(res[i].id) != -1 ? 'Unfollow' : 'Follow'}</button>
                            ${accepted_friends.indexOf(res[i].id) == -1 && friend_array.indexOf(res[i].id) == -1 ?
                                `<button class="button is-dark add-friend-btn" data-store-id=${res[i].id}>Add Friend</button>` : ''
                            }
                            ${accepted_friends.indexOf(res[i].id) == -1 && friend_array.indexOf(res[i].id) != -1 ?
                                `<button class="button is-warning cancel-friend-btn" data-store-id=${res[i].id}>Cancel Request</button>` : ''
                            }
                            ${accepted_friends.indexOf(res[i].id) != -1 && friend_array.indexOf(res[i].id) == -1 ?
                                `<button class="button remove-friend-btn" data-store-id=${res[i].id}>Remove Friend</button>` : ''
                            }
                            <button class="button is-link" data-store-id=${res[i].id}>View</button>
                        </div>
                      </div>
                    </div>
                </div>
                `;
      }
      parent_container.html(content);
   }

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
              $.ajax({
                type: "GET",
                url: 'http://localhost:8000/accounts/api/list',
                success: function(res) {
                    successFunction(res);
                },
                error: function(error) {
                    console.log('The request failed : ', error);
                },
            });
          },
          error: function() {
              console.log('Some error occurred, request failed to execute');
          }
       })
   });

   // Unfollow button functionality
    parent_container.on('click', 'button.unfollow-btn', function(event) {
       current_user = event.target.getAttribute('data-store-id');
       console.log('Not follow button clicked!!', current_user, csrftoken);

       $.ajax({
          type: "DELETE",
          url: 'http://localhost:8000/accounts/api/un_follow/' + current_user,
          data: {
            following: current_user,
          },
           headers: {
                'X-CSRFToken': csrftoken
          },
          success: function() {
              $.ajax({
                type: "GET",
                url: 'http://localhost:8000/accounts/api/list',
                success: function(res) {
                    successFunction(res);
                },
                error: function(error) {
                    console.log('The request failed : ', error);
                },
            });
          },
          error: function() {
              console.log('Some error occurred, request failed to execute');
          }
       })
   });

   // Add Friend Functionality
    parent_container.on('click', 'button.add-friend-btn', function(event) {
       current_user = event.target.getAttribute('data-store-id');
       console.log('Add Friend button clicked!!', current_user);

       $.ajax({
          type: "POST",
          url: 'http://localhost:8000/accounts/api/friend',
          data: {
            user_to: current_user,
            user_from: 1
          },
           headers: {
                'X-CSRFToken': csrftoken
          },
          success: function() {
              $.ajax({
                type: "GET",
                url: 'http://localhost:8000/accounts/api/list',
                success: function(res) {
                    successFunction(res);
                },
                error: function(error) {
                    console.log('The request failed : ', error);
                },
            });
          },
          error: function() {
              console.log('Some error occurred, request failed to execute');
          }
       })
   });

    // Remove friend functionality
    parent_container.on('click', 'button.remove-friend-btn', function(event) {
       current_user = event.target.getAttribute('data-store-id');
       console.log('Remove Friend button clicked!!', current_user);

      $.ajax({
          type: "DELETE",
          url: 'http://localhost:8000/accounts/api/cancel_friend/' + current_user,

          headers: {
                'X-CSRFToken': csrftoken
          },
          success: function() {
              $.ajax({
                type: "GET",
                url: 'http://localhost:8000/accounts/api/list',
                success: function(res) {
                    successFunction(res);
                },
                error: function(error) {
                    console.log('The request failed : ', error);
                },
            });
          },
          error: function() {
              console.log('Some error occurred, request failed to execute');
          }
       })
   });

    // Cancel Friend Request Functionality
    parent_container.on('click', 'button.cancel-friend-btn', function(event) {
       current_user = event.target.getAttribute('data-store-id');
       console.log('Cancel Friend clicked!!', current_user);

       $.ajax({
          type: "DELETE",
          url: 'http://localhost:8000/accounts/api/cancel_friend/' + current_user,

          headers: {
                'X-CSRFToken': csrftoken
          },
          success: function() {
              $.ajax({
                type: "GET",
                url: 'http://localhost:8000/accounts/api/list',
                success: function(res) {
                    successFunction(res);
                },
                error: function(error) {
                    console.log('The request failed : ', error);
                },
            });
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
            successFunction(res);
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

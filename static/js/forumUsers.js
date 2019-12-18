/**
 * Created by Amit on 17-12-2019.
 */

$(document).ready(function() {
   console.log('Jquery loaded on the forum users page..');

   let username = $('#search_name');
   let email = $('#search_email');
   let search_btn = $('#search-btn');
   let parent_container = $('.forum-user-container');
   let container = $('.search-container');
   let username_text = '';
   let email_text = '';

   username.on('keyup', function(event) {
       username_text = event.target.value;
       console.log('Something typed..', username_text);
   });

   email.on('keyup', function(event) {
       email_text = event.target.value;
       console.log('Something typed..', email_text);
   })


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
                                    <button class="button">Follow</button>
                                    <button class="button is-dark">Add Friend</button>
                                    <button class="button is-link">View Profile</button>
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
   });

});

/**
 * Created by Amit on 05-12-2019. Javascript functions for search User page
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

    let result = $('.profile-container');
    let search_text = $('#username');
    let input_text = '';
    let current_data = {};
    let response_data = {};
    let csrftoken = getCookie('csrftoken');

    search_text.focusout(function(event){
        input_text = event.target.value;
    });

    result.on('click', '#save-profile', function(event) {
        event.preventDefault();
        console.log('Save Profile method called..');

        current_data.user_name = response_data.login;
        current_data.user_url = response_data.html_url;
        current_data.user_image_url = response_data.avatar_url;

        console.log('Current data is : ', current_data);
        $.ajax({
          type: "POST",
          url: 'http://localhost:8000/hub/api/user',
          data: current_data,
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
    });

    $("button.my-btn").click(function(event) {
        event.preventDefault();
        result.hide(400);

        if(input_text == '') {
            result.html(
                `<div class="error-container">
                    <p>Please Type in a Username to search!</p>
                 </div>`);
            result.fadeIn(500, 'swing', () => {
                result.fadeOut(1500);
            });
            return false;
        }
        $.ajax({
            type: 'GET',
            url: `https://api.github.com/users/${input_text}`,
            success: function(response) {
                // Clear the current html
                result.html('');
                response_data = response;
                console.log('The response data is : ', response_data);
                result.html(`
                    <div class="card">
                        <div class="card-header">
                            <p>${response.name}</p> <p>${response.login}</p> <p>${response.location ? response.location : null}</p>
                        </div>
                        <div class="card-content">
                            <div class="card-image">
                                <figure class="image">
                                    <img src=${response.avatar_url} alt="Profile Image Not Found" 
                                    height="300" width="300">
                                </figure>
                            </div>
                            <p>Biography - ${response.bio}</p>
                            <p>Profile Url - <a href=${response.html_url}>Github Profile</a></p>
                            <p>Company - ${response.company}</p>
                            <p>All Repositories for this user - ${response.repos_url}</p>
                            <p>${response.name} has ${response.public_repos} Public Repositories</p>
                            <a href=${response.repos_url}></a>
                        </div>
                        <div class="card-footer">
                            <a href="#" class="card-footer-item">${response.followers} Followers</a>
                            <a href="#" class="card-footer-item">${response.following} Following</a>
                            <a href="#" class="card-footer-item" id="save-profile">Favorite</a>
                        </div>
                    </div>
                `);
            },
            error: function(error) {
                result.html('<p class="title has-text-white"> Some Error Occurred, cannot load data from the server </p>');
            }
        });
        result.fadeIn(1000);
    });
});
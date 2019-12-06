/**
 * Created by Amit on 05-12-2019. Javascript functions for search User page
 */

$(document).ready(function() {
    let result = $('.profile-container');
    let search_text = $('#username');
    let input_text = '';

    search_text.focusout(function(event){
        input_text = event.target.value;
    });

    $("button.my-btn").click(function(event) {
        event.preventDefault();
        result.hide(400);

        $.ajax({
            type: 'GET',
            url: `https://api.github.com/users/${input_text}`,
            success: function(response) {
                // Clear the current html
                result.html('');
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
                            <a href="#" class="card-footer-item">Favorite</a>
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
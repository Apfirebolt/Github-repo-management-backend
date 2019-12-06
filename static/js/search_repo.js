/**
 * Created by Amit on 05-12-2019. Javascript functions for search Repo page
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

    let result = $('.repo-container');
    let search_text = $('#repo_name');
    let sort_by_value = $('#sort_by');
    let order_by_value = $('#order_by');
    let input_text = '';
    let sort_by_value_text = 'stars';
    let order_by_value_text = 'asc';
    let current_data = {};
    let current_index = 0;
    let items = [];
    let csrftoken = getCookie('csrftoken');

    // Calling methods on dynamic jquery elements, change current index
    result.on('click', 'a.save_link', function(event) {
        current_index = event.target.getAttribute('data-store-id');
        // console.log('Item at current index : ', items[current_index]);

        current_data.repo_name = items[current_index].name;
        current_data.repo_creator = items[current_index].owner.login;
        current_data.repo_language = items[current_index].language ? items[current_index].language : 'Language not specified';
        current_data.repo_description = items[current_index].description ? items[current_index].description : '';
        current_data.repo_url = items[current_index].html_url;
        current_data.repo_forked = items[current_index].forks_count ? items[current_index].forks_count : 0;
        current_data.repo_watchers = items[current_index].watchers_count ? items[current_index].watchers_count : 0;
        current_data.repo_score = items[current_index].score ? Math.ceil(items[current_index].score) : 0;
        current_data.repo_stars = items[current_index].stargazers_count ? items[current_index].stargazers_count : 0;
        current_data.repo_created_on = items[current_index].created_at;

        $.ajax({
          type: "POST",
          url: 'http://localhost:8000/hub/api/create',
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

    search_text.focusout(function(event){
        input_text = event.target.value;
        console.log('Input text is ', input_text);
    });

    sort_by_value.change(function(event){
        sort_by_value_text = event.target.value;
    });

    order_by_value.change(function(event){
        order_by_value_text = event.target.value;
    });


    $("button.my-btn").click(function(event) {
        event.preventDefault();
        result.hide(400);
        $.ajax({
            type: 'GET',
            url: `https://api.github.com/search/repositories?q=${input_text}&sort=${sort_by_value_text}&order=${order_by_value_text}`,
            success: function(response) {
                // Clear the current html
                items = response.items;
                result.html('');

                for(let i=0; i<response.items.length; i++)
                {
                    result.append(`
                        <div class="card">
                          <div class="card-header is-centered">
                            <p class="subtitle">${response.items[i].name} - ${response.items[i].owner.login}</p>
                          </div>  
                          <div class="card-content">
                            <div class="content">
                              <p>Made in <span class="subtitle is-warning">${response.items[i].language}</span></p>
                              <p>Project url : <a href=${response.items[i].html_url}>${response.items[i].html_url}</a></p>
                              <p>This repo was forked ${response.items[i].forks_count} times.</p>
                              <br>
                              <time datetime="2016-1-1" class="text-warning">${response.items[i].created_at}</time>
                            </div>
                          </div>
                          <footer class="card-footer">
                            <a href="#" class="card-footer-item">${response.items[i].stargazers_count} Stars</a>
                            <a href="#" class="card-footer-item">${response.items[i].watchers_count} Watchers</a>
                            <a href="#" class="card-footer-item">Score is ${response.items[i].score}</a>
                            <a class="card-footer-item save_link" data-store-id=${i} >Save</a>
                            <a href="#" class="card-footer-item">Mark Favorite</a>
                          </footer>
                        </div>
                    `)
                }
            },
            error: function(error) {
                result.html('<p class="title has-text-white"> Some Error Occurred, cannot load data from the server </p>');
            }
        });
        result.fadeIn(1500);
    });
});
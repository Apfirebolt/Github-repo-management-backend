/**
 * Created by Amit on 05-12-2019. Javascript functions for search topic page
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

    let result = $('.result-container');
    let search_text = $('#topic_name');
    let input_text = '';
    let btn = $('.my-btn');
    let topic_results = [];
    let current_index = 0;
    let current_data = {};
    let csrftoken = getCookie('csrftoken');

    search_text.focusout(function(event){
        input_text = event.target.value;
    });

    result.on('click', '.save-topic', function(event) {
        event.preventDefault();
        current_index = event.target.getAttribute('data-store-id');

        current_data.topic_name = topic_results[current_index].name;
        current_data.topic_score = Math.ceil(topic_results[current_index].score);
        current_data.topic_description = topic_results[current_index].description ?
            topic_results[current_index].description : 'No Topic Description Provided' ;


        $.ajax({
          type: "POST",
          url: 'http://localhost:8000/hub/api/topic',
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

    btn.click(function(event) {
        event.preventDefault();
        result.hide();

        $.ajax({
            type: 'GET',
            beforeSend: function(request) {
            request.setRequestHeader("Accept", "application/vnd.github.mercy-preview+json");
          },
            url: `https://api.github.com/search/topics?q=${input_text}`,
            success: function(response) {
                // Clear the current html
                result.html('');
                topic_results = response.items;
                for(let i=0; i<response.items.length; i++)
                {
                    result.append(`
                        <div class="card">
                          <div class="card-header">
                            <p class="subtitle">${response.items[i].name} ${response.items[i].display_name ? (response.items[i].display_name) : ''}</p>
                          </div>  
                          <div class="card-content">
                            <div class="content">
                              ${response.items[i].description}
                              <br>
                              <time datetime="2016-1-1" class="text-warning">${response.items[i].created_at}</time>
                              <p class="is-success">${response.items[i].created_by}</p>
                            </div>
                          </div>
                          <footer class="card-footer">
                            <a class="card-footer-item">Score is ${response.items[i].score}</a>
                            <a class="card-footer-item save-topic" data-store-id=${i}>Save</a>
                            <a class="card-footer-item">Mark Favorite</a>
                          </footer>
                        </div>
                    `)
                }
                result.fadeIn();
            },
            error: function(error) {
                console.log('Some error occurred!');
                result.html('<p class="title has-text-white"> Some Error Occurred, cannot load data from the server </p>');
            }
        });
    });
});

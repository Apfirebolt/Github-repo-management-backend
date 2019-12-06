/**
 * Created by Amit on 05-12-2019. Javascript functions for search topic page
 */

$(document).ready(function() {
    let result = $('.result-container');
    let search_text = $('#topic_name');
    let input_text = '';
    let btn = $('.my-btn');

    search_text.focusout(function(event){
        input_text = event.target.value;
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
                            <a href="#" class="card-footer-item">Score is ${response.items[i].score}</a>
                            <a href="#" class="card-footer-item">Save</a>
                            <a href="#" class="card-footer-item">Mark Favorite</a>
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

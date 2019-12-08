/**
 * Created by Amit on 07-12-2019, All Javascript for Blog category
 */

$(document).ready(function() {

    // Function to extract CSRF token
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

    let delete_blog = $('.delete-blog');
    let delete_blog_post = $('.delete-blog-post');
    let modal = $('.global-modal');
    let csrftoken = getCookie('csrftoken');
    let current_index = 0;
    let result = $('.global-modal');


    // Method to delete Blog
    delete_blog.click((event) => {

        current_index = event.target.getAttribute('data-store-id');
        $.ajax({
            type: 'DELETE',
            url: `http://localhost:8000/blog/api/blog-delete/${current_index}`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                result.html('');
                result.append(`
                          <p class="title has-white-text has-text-centered">Blog was successfully deleted!</p>`
                )
                result.fadeIn(1200, () => {
                    setTimeout(() => {
                        result.fadeOut(1200)
                    }, 2000);
                });
            },
            error: function(error) {
                console.log('Some error occurred!');
                result.html('<p class="title has-text-white"> Some Error Occurred, cannot load data from the server </p>');
            }
        });
    });

    // Method to delete Blog Post
    delete_blog_post.click((event) => {

        current_index = event.target.getAttribute('data-store-id');

        $.ajax({
            type: 'DELETE',
            url: `http://localhost:8000/blog/api/post-delete/${current_index}`,
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                result.html('');
                result.append(`
                          <p>Blog Post was successfully deleted!</p>`
                )
                result.fadeIn(1200, () => {
                    setTimeout(() => {
                        result.fadeOut(1200)
                    }, 2000);
                });
            },
            error: function(error) {
                console.log('Some error occurred!');
                result.html('<p class="title has-text-white"> Some Error Occurred, cannot load data from the server </p>');
            }
        });
    });
});

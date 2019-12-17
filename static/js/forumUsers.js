/**
 * Created by Amit on 17-12-2019.
 */

$(document).ready(function() {
   console.log('Jquery loaded on the forum users page..');

   let username = $('#search_name');
   let email = $('#search_email');
   let search_btn = $('#search-btn');
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
              console.log('So this was success', res);
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

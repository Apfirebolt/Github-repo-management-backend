/**
 * Created by Amit on 08-12-2019.
 */

$(document).ready(function() {
    console.log('Test jquery script loaded');
    $('#test-button').click(function () {
        $(this).animate({
            left: '250px',
            top: '200px',
            backgroundColor: 'red',
        }, 3000, 'swing', () => {
            console.log('Animation finally completed');
        });
    })
});
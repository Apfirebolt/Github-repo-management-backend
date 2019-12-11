/**
 * Created by Amit on 08-12-2019.
 */

$(document).ready(function() {
    console.log('Test Page loaded!');
    let container = $('.global-modal');

    $('.test-btn').on('click', (e) => {
        let yPos = $('.test-btn').position().top;

        container.fadeIn(200);
        container.animate({
            'top': yPos*2,
        }, 2000)
    })
});
// const user_input = $("#user-input")
const cart_icon = $('#cart-icon')
const cart_goods_div = $('#replaceable-cart-content')
const cart_endpoint = '/cart/view_cart/'
const cart_delay_by_in_ms = 0
// let scheduled_function = false


let cart_ajax_call = function (endpoint) {
    $.getJSON(endpoint)
        .done(response => {
            // fade out the goods_div, then:
            cart_goods_div.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                cart_goods_div.html(response['html_from_cart_view'])
                // fade-in the div with new contents
                cart_goods_div.fadeTo('slow', 1)
            })
        })
}

$(document).ready(function () {
//
//     const request_parameters = {
//         q: $(this).val() // value of user_input: the HTML element with ID user-input
//     }
//
//     // start animating the search icon with the CSS class
//     search_icon.addClass('blink')
//
//     // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, cart_delay_by_in_ms, cart_endpoint)
})
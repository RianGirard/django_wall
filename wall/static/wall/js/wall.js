$(document).ready(function(){
    $('#delete_message').click(function(){
        console.log('hi')
        let message = $('#message_id').value        // jquery "submit" creates a list, as opposed to just a value, so we need to grab the [0] position value
        console.log(message)
        $.ajax({
            method: "GET",
            url: "delete_message/"+message,
            })
    })



})
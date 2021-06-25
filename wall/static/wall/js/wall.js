$(document).ready(function(){
    $('.delete_message').click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'delete_message',
            method: 'POST',
            data: $(this).serialize(),
            success: function(serverResponse){
                if ((serverResponse).indexOf('Item Deleted') > -1){
                    location.reload();
                } else {
                    $('.delete_response').html(serverResponse)
                }
            }
        })
    })

    $('.delete_comment').click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'delete_comment',
            method: 'POST',
            data: $(this).serialize(),
            success: function(serverResponse){
                if ((serverResponse).indexOf('Item Deleted') > -1){
                    location.reload();
                } else {
                    $('.delete_response').html(serverResponse)
                }
            }
        })
    })

    $('.enter_comment').submit(function(e){
        e.preventDefault()
        $.ajax({
            url: 'enter_comment',
            method: 'POST',
            data: $(this).serialize(),
            success: function(serverResponse){
                location.reload();
            }
        })
    })

})
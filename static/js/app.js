$(".comment_reply").click(function(){
    comment_id = this.id.substr(11);
    replies = document.getElementsByClassName('comment_wrapper')
    for (let i = 0; i < replies.length; i++) {
        replies[i].innerHTML = '';
    }
    document.querySelector(`#comment_wrapper_${comment_id}`).classList.toggle("mystyle");
    if (document.querySelector(`#comment_wrapper_${comment_id}`).classList.contains('mystyle')) {
        // $(`<input type="hidden" name="parent" value="${comment_id}">`).appendTo("#comment_form form");
        // var myForm = $("#comment_form").clone();
        var parentInput = $(`<input type="hidden" value="${comment_id}">`);
        var replyButton = $('<input type="submit" value="Reply" class="btn py-3 px-4 btn-primary">');
        var replyArea = $('<div class="form-group"><textarea id="reply_text" name="text" rows="5" class="form-control">');
        parentInput.appendTo(replyArea);
        replyButton.appendTo(replyArea);
        replyArea.appendTo(`#comment_wrapper_${comment_id}`);
    }

    $(replyButton).click(function(){

        var parent_id = parentInput.val();
        $('#parent').val(parent_id);
        $('#id_text').val($('#reply_text').val());
        $('#form').submit();
        replies = document.getElementsByClassName('comment_wrapper')
        for (let i = 0; i < replies.length; i++) {
            replies[i].innerHTML = '';
        }
    })
});



// $('#id_tag').tagsInput({
//     'unique': true,
//     'minChars': 2,
//     'maxChars': 10,
//     'limit': 3,
//     'delimiter': [',', ';']
// });
  

// document.getElementById("id_tag_tag").addEventListener("keyup", function () {
//     tag = this.value;

//     $.ajax({
//         url: "http://localhost:8000/api-story/?tag=" + tag,
//         method: 'GET',
//         success: function (results) {
//             var availableTags = [];
//             for(let tag of results){
//                 availableTags.push(tag['name'].toUpperCase());
//             };
//             console.log([availableTags, availableTags]);
            
//             $("#id_tag_tag").autocomplete({
//                 source: availableTags,
//             });
//         },
//         error: function (error) {
//             console.log(error);
//             console.log('error')
//         },
//     });
// });






var loc = window.location;
var wsStart = 'ws://';
if (loc.protocol == 'https:'){
    wsStart = 'wss://';
}
var endpoint = wsStart + loc.host + loc.pathname;
var socket = new ReconnectingWebSocket(endpoint);
// var socket = new WebSocket(endpoint);

socket.onmessage = function(e) {
    console.log('message', e);
    var data_response = JSON.parse(e.data);
    console.log(data_response);
    var comment_li = $(`<li class="comment" id='comment_id_${data_response.comment_id}'><div class="comment-body"></div></li>`);
    var user_image = $(`<div class="vcard bio"><img src="/static/images/person_1.jpg" alt="Image placeholder"></div>`);

    var comment_body = $(`<div class="comment-body"></div>`);
        var comment_user = $(`<h3>${data_response.first_name} ${data_response.last_name}</h3>`);
        var comment_date = $(`<div class="meta">${data_response.updated_at}</div>`);
        var comment_text = $(`<p>${data_response.text}</p>`);
        var reply_button = $(`<button class='comment_reply' id="comment_id_${data_response.comment_id}">Reply</button>`);
        comment_user.appendTo(comment_body);
        comment_date.appendTo(comment_body);
        comment_text.appendTo(comment_body);
        reply_button.appendTo(comment_body);

    var comment_wrapper = $(`<div id="comment_wrapper_${data_response.comment_id}" class="comment_wrapper"></div>`);
    user_image.appendTo(comment_li);
    comment_body.appendTo(comment_li);
    comment_wrapper.appendTo(comment_li);
    if (data_response.parent_id == '') {
        comment_li.appendTo($('#comment-list'))
    }else{
        comment_children = $(`<ul class="children"></ul>`);
        comment_li.appendTo(comment_children);
        comment_children.appendTo($(`#comment_id_${data_response.parent_id}`));
    }


    
    $(".comment_reply").click(function(){
        comment_id = this.id.substr(11);
        replies = document.getElementsByClassName('comment_wrapper')
        for (let i = 0; i < replies.length; i++) {
            replies[i].innerHTML = '';
        }
        document.querySelector(`#comment_wrapper_${comment_id}`).classList.toggle("mystyle");
        if (document.querySelector(`#comment_wrapper_${comment_id}`).classList.contains('mystyle')) {
            // $(`<input type="hidden" name="parent" value="${comment_id}">`).appendTo("#comment_form form");
            // var myForm = $("#comment_form").clone();
            var parentInput = $(`<input type="hidden" value="${comment_id}">`);
            var replyButton = $('<input type="submit" value="Reply" class="btn py-3 px-4 btn-primary">');
            var replyArea = $('<div class="form-group"><textarea id="reply_text" name="text" rows="5" class="form-control">');
            parentInput.appendTo(replyArea);
            replyButton.appendTo(replyArea);
            replyArea.appendTo(`#comment_wrapper_${comment_id}`);
        }
    
        $(replyButton).click(function(){
    
            var parent_id = parentInput.val();
            $('#parent').val(parent_id);
            $('#id_text').val($('#reply_text').val());
            $('#form').submit();
            replies = document.getElementsByClassName('comment_wrapper')
            for (let i = 0; i < replies.length; i++) {
                replies[i].innerHTML = '';
            }
        })
    });
};

socket.onopen = function(e) {
    console.log('open', e);
    $('#form').submit(function(event){
        event.preventDefault()
        var commentText = $('#id_text').val();
        var parentId = $('#parent').val();
        socket.send(JSON.stringify({
            'text': commentText,
            'parent_id': parentId ,
        }))
        $('#id_text').val("");
        $('#reply_text').val("");
        $('#parent').val("");
        });
};

socket.onerror = function(e) {
    console.log('error', e);
}

socket.onclose = function(e) {
    console.log('close', e);
}

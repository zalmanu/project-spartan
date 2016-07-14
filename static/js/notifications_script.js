notif_socket = new WebSocket("ws://" + window.location.host);
notif_socket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    var username = $('#user_name_not').text();
    if(username.value != data.author){
        $("#noti-list").append(data.html);
    }
}

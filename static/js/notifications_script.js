notif_socket = new WebSocket("ws://" + window.location.host);
notif_socket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    username = document.getElementById("user_name_not");
    if(username.value != data.author){
        $("#notif_list").append(data.html);
    }
}

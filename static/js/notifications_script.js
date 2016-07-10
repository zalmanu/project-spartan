notif_socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
notif_socket.onopen = function(message) {
    var username = document.getElementById("user_name_not");
}

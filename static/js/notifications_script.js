notif_socket = new WebSocket("ws://" + window.location.host);
notif_socket.onmessage = function(message) {
    print message.data
    var data = JSON.parse(message.data);
    console.log("what");
    console.log(data.mesaj);
}

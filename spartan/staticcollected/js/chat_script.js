 socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
 function sendmessage() {
     field = document.getElementById("textcase");
     url_path = window.location.href.split('/');
     len = url_path.length;
     message = {
         message: field.value,
         room: url_path[len - 2]
     }
    socket.send("wat");
    return false;
}

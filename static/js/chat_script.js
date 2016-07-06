socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
function sendmessage() {o
     var field = document.getElementById("textcase");
     var username = document.getElementById("user_name");
     var url_path = window.location.href.split('/');
     var len = url_path.length;
     message = {
         message: field.value,
         room: url_path[len - 2],
	 user: username.value
	 
     }
     socket.send(JSON.stringify);
    return false;
 }
socket.onmessage = function(message){
    var data = JSON.parse(message.data);
    var elem = docuemnt.getElementById("chat-frame");
    elem.innerHTML = data.message;
}

socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
 function sendmessage() {
 var field = document.getElementById("chat-input");
 if(field.value == '')return false;
     var username = document.getElementById("user_name_not");
     var url_path = window.location.href.split('/');
     var len = url_path.length;
     message = {
         text: field.value,
         room_slug: url_path[len - 2],
	 user_name: username.value
     }
     socket.send(JSON.stringify(message));
     field.value = '';
     return false;
 }
socket.onmessage = function(message){
    var data = JSON.parse(message.data);
    var elem = document.getElementById("chat-body");
    var list = document.getElementById("mesg-list");
    console.log(list.);
    var user = data.username;
    var clas ='profile-img pull-left';
    if(user == data.submitter)clas='profile-img pull-right';
    $("#message-list").append("<a><li><img class=\""+ clas + "\">" + data.html);
    elem.scrollTop = objDiv.scrollHeight;
 }

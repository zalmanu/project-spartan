socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
function sendmessage() {
 var field = document.getElementById("chat-input");
 if(field.value == '')return false;
     var username = $('#user_name_not').text();
     var url_path = window.location.href.split('/');
     var len = url_path.length;
     message = {
         text: field.value,
         room_slug: url_path[len - 2],
	 user_name: username
     };
     socket.send(JSON.stringify(message));
     field.value = '';
     return false;
 }
socket.onmessage = function(message){
    var data = JSON.parse(message.data);
    if(data.type == "chat_mess"){
	var chat_audio = document.getElementById("chat_sound");    
	var elem = document.getElementById("chat-body");
	var list = document.getElementById("mesg-list");
	var clas ='profile-img pull-left';
	var username = $('#user_name_not').text();
	if(username == data.submitter)clas='profile-img pull-right';
	$("#mesg-list").append("<a><li><img src=\"" + data.img + "\"class=\""+ clas + "\">" + data.html);
	elem.scrollTop = objDiv.scrollHeight;
	chat_audio.play();
    }
 }

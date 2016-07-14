socket = new WebSocket("ws://" + window.location.host + window.location.pathname);
 function sendmessage() {
 var field = document.getElementById("textcase");
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
     var elem = document.getElementById("mesg");
     var username = document.getElementById("user_name_not");
     var clas ='other';
     if(username.value == data.submitter)clas='self';
     $("#mesg").append("<li class=" + clas + ">" + data.html);
     elem.scrollTop = objDiv.scrollHeight;
 }

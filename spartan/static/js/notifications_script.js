notif_socket = new WebSocket("ws://" + window.location.host);
notif_socket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    var username = $('#user_name_not').text();
    var noti_audio = document.getElementById("notification_sound");
    var chat_audio = document.getElementById("chat_sound");    
    if(username != data.author){
	if(data.type == "chat"){
	    current_location = window.location.pathname.split("/");
	    url = data.url.split("/");
	    if(current_location.length > 3 && url[2] == current_location[2]){
		$.post("/delete/", {"id": data.id});
	    }
	    else{
		$("#chat-noti-bar-list").append(data.html);
		var in_dropdown = document.getElementById("chatnum");
		var in_bar = document.getElementById("chatcount");
		in_dropdown.innerHTML = parseInt(in_dropdown.innerHTML) + 1;
		in_bar.innerHTML = "<i class=\"fa fa-comments-o\">"+parseInt(in_dropdown.innerHTML);
		chat_audio.play();
	    }
	}
	else {
            $("#noti-list").append(data.html);
	    var in_dropdown = document.getElementById("notifnum");
	    var in_bar = document.getElementById("iconcount");
	    in_dropdown.innerHTML = parseInt(in_dropdown.innerHTML) + 1;
	    in_bar.innerHTML = "<i class=\"glyphicon glyphicon-globe\"></i>"+parseInt(in_dropdown.innerHTML);
	    noti_audio.play();
	}
    }
}

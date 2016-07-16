notif_socket = new WebSocket("ws://" + window.location.host);
notif_socket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    var username = $('#user_name_not').text();
    var in_dropdown = document.getElementById("notifnum");
    var in_bar = document.getElementById("iconcount");
    console.log(data.author);
    if(username != data.author){
        $("#noti-list").append(data.html);
	in_dropdown.innerHTML = parseInt(in_dropdown.innerHTML) + 1;
	in_bar.innerHTML = "<i class=\"fa fa-star-half-o\"></i>"+parseInt(in_dropdown.innerHTML);
    }
}

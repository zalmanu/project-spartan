var seennumber = 0;
function seencheck(){
    var elem = document.getElementById("notifnum");
    var iconcount = document.getElementById("iconcount");
    if(seennumber)
	iconcount.innerHTML += seennumber;
    elem.innerHTML = seennumber;
}

function seen_not(notif_data){
    var notif = notif_data;
    $.post("/seen/", { 'notif': notif }, function(response) {
        if (response.result == "success") {
	    var in_dropdown = document.getElementById("notifnum");
	    var in_bar = document.getElementById("iconcount");
	    var seen_bar = document.getElementById(notif);
	    in_dropdown.innerHTML = parseInt(in_dropdown.innerHTML) - 1;
	    if(in_dropdown.innerHTML > 0)
		in_bar.innerHTML = "<i class=\"fa fa-star-half-o\"></i>"+parseInt(in_dropdown.innerHTML);
	    else
		in_bar.innerHTML = "<i class=\"fa fa-star-half-o\"></i>";
	    if(response.type == "post")
		seen_bar.innerHTML = "<i class=\"fa\"></i>New post in your area";
	    else
		seen_bar.innerHTML = "<i class=\"fa\"></i> Someone bid on your post";		
        }
    })
    return true;
}

  

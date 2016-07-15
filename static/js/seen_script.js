var seennumber = 0;
function seencheck(){
    var elem = document.getElementById("notifnum");
    var iconcount = document.getElementById("iconcount");
    if(seennumber)
	iconcount.innerHTML += seennumber;
    elem.innerHTML = seennumber;
}

$(document).ready(function(){
        $("#seen_notif_req").hover(function(event){
            var notif = $(this).data("notification");
            $.post("/seen/", { 'notif': notif }, function(response) {
                if (response.result == "success") {
		    var in_dropdown = document.getElementById("notifnum");
		    var in_bar = document.getElementById("iconcount");
		    var seen_bar = document.getElementById("seen_notif_req");
		    in_dropdown.innerHTML = parseInt(in_dropdown.innerHTML) - 1;
		    in_bar.innerHTML = "<i class=\"fa fa-star-half-o\"></i>"+parseInt(in_dropdown.innerHTML);
		    seen_bar.firstChild.nextSibling.innerHTML = "<i class=\"fa\"></i>New post in your area";
                 }
            })
            return true;
        });
    });
    
    

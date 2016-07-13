var seennumber = 0;
function seencount(seenstatus){
    if (seenstatus == false){
	seennumber++;
    }
}

function seencheck(){
    var elem = document.getElementById("notifnum");
    var iconcount = document.getElementById("iconcount");
    if(seennumber == 0){
	iconcount.remove()
    }
    else{
	iconcount.innerHTML = seennumber;
    }
    elem.innerHTML = "You have " + seennumber + " new notifications";
}

$(document).ready(function(){
        $("#seen_not").hover(function(event){
            var notif = $(this).data("notification");
            $.post("/seen/", { 'notif': notif }, function(response) {
                if (response.result == "success") {
		    var iconcount = document.getElementById("iconcount");
		    var elem = document.getElementById("seen_not");
		    var seennum = parseInt(iconcount.innerHTML);
		    var elem_up = document.getElementById("notifnum");
		    seennum--;
		    if(seennum == false)
			iconcount.remove()
		    else 
			iconcount.innerHTML = seennum.toString();	
		    elem_up.innerHTML = "You have " + seennum + " new notifications";	    
		    elem.id = "";
		    elem.style = "";
		    iconc
                 }
            })
            return true;
        });
    });
    

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
	elem.innerHTML = "No new notifications";
	iconcount.remove()
    }
    else{
	elem.innerHTML = "You have " + seennumber + " new notifications";
	iconcount.innerHTML = seennumber;
    }
}

$(document).ready(function(){
        $("#seen_not").hover(function(event){
            var notif = $(this).data("notification");;
            $.post("/seen/", { 'notif': notif }, function(response) {
                 if (response.result == "success") {
                     console.log("success");
                 }
            })
            return true;
        });
    });
    

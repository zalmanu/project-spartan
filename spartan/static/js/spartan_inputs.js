$(document).ready(function(){
    $("#cuifield").keydown(function(){
	if((event.keyCode == 8 || event.keyCode == 46) && this.value.length == 2)
	    return false;
	return true;
    });
});

$(document).ready(function(){
    $("#cuifield").keyup(function(){
	if(this.value.substring(0, 2) != "RO")
	    this.value = "RO";
	return true;
    });
});

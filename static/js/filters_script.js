function ask_for_posts(obj, path, type){
    var dict_values = {
	'category': path
    };
    switch(type){
    case "maxprice":
	dict_values["maxprice"] = obj;
	break;
    case "minprice":
	dict_values["minprice"] = obj;
	break;
    case "city":
	dict_values["city"] = obj;
	break;
    case "date":
	dict_values["date"] = obj;
	break;
    default:
	break;
    }
    $.post("/filter/", dict_values, function(response){
	var decoded = JSON.parse(response);
	var array = decoded.posts;
	$("#posts_div").empty();
	for(var i = 0; i < array.length; i++){
	    html = "<div class=\"col-lg-3 col-md-4 col-sm-6 col-xs-12\">" +
		"<div class=\"thumbnail no-margin-bottom\">" +
		"<img src=\'" + array[i].image + "\' class = \'img-responsive\'/>" +
		"<div class=\"caption\">" + 
		"<h3 id=\"thumbnail-label\">" + array[i].title + "<a class=\"anchorjs-link\" href=\"#thumbnail-label\"><span class=\"anchorjs-icon\"></span></a></h3>" + 
		" <p>" + array[i].description + "</p>" + 
		" <p> " +
                "<a href=\"" + array[i].slug + "\" class=\"btn btn-success\" role=\"button\">View Post</a>" + 
		"<br>" + 
		"</p>" + 
		"</div>" + 
		"</div>" + 
		"</div>";
	    $("#posts_div").append(html);
	}
    });
}

$(document).ready(function(){
    $("#maxprice").keyup(function(event){
	path = window.location.pathname;
	path = path.split("/");
	ask_for_posts(this.value, path[2], "maxprice");
        });
});
$(document).ready(function(){
    $("#minprice").keyup(function(event){
	path = window.location.pathname;
	path = path.split("/");
	ask_for_posts(this.value, path[2], "minprice");
        });
    });


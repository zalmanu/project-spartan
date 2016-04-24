$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});
$("#expand_menu").click(function(){
    $(".ham_menu").toggleClass('show_menu');
});
$(document).ready(function(){
    $("#mytable #checkall").click(function () {
        if ($("#mytable #checkall").is(':checked')) {
            $("#mytable input[type=checkbox]").each(function () {
                $(this).prop("checked", true);
            });
	    
        } else {
            $("#mytable input[type=checkbox]").each(function () {
                $(this).prop("checked", false);
            });
        }
    });
    
    $("[data-toggle=tooltip]").tooltip();
});
$("#show_other_bids").click(function(){
    $(".each_bid").toggleClass('show_bids');
});


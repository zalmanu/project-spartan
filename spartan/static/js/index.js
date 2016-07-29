$('#show-reviews').click(function(){
  $('.review-card').slideToggle();
});

$('#edit-profile-btn').click(function(){
  $('#card-edit-profile').slideToggle();
});

var faqList = $('#faq-list');
var faqElements = faqList.children().length;
faqList.children().find('span').hide();
var arrow = faqList.children().find('i');

for(var i = 0; i <= faqElements; i++){
	arrow.addClass("glyphicon glyphicon-play faq-icon");
}
$('.faq-froup').on('click', function(){
	$(this).find('span').toggle();
});

	$('#us2-address').change(function(){
		$('#location-input').val($(this).val());
	});



var post_description = $('.description-text').text().length;

$(document).ready(function(){
    $(".description-text").each(function() {
         if($(this).text().length > 40) {
           $(this).text($(this).text().substr(0, 40)+"...");
         }
     });
});

var_post_title = $('.post-title').text().length;

$(document).ready(function(){
    $(".post-title").each(function() {
         if($(this).text().length > 20) {
           $(this).text($(this).text().substr(0, 20)+"...");
         }
     });
});


$('#special').hide();


$('#fineas').click(function(){
  $('#special').show();
})

$('#password-message').hide();
$('#password-input').show();

$('#display-message').click(function(){
  $('#password-message').show();
  $("#password-input").hide();
});

$('#create-post-tooltip').tooltip('autostart : false').show();


















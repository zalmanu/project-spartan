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



var post_description = $('.description').text().length;

console.log(post_description);

$(document).ready(function(){

     $(".description").each(function() {
         if($(this).text().length > 270) {
           $(this).text($(this).text().substr(0, 270)+"...");
         }
     });
});































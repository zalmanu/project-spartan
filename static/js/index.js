$('#chat').hide();

$('.open-chat-box').click(function(){
  $('#chat').fadeIn();
});

$('#close-chat-box').click(function(){
  $('#chat').hide();
});

$('#show-reviews').click(function(){
  $('.review-card').slideToggle();
});

$('#edit-profile-btn').click(function(){
  $('#card-edit-profile').slideToggle();
});

$('#cancel_button').click(function(){
$('#card-edit-profile').slideToggle();
});

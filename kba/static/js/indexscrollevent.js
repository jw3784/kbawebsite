// click 'about us' scroll event
$('#about-btn').on('click', ClickAbout)
var AboutLocation = $('#ab').position().top - 105;

function ClickAbout() {
    $('html, body').animate({
        scrollTop: AboutLocation
    }, 1000);
}
// navbar shadow event
function scrollHandler() {
	console.log($(window).scrollTop());
	console.log($('#ab').position().top);

	if ($(window).scrollTop() >= $('#ab').position().top-101) {
		$('.navbar').css('border-bottom', '1px solid #9DA4AA');
	} else {
		$('.navbar').css('box-shadow', 'none');
	}
}
$(window).on('scroll', scrollHandler);

scrollHandler();

$(document).ready(function() {
 
  $("#ab-owl").owlCarousel({
 
      navigation : true, // Show next and prev buttons
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem:true
 
      // "singleItem:true" is a shortcut for:
      // items : 1, 
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false
 
  });
 
});
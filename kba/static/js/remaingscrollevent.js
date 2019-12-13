// scroll event
// alumni.html showcase scroll
function scrollHandler() {
	console.log($(window).scrollTop());
	console.log($('#bc').position().top);

	if ($(window).scrollTop() >= $('#bc').position().top) {
		$('.navbar').css('border-bottom', '1px solid #9DA4AA');
	} else {
		$('.navbar').css('box-shadow', 'none');
	}
}
$(window).on('scroll', scrollHandler);
// 
scrollHandler();
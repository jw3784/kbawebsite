// fade event
// index.html carousel fade event
$(window).on('scroll', function(){
	$('#carouselExampleIndicators').css('opacity', 1 - $(window).scrollTop() / $('#carouselExampleIndicators').height());
})
// alumni.html showcase fade event
$(window).on('scroll', function(){
	$('#showcase-alumni-top').css('opacity', 1 - $(window).scrollTop() / $('#showcase-alumni-top').height());
})
// events.html showcase fade event
$(window).on('scroll', function(){
	$('#showcase-events-top').css('opacity', 1 - $(window).scrollTop() / $('#showcase-events-top').height());
})
// boardmembers.html showcase fade event
$(window).on('scroll', function(){
	$('#showcase-board-top').css('opacity', 1 - $(window).scrollTop() / $('#showcase-board-top').height());
})
// about.html showcase fade event
$(window).on('scroll', function(){
	$('#showcase-about-top').css('opacity', 1 - $(window).scrollTop() / $('#showcase-about-top').height());
})
// guidebook.html showcase fade event
$(window).on('scroll', function(){
	$('#showcase-gb-top').css('opacity', 1 - $(window).scrollTop() / $('#showcase-gb-top').height());
})

$('#owl-demo').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:2
        },
        1000:{
            items:3
        }
    }
})
$(document).ready(function() {
 
    $('#ab-owl').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        items: 1,
        responsive:{
            0:{
                items:1,
                nav:true,
                loop:true
            },
            600:{
                items:1,
                nav:false,
                loop:true
            },
            1000:{
                items:1,
                nav:true,
                loop:true
            }
        }
    }); 
});
$(document).ready(function() {
  
  var owl = $("#owl-demo");
 
  owl.owlCarousel({
     
      navigation : true,

  navigationText: ["◀ Left <strong>arrow</strong>","Right <strong>arrow</strong> ▶"]
  });
});

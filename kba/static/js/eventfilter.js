// event filtering function
$(document).ready(function(){

    $('.filter-btn').click(function(){
        var value = $(this).attr('data-filter');
        
        if(value == "all")
        {
            //$('.filter').removeClass('hidden');
            $('.card-main').show('1000');
        }
        else
        {
//            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
//            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $('.card-main').not('.'+value).hide('3000');
            $('.card-main').filter('.'+value).show('3000');
            
        }
    });
});


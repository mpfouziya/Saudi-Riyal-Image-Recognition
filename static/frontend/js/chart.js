const bar=document.querySelector('.bars li .bar');

function chartgrow(){
    (bar).each(function(key,bar){
        var percentage=$(this).data('percentage');
        $(this).animate({
            'height' : percentage + '%'
        },1000);
    });
    }

chartgrow();
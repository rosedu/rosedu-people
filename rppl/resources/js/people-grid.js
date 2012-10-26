$('.person').hover(
        function()
        {
            $(this).find('.avatar-container-big').css({opacity: 0.0, visibility: 'visible'}).animate({opacity: 1.0, width: '180px', height: '180px'}, 500);
        },
        function()
        {
            $(this).find('.avatar-container-big').css({opacity: 0.0, visibility: 'hidden'}).animate({opacity: 0, width: '60px', height: '60px'}, 100);
        });



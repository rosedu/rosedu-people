$('.person').hover(
        function()
        {
            $(this).find('.avatar-container-big').css('visibility', 'visible');
        },
        function()
        {
            $(this).find('.avatar-container-big').css('visibility', 'hidden');
        });



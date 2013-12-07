$( document ).ready( function(){
    
$(".grid li").hover(function(){
    if($(this).find("div").hasClass("visible"))
    {
        $(this).find("div").removeClass("visible").addClass("hidden");
    }
    else
    {
        $(this).find("div").removeClass("hidden").addClass("visible");
    }
     
}); });

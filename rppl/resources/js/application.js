$(document).ready(function() {
	$('#auth-form').css('left',$('#auth-button').offset().left-35+'px');
	$('#auth-form').css('top',$('#auth-button').offset().top+32+'px');

	var authForm=0;

	$(window).resize(function() {
		$('#auth-form').css('left',$('#auth-button').offset().left-35+'px');
		$('#auth-form').css('top',$('#auth-button').offset().top+32+'px');
	});

	$('#auth-button').click(function() {
		if(authForm) {
			$('#auth-form').fadeOut('fast');
			authForm=0;
		} else {
			$('#auth-form').fadeIn('fast');
			authForm=1;
		}
	});

	$('input').focus(function() {
		if(this.value==this.defaultValue)
			this.value='';
		$(this).css('color','#323232');
	});

	$('input').blur(function() {
		if($.trim(this.value)=='')
			this.value=(this.defaultValue?this.defaultValue:'');
		$(this).css('color','');
	});
});
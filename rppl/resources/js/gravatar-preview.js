var gravatarPreview = function() {
    var gravatar = document.querySelector('.gravatar-preview');
    var email = document.querySelector('#id_email').value;
    gravatar.src = 'http://www.gravatar.com/avatar/' + md5(email)
}

setInterval(gravatarPreview, 30)

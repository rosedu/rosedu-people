from django.http import HttpResponse

def same_user_from_request_required(function):
    """ Decorates a view to authorize a user only if the view is called
    with pk equal to logged in user id
    """
    def wrapper(request, *args, **kwargs):
        if int(request.user.id) == int(kwargs['pk']):
            return function(request, *args, **kwargs)
        else:
            return HttpResponse("Your Jedi tricks don't work on me",
                                status=403)

    return wrapper

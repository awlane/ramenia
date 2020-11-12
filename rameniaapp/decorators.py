from django.core.exceptions import PermissionDenied
#Thanks https://simpleisbetterthancomplex.com/2015/12/07/working-with-django-view-decorators.html
def user_is_moderator(function):
    def wrap(request, *args, **kwargs):
        if request.user.groups.filter(name="moderator").exists():
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

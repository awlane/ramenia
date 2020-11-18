#if request.user.groups.filter(name="moderator").exists()
from django.core.exceptions import PermissionDenied
#Thanks https://stackoverflow.com/a/54592371/9627903
class UserIsModeratorMixin(object):
    '''Class-based view mixin to block non-moderator users from their pages/actions'''
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name="moderator").exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
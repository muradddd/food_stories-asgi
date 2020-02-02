from django.core.exceptions import PermissionDenied


class ProfileEditMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object():
            raise PermissionDenied
        return super(ProfileEditMixin, self).dispatch(request, *args, **kwargs)
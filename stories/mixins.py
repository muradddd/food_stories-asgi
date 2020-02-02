from django.core.exceptions import PermissionDenied


class StoryEditMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object().user:
            raise PermissionDenied
        return super(StoryEditMixin, self).dispatch(request, *args, **kwargs)
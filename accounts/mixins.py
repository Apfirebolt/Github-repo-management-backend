from django.http import HttpResponseForbidden


class AuthorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.object.author != self.request.user:
            return HttpResponseForbidden()
        return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)
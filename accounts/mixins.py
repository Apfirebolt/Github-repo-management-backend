from django.http import HttpResponseForbidden


class AuthorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.object.author != self.request.user:
            return HttpResponseForbidden()
        return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)


class ContextDataMixin():
    """ A Simple Mixin example, applied when some methods are required in multiple CBV """
    def __init__(self):
        print('Mixin started..')

    def get_object(self):
        obj = super(ContextDataMixin, self).get_object()
        print('The selected Object is : ', obj)
        return obj

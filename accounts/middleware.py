from django.utils.timezone import now
from accounts.models import CustomUser


class SetLastVisitMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        if request.user.is_authenticated:
            CustomUser.objects.filter(pk=request.user.id).update(last_login=now())
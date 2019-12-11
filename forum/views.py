from django.shortcuts import render
from django.views.generic import CreateView, FormView, UpdateView, DetailView, ListView
from forum.models import ForumThread, ThreadComment
from forum.forms import ThreadForm
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.shortcuts import reverse


def forum_home(request):
    return render(request, 'forum/forum_test.html', {})


class CreateThread(FormView):
    form_class = ThreadForm
    template_name = 'forum/create_thread.html'
    success_url = 'home'

    def form_valid(self, form):
        forum_obj = form.save(commit=False)
        forum_obj.owner = self.request.user
        forum_obj.slug = slugify(forum_obj.title)

        forum_obj.save()
        return HttpResponseRedirect(reverse('blog:list'))

    def form_invalid(self, form):
        print('Some errors occurred..')
        return HttpResponse('Some errors on the page')


class ThreadList(ListView):
    model = ForumThread
    template_name = 'forum/list_thread.html'

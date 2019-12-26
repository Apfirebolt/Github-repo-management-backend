from django.shortcuts import render
from django.views.generic import CreateView, FormView, UpdateView, DetailView, ListView
from forum.models import ForumThread, ThreadComment
from forum.forms import ThreadForm
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.shortcuts import reverse
from forum.utilities import handle_uploaded_file
from accounts.models import UserModel, UserFollowing, FriendRequests
from django.db.models import Q


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

        handle_uploaded_file(self.request.FILES['thread_video'])
        forum_obj.save()
        return HttpResponseRedirect(reverse('blog:list'))

    def form_invalid(self, form):
        print('Some errors occurred..')
        return HttpResponse('Some errors on the page')


class ThreadList(ListView):
    model = ForumThread
    template_name = 'forum/list_thread.html'


class ListForumUsers(ListView):
    model = UserModel
    template_name = 'forum/list_users.html'
    context_object_name = 'all_users'
    paginate_by = 20

    def get_follow_users(self):
        follow_qs = UserFollowing.objects.filter(user_id=self.request.user.id)
        return follow_qs

    def get_queryset_friend(self):
        friend_qs = FriendRequests.objects.filter(user_from_id=self.request.user.id)
        return friend_qs

    def get_queryset_friend_accepted(self):
        queryset = FriendRequests.objects.filter(Q(user_from_id=self.request.user.id) & Q(accepted=True))
        return queryset

    def get_queryset(self):
        queryset = UserModel.objects.exclude(username=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListForumUsers, self).get_context_data()
        context['all_follow'] = self.get_follow_users()
        context['all_friend'] = self.get_queryset_friend()
        context['all_accepted'] = self.get_queryset_friend_accepted()

        all_following_id = [data.following.id for data in list(context['all_follow'])]
        all_friend_id = [data.user_to_id for data in list(context['all_friend'])]
        all_accepted_id = [data.user_to_id for data in list(context['all_accepted'])]

        context['all_following_id'] = all_following_id
        context['all_friend_id'] = all_friend_id
        context['all_accepted_id'] = all_accepted_id

        print('All accepted context is : ', context['all_accepted_id'])

        return context






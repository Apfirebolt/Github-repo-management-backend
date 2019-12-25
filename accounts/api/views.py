from rest_framework import generics
from rest_framework.views import APIView
from . serializers import UserSerializer, FollowSerializer, FriendSerializer
from accounts.models import UserModel, FriendRequests, UserFollowing
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.http import HttpResponseForbidden, Http404
from . permission import IsUserAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsUserAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_fields = ('username', 'about_me', 'first_name',)

    def get_queryset_user(self):
        queryset = UserModel.objects.exclude(username=self.request.user)
        search_user = self.request.query_params.get('username')
        search_email = self.request.query_params.get('email')

        if search_user:
            queryset = queryset.filter(username__icontains=search_user)
        elif search_email:
            queryset = queryset.filter(email__icontains=search_email)
        elif search_user and search_email:
            queryset = queryset.filter(Q(username__icontains=search_user) & Q(email__icontains=search_email))

        return queryset

    def get_queryset_follow(self):
        queryset = UserFollowing.objects.filter(user_id=self.request.user.id)
        return queryset

    def get_queryset_friend(self):
        queryset = FriendRequests.objects.filter(Q(user_from_id=self.request.user.id) & Q(accepted=False))
        return queryset

    def get_queryset_friend_accepted(self):
        queryset = FriendRequests.objects.filter(Q(user_from_id=self.request.user.id) & Q(accepted=True))
        return queryset

    def list(self, request, *args, **kwargs):
        user_data = UserSerializer(self.get_queryset_user(), many=True)
        follow_data = self.get_queryset_follow()
        friend_data = self.get_queryset_friend()
        friend_accepted = self.get_queryset_friend_accepted()

        follow_data_array = [each_data.following_id for each_data in list(follow_data)]
        friend_data_array = [each_data.user_to_id for each_data in list(friend_data)]
        friend_accepted = [each_data.user_to_id for each_data in list(friend_accepted)]

        print('Friend data array is : ', friend_accepted)
        print('Friend not accepted array is : ', friend_data_array)

        return Response({
          'user_data': user_data.data,
          'follow_data_array': follow_data_array,
          'friend_data_array': friend_data_array,
          'friend_accepted_array': friend_accepted
        })


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def perform_update(self, serializer):
        serializer.validated_data['password'] = make_password(serializer.validated_data.get('password'))
        serializer.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class FriendRequestView(generics.CreateAPIView):
    serializer_class = FriendSerializer
    permission_classes = [IsUserAuthenticated]
    authentication_classes = [SessionAuthentication]


class FriendRequestListView(generics.ListAPIView):
    serializer_class = FriendSerializer
    permission_classes = [IsUserAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        qs = FriendRequests.objects.all()
        return qs


class UpdateFriendRequest(APIView):
    serializer_class = FriendSerializer
    permission_classes = [IsUserAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_object(self, request, friend_id):
        try:
            current_user = self.request.user.id
            return FriendRequests.objects.get(Q(user_from_id=current_user) & Q(user_to_id=friend_id))

        except FriendRequests.DoesNotExist:
            raise Http404

    def put(self, request, friend_id):
        friend = self.get_object(request, friend_id)

        serializer = FriendSerializer(friend, data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, friend_id):
        current_obj = self.get_object(request, friend_id)
        content = {'message': 'You have cancelled friend request from this user!'}

        try:
            current_obj.delete()
        except ObjectDoesNotExist:
            print('The object does not exists')

        return Response(content, status=status.HTTP_204_NO_CONTENT)


class UserFollowView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsUserAuthenticated]


class UserUnfollowView(APIView):

    serializer_class = FollowSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsUserAuthenticated]

    def delete(self, request, follow_id):
        current_user = self.request.user.id
        content = {'message': 'You have successfully unfollowed this user!'}

        try:
            obj = UserFollowing.objects.get(Q(user_id=current_user) & Q(following_id=follow_id))
            obj.delete()
        except ObjectDoesNotExist:
            print('The object does not exists')

        return Response(content, status=status.HTTP_204_NO_CONTENT)


class CancelFriendView(APIView):
    serializer_class = FollowSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsUserAuthenticated]

    def delete(self, request, friend_id):
        current_user = self.request.user
        content = {'message': 'You have successfully cancelled friend request to this user!'}

        try:
            obj = FriendRequests.objects.get(Q(user_to_id=friend_id) & Q(user_from_id=current_user))
            obj.delete()
        except ObjectDoesNotExist:
            print('The object does not exists', friend_id, current_user)

        return Response(content, status=status.HTTP_204_NO_CONTENT)


class UserFollowListView(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        qs = UserFollowing.objects.all()
        return qs
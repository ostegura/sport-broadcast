from django.contrib.auth.models import User

from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import viewsets, views, generics
from rest_framework.reverse import reverse

from .models import (BroadcastType, Broadcast, Event, Comment)

from .serializers import (BroadcastTypeSerializer, BroadcastSerializer,
                          EventSerializer, CommentSerializer, UserSerializer)

from .permissions import IsOwnerOrReadOnly


class BroadcastTypeViewSet(viewsets.ModelViewSet):
    queryset = BroadcastType.objects.all()
    serializer_class = BroadcastTypeSerializer
    permission_classes = (permissions.IsAdminUser,)


class BroadcastViewSet(viewsets.ModelViewSet):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer
    permission_classes = (permissions.IsAdminUser,)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny, )


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAdminUser,
                          IsOwnerOrReadOnly, )  # moderator?


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'comments': reverse('comment-list', request=request, format=format),
#     })

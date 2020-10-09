from django.contrib.auth.models import User

from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import viewsets, views, generics
from rest_framework.reverse import reverse
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.views import ObtainAuthToken

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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class LoginView(ViewSet):
#     serializer_class = AuthTokenSerializer

#     def create(request):
#         return ObtainAuthToken().post(request)


# class LogoutView(APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
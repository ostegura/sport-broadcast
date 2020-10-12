from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'date', 'broadcast_type__name']
    search_fields = ['title', 'date', 'broadcast_type__name']
    ordering_fields = ['title', 'date', 'broadcast_type__name']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['creation_date', 'broadcast__title']
    search_fields = ['creation_date', 'broadcast__title']
    ordering_fields = ['creation_date', 'broadcast__title']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['creation_date', 'owner', 'broadcast__title']
    search_fields = ['creation_date', 'owner', 'broadcast__title']
    ordering_fields = ['creation_date', 'owner', 'broadcast__title']

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [
                permissions.IsAuthenticated, permissions.IsAdminUser]
        elif self.action == 'list':
            permission_classes = [
                permissions.IsAuthenticated, permissions.IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [
                permissions.IsAuthenticated, permissions.IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

# class LoginView(ViewSet):
#     serializer_class = AuthTokenSerializer

#     def create(request):
#         return ObtainAuthToken().post(request)


# class LogoutView(APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

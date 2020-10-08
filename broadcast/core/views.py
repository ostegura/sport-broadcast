from django.http import Http404

from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import viewsets, views, generics

from .models import (BroadcastType, Broadcast, Event, Comment)

from .serializers import (BroadcastTypeSerializer, BroadcastSerializer,
                          EventSerializer, CommentSerializer)

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


# TODO get, post, patch, put for comments
class CommentListView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)

    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(views.APIView):
    # queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated,
                          permissions.IsAdminUser)

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAdminUser,
                          IsOwnerOrReadOnly,)  # moderator?

    def get_queryset(self):
        queryset = Comment.objects.filter(id=self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_default() == True:
            return Response("Cannot delete default system category",
                            status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)

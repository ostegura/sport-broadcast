from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (
    BroadcastType, Broadcast,
    Event, Comment
)


class BroadcastTypeSerializer(serializers.HyperlinkedModelSerializer):

    # provides user to see 'children' broadcasts
    types = serializers.HyperlinkedRelatedField(
        many=True, view_name="broadcast-detail", read_only=True
    )

    class Meta:
        model = BroadcastType
        fields = "__all__"


class BroadcastSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        many=True, view_name="event-detail", read_only=True
    )

    broadcast_comments = serializers.HyperlinkedRelatedField(
        many=True, view_name="comment-detail", read_only=True
    )

    class Meta:
        model = Broadcast
        fields = "__all__"


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_comments = serializers.HyperlinkedRelatedField(
        many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'user_comments')

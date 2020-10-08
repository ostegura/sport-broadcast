from rest_framework import serializers

from .models import (
    BroadcastType, Broadcast,
    Event, Comment
)


class BroadcastTypeSerializer(serializers.HyperlinkedModelSerializer):
    # provides user to see 'children' comments
    broadcast = serializers.HyperlinkedRelatedField(
        many=True, view_name="broadcast-detail", read_only=True
    )

    class Meta:
        model = BroadcastType
        fields = "__all__"


class BroadcastSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        many=True, view_name="event-detail", read_only=True
    )

    comment = serializers.HyperlinkedRelatedField(
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

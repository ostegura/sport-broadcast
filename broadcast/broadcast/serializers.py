from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'is_staff', 'comments']

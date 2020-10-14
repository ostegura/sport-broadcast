from django.urls import path, include

from rest_framework import routers

from core.views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'broadcastTypes', BroadcastTypeViewSet)
router.register(r'broadcasts', BroadcastViewSet)
router.register(r'events', EventViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

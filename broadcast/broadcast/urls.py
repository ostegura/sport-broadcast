from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework_simplejwt import views as jwt_views

from core.views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'broadcastTypes', BroadcastTypeViewSet)
router.register(r'broadcasts', BroadcastViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),

    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/',
         CommentDetailView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/delete',
         CommentDeleteView.as_view(), name='comment-delete'),

    path("api-auth/",
         include("rest_framework.urls", namespace='rest_framework')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
    #      name='token_refresh'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

from rest_framework import routers
# from rest_framework_simplejwt import views as jwt_views

from broadcast.views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


app_name = "broadcast"
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('core/', include('core.urls')),
    path("api-auth/",
         include("rest_framework.urls", namespace='rest_framework')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
    #      name='token_refresh'),
]

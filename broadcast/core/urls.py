from django.urls import path
from .views import (CommentDeleteView, CommentListView,
                    CommentDetailView)

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('comments/', CommentListView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
    path('comments/<int:pk>/delete',
         CommentDeleteView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

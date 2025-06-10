from django.urls import path
from .views import CommentAPIView, PostCommentView

urlpatterns = [
    path('comments', CommentAPIView.as_view()),
    path('posts/<str:pk>/comments', PostCommentView.as_view())
]
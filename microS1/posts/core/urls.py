from .views import PostAPI
from django.urls import path
urlpatterns = [
    path('posts', PostAPI.as_view(), name='post_api'),
]

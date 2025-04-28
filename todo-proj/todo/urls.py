from django.urls import path
from . import views
from .views import updateTask, deleteTask

urlpatterns = [
    path('', views.index, name='list'),
    path('update/<str:pk>/', updateTask, name='updateTask'),
    path('delete/<str:pk>/', deleteTask, name='deleteTask')
]
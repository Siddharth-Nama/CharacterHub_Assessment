from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
]

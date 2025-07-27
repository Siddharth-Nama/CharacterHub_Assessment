# TODO There's certainly more than one way to do this task, so take your pick.

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer

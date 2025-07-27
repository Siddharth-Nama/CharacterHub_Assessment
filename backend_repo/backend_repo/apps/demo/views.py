# TODO There's certainly more than one way to do this task, so take your pick.

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-timestamp')

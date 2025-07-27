# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
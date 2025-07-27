from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class PostListViewTests(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpass')

        Post.objects.create(text="This is the first post", user=self.user)
        Post.objects.create(text="This is the second post", user=self.user)

    def test_post_list_view(self):
            url = reverse('post-list')
            response = self.client.get(url)

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            texts = [post['text'] for post in response.data]
            self.assertIn("This is the first post", texts)
            self.assertIn("This is the second post", texts)

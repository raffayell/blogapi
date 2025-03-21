from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="testuser",
            email="testuser@email.com",
            password="secret"
        )
        cls.post = Post.objects.create(
            title="Test title",
            body="Test body",
            author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Test title")
        self.assertEqual(self.post.body, "Test body")
        self.assertEqual(str(self.post), "Test title")


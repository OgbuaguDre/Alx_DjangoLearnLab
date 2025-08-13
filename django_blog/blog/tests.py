from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass')
        self.other = User.objects.create_user(username='bob', password='pass')
        self.post = Post.objects.create(title='Hello', content='World', author=self.user)

    def test_list_view(self):
        resp = self.client.get(reverse('blog:post_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.post.title)

    def test_create_requires_login(self):
        resp = self.client.get(reverse('blog:post_create'))
        self.assertEqual(resp.status_code, 302)  # redirect to login

        self.client.login(username='alice', password='pass')
        resp = self.client.post(reverse('blog:post_create'), {'title':'New','content':'x'})
        self.assertEqual(Post.objects.filter(title='New').count(), 1)

    def test_only_author_can_edit_or_delete(self):
        self.client.login(username='bob', password='pass')
        resp = self.client.get(reverse('blog:post_update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 403)  # or 302 depending on mixin settings

        resp = self.client.post(reverse('blog:post_update', kwargs={'pk': self.post.pk}), {'title':'H','content':'C'})
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Hello')

# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()

        # Log in user (if endpoints require authentication)
        self.client.login(username='testuser', password='testpass123')

        # Create sample books
        self.book1 = Book.objects.create(title='The Alchemist', author='Paulo Coelho', publication_year=1988)
        self.book2 = Book.objects.create(title='Things Fall Apart', author='Chinua Achebe', publication_year=1958)

        # Endpoint URLs
        self.list_url = reverse('book-list')  # name from urls.py for List/Create
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])  # name for Retrieve/Update/Delete

    # ---------- CRUD TESTS ----------

    def test_create_book(self):
        data = {
            'title': 'Half of a Yellow Sun',
            'author': 'Chimamanda Ngozi Adichie',
            'publication_year': 2006
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'Half of a Yellow Sun')

    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # two books in setUp

    def test_update_book(self):
        data = {'title': 'The Alchemist Updated', 'author': 'Paulo Coelho', 'publication_year': 1988}
        response = self.client.put(self.detail_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Alchemist Updated')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # ---------- FILTERING, SEARCH, ORDERING ----------

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_url}?author=Chinua Achebe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Chinua Achebe')

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.list_url}?search=alchemist")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Alchemist')

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Alchemist')  # newest first

    # ---------- PERMISSIONS TESTS ----------

    def test_unauthenticated_user_cannot_create_book(self):
        client = APIClient()  # fresh client without login
        data = {'title': 'No Auth Book', 'author': 'Unknown', 'publication_year': 2024}
        response = client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

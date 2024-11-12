from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('book_list')  # Use the name of your URL pattern

        # Sample data for testing
        self.book_data = {
            "id": 10,
            "title": "Secret",
            "author": "Sud kua",
            "price": "142.00"
        }

    def test_create_book(self):
        """Test that a new book can be created"""
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
        self.assertEqual(response.data['author'], self.book_data['author'])
        self.assertEqual(response.data['price'], self.book_data['price'])

    def test_get_books(self):
        """Test that all books can be retrieved"""
        # First, create a book
        self.client.post(self.url, self.book_data, format='json')

        # Retrieve books
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # At least one book should be present

    def test_invalid_book_data(self):
        """Test that invalid data returns a 400 Bad Request"""
        invalid_book_data = {
            "id": 11,
            "title": "",  # Empty title should cause a failure
            "author": "Some Author",
            "price": "100.00"
        }
        response = self.client.post(self.url, invalid_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


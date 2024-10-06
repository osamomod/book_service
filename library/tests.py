from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from library.models import Author


class AuthorAPITests(APITestCase):
    def test_create_author(self):
        url = reverse("create_author")
        data = {"name": "Test Author"}
        response = self.client.post(url, data, format="json")

        # Проверяем, что статус-код 302 (перенаправление)
        self.assertEqual(response.status_code, 302)

        # Проверяем, что произошло перенаправление на правильный URL
        redirect_url = reverse("add_author_and_book")
        self.assertRedirects(response, redirect_url)

    def test_get_author(self):
        author = Author.objects.create(name="Test Author")
        url = reverse("author-detail", args=[author.author_id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Author")

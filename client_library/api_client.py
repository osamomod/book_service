import requests


class BookServiceClient:
    BASE_URL = "http://127.0.0.1:8000/api/"

    def __init__(self):
        pass

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            response.raise_for_status()

    def get_authors(self):
        response = requests.get(f"{self.BASE_URL}authors/")
        return self._handle_response(response)

    def get_author(self, author_id):
        response = requests.get(f"{self.BASE_URL}authors/{author_id}/")
        return self._handle_response(response)

    def create_author(self, name):
        response = requests.post(
            f"{self.BASE_URL}authors/",
            json={"name": name},
            headers={"Content-Type": "application/json"},
        )
        if response.status_code == 201:  # Успешное создание
            return response.json()  # Возвращаем данные нового автора
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def get_books(self):
        response = requests.get(f"{self.BASE_URL}books/")
        return self._handle_response(response)

    def create_book(self, title, authors):
        response = requests.post(
            f"{self.BASE_URL}books/",
            json={"title": title, "authors": authors},
            headers={"Content-Type": "application/json"},
        )
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

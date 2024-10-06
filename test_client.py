from client_library.api_client import BookServiceClient

if __name__ == "__main__":
    client = BookServiceClient()

    try:
        # Получение списка авторов
        authors = client.get_authors()
        print("Authors list:", authors)

        # Добавляем нового автора
        # new_author = client.create_author("AuthorLibrary")
        # print("Added author:", new_author)

        # Получение списка книг
        # books = client.get_books()
        # print("Books list:", books)

    except Exception as e:
        print("Error:", e)

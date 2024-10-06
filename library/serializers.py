import re
from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = ["book_id", "title", "authors"]

    def validate_title(self, value):
        # Проверяем, что название книги состоит только из латинских символов и пробелов
        if not re.match(r"^[a-zA-Z\s\d]+$", value):
            raise serializers.ValidationError(
                "The book title can only contain English letters and spaces."
            )
        # Обрезаем пробелы в начале и конце и проверяем
        if not value.strip():
            raise serializers.ValidationError(
                "The book title cannot be empty or consist only of spaces."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Включаем книги

    class Meta:
        model = Author
        fields = ["author_id", "name", "books"]

    def validate_name(self, value):
        # Проверяем, что имя автора состоит только из латинских символов и пробелов, без цифр
        if not re.match(r"^[a-zA-Z\s]+$", value):
            raise serializers.ValidationError(
                "The author's name can only contain English letters and spaces."
            )
        # Обрезаем пробелы в начале и конце и проверяем
        if not value.strip():
            raise serializers.ValidationError(
                "The author's name cannot be empty or consist only of spaces."
            )
        return value

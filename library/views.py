from django.shortcuts import render, redirect
from .models import Author, Book
from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from .filters import AuthorFilter
from django.db.models import Q
from django.contrib import messages


def list_authors(request):
    authors = Author.objects.prefetch_related("books").all()
    author_filter = AuthorFilter(request.GET, queryset=authors)  # Применяем фильтр
    return render(
        request,
        "list_authors.html",
        {"authors": author_filter.qs, "filter": author_filter},
    )


def list_books(request):
    search_query = request.GET.get("q", "")  # Приводим к нижнему регистру
    books = Book.objects.prefetch_related("authors").all()

    if search_query:
        books = books.filter(title__icontains=search_query)  # Приводим и в фильтре

    return render(request, "list_books.html", {"books": books})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Включаем книги для каждого автора
        for author in queryset:
            author.books_list = author.books.all()
        return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["delete"])
    def delete_all(self, request):
        self.queryset.all().delete()
        return Response({"status": "Все авторы были удалены"})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["delete"])
    def delete_all(self, request):
        self.queryset.all().delete()
        return Response({"status": "Все книги были удалены"})


@csrf_exempt
@api_view(["POST"])
def create_author(request):
    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        authors = Author.objects.all()  # Получаем список авторов
        if serializer.is_valid():
            serializer.save()
            # Добавляем уведомление об успехе
            return render(
                request,
                "add_author_and_book.html",
                {"success_message": "Author successfully added!", "authors": authors},
            )
        return render(
            request,
            "add_author_and_book.html",
            {"errors": serializer.errors, "authors": authors},
        )


@csrf_exempt
@api_view(["POST"])
def create_book(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        authors = Author.objects.all()  # Получаем список авторов
        if serializer.is_valid():
            serializer.save()
            # Добавляем уведомление об успехе
            return render(
                request,
                "add_author_and_book.html",
                {"success_message": "Book successfully added!", "authors": authors},
            )
        return render(
            request,
            "add_author_and_book.html",
            {"errors": serializer.errors, "authors": authors},
        )


def add_author_and_book(request):
    authors = Author.objects.all()
    return render(request, "add_author_and_book.html", {"authors": authors})

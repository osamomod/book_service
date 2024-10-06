"""
URL configuration for book_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from library import views
from rest_framework.routers import DefaultRouter
from library.views import (
    AuthorViewSet,
    BookViewSet,
    create_author,
    create_book,
    add_author_and_book,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Book Service API",
        default_version="v1",
        description="API для работы с книгами и авторами",
        contact=openapi.Contact(email="osamo@tut.by"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.add_author_and_book, name="add_author_and_book"),
    path("authors/", views.list_authors, name="list_authors"),  # Список авторов
    path("books/", views.list_books, name="list_books"),  # Список книг
    path("create-author/", create_author, name="create_author"),  # Создание автора
    path("create-book/", create_book, name="create_book"),  # Создание книги
    path("api/", include(router.urls)),  # API для авторов и книг
]

urlpatterns += [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

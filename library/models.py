from django.db import models
import uuid


class Author(models.Model):
    author_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255, unique=True)
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title

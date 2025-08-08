from django.db import models

# Create your models here
# Author model - represents a book author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

# Book model - represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )  # One author -> Many books

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

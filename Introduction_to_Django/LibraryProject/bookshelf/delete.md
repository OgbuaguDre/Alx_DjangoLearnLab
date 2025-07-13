```python
from bookshelf.models import Book

# Retrieve the book before deleting
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>

from django import forms
from django import forms
from .models import Book

# ExampleForm for testing CSRF protection and safe input handling
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

# Optional: A model form for Book if needed elsewhere
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

# Optional: A search form for safe querying
class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search books', max_length=100)

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

from django import forms
from .models import Post
from .models import Comment
from taggit.managers import TaggableManager

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }

    def save(self, commit=True, author=None):
        post = super().save(commit=False)
        if author:
            post.author = author
        if commit:
            post.save()
        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class Post(models.Model):
    ...
    tags = TaggableManager()

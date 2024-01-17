from django import forms
from .models import Book
from .models import Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pdf', 'cover', 'description']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
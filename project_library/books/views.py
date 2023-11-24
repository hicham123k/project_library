

from django.shortcuts import render
from .models import Book
from .forms import BookForm

def book_list(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'form': form, 'books': books})


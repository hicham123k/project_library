
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Book, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect


@login_required
def book_list(request):
    books = Book.objects.all()
    comments = {book.id: Comment.objects.filter(book=book) for book in books}
    forms = {book.id: CommentForm(request.POST or None) for book in books}
   
    if request.method == 'POST':
        book_id = int(request.POST.get('book_id'))
        form = forms[book_id]
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.book_id = book_id
            comment.save()
            return redirect('books:book_list')

    return render(request, 'books/book_list.html', {'books': books, 'comments': comments, 'forms': forms})


# def like_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.likes += 1
#     comment.save()
#     return redirect('comment_detail', pk=comment.pk)





# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .models import Book, Comment
# from .forms import CommentForm
# from django.shortcuts import get_object_or_404

# @login_required
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books': books})






# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.book = book
#             comment.user = request.user
#             comment.save()
#     else:
#         form = CommentForm()
#     return render(request, 'book_list.html', {'book': book, 'form': form})



# def book_list(request):
#     comment_form = CommentForm()
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books': books, 'comment_form': comment_form})



# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     comments = Comment.objects.filter(book=book)
#     form = CommentForm()

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.book = book
#             comment.save()
#             form = CommentForm()

#     return render(request, 'books/book_list.html', {'book': book, 'comments': comments, 'form': form})


# # views.py
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, get_object_or_404
# from .models import Book, Comment
# from .forms import CommentForm

# @login_required
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books/book_list.html', {'books': books})

# @login_required
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     comments = Comment.objects.filter(book=book)
#     form = CommentForm()

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.book = book
#             comment.user = request.user
#             comment.save()
#             form = CommentForm()

#     return render(request, 'books/book_detail.html', {'book': book, 'comments': comments, 'form': form})

# # views.py
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .models import Book, Comment
# from .forms import CommentForm

# @login_required
# def book_list(request):
#     books = Book.objects.all()
#     comments = {book.id: Comment.objects.filter(book=book) for book in books}
#     form = CommentForm()

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.save()
#             form = CommentForm()

#     return render(request, 'books/book_list.html', {'books': books, 'comments': comments, 'form': form})

from django.shortcuts import render
from books.models import Book
from django.views.generic import TemplateView


# def home(request):
#     books = Book.objects.all()
#     return render(request, 'home.html', {'books': books})

# class HomeView(TemplateView):
#     template_name = 'pages/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = Book.objects.all()
#         return context
    



class HomeWithBooksView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context
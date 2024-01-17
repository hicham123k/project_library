from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    # path('comment/<int:pk>/like/', views.like_comment, name='like_comment'),
]
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'books'

class Comment(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     book = models.ForeignKey(Book, on_delete=models.CASCADE)
     text = models.TextField()
     created_date = models.DateTimeField(auto_now_add=True)
#     likes = models.IntegerField(default=0)
     
     




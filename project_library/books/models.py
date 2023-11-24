from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'books'



        
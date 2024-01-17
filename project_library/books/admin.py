from django.contrib import admin
from .models import Book
from .models import Comment

admin.site.register(Book)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'book', 'created_date')
    search_fields = ('user__username', 'text', 'book__title')
admin.site.register(Comment, CommentAdmin)
# from django.contrib import admin
# from .models import Book
# from .models import Comment

# admin.site.register(Book)




# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'text', 'book', 'created_at')
#     search_fields = ('user__username', 'text', 'book__title')

# admin.site.register(Comment, CommentAdmin)


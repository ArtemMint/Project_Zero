from django.contrib import admin
from .models import Blog, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1 

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    list_display = ('author', 'title')
    list_filter = ['published_date']
    search_fields = ['title']


admin.site.register(Blog, BlogAdmin)
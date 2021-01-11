from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Blog, Comment


admin.site.unregister(Group)

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0 

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]
    list_display = ('author', 'title','text','published_date')
    list_filter = ['published_date']
    search_fields = ['title']


admin.site.register(Blog, BlogAdmin)
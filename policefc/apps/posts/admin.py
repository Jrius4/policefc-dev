from django.contrib import admin
from .models import Author, Category, Post, Comment, PostView
from .tinymcemodel import PostTiny
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostTiny)
admin.site.register(Comment)
admin.site.register(PostView)

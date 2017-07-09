from django.contrib import admin
from .models import Genre, Article
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Genre)
admin.site.register(Article, MarkdownxModelAdmin)

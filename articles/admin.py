from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Comment)

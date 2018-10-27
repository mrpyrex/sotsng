from django.contrib import admin
from .models import ArticleCat, Article


class ArticleCatAdmin(admin.ModelAdmin):
    list_display            = ('cat_name', 'cat_slug')
    prepopulated_fields     = {'cat_slug': ('cat_name',)}

admin.site.register(ArticleCat, ArticleCatAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display            = ('article_title', 'article_slug')
    prepopulated_fields     = {'article_slug': ('article_title',)}

admin.site.register(Article, ArticleAdmin)
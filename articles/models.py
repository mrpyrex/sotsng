from django.db import models
import datetime

# Create your models here.
class ArticleCat(models.Model):
    cat_name            = models.CharField(max_length=250, unique=True)
    cat_slug            = models.SlugField()
    cat_description     = models.TextField()
    cat_thumb           = models.ImageField(default='default.png', blank=True, upload_to='articlescat/')

    class Meta:
        ordering                = ('cat_name',)
        verbose_name            = 'articlecat'
        verbose_name_plural     = 'articlecats'
    
    def __str__(self):
        return self.cat_name

class Article(models.Model):
    article_title      = models.CharField(max_length=250, unique=True)
    article_slug       = models.SlugField()
    article_body       = models.TextField()
    article_thumb      = models.ImageField(default='default.png', blank=True, null=True, upload_to='article/')
    article_cat        = models.ForeignKey(ArticleCat, on_delete=models.CASCADE)
    article_featured   = models.BooleanField(default=False)
    article_date       = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.article_title
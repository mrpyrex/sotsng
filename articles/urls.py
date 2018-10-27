from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.articlesView, name='articles'),
]


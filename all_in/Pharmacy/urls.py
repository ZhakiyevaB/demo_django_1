from django.urls import path, include, re_path
from post import views

urlpatterns = [
    path('index/', views.index),
    re_path('', views.news_home, name='news_home')
    re_path(r'^Medicine/', views.Medicine),
]


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.grammar_page, name='grammar_page'),
    path('check/', views.check, name='check'),
]

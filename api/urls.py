from django.urls import path, include
from . import views


urlpatterns = [
    path('grammar-api/', views.grammar, name='grammar_api'),
]

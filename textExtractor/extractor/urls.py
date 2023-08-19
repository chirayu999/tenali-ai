from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('extract/', views.extract_text, name='extract_text'),
]

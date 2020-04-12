# myapi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('answer/',views.answer, name='answer'),
    path('<str:question>/', views.detail, name='detail'),
]

# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'Chat', views.ChatViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('home/', views.home, name='home'),
    path('',views.index,name='index'),
    path('chat/', views.chat, name='chat'),
    path('answer/',views.answer, name='answer'),
    path('<str:question>/', views.detail, name='detail'),
]
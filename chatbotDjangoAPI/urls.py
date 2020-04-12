from django.contrib import admin
from django.conf.urls import url
urlpatterns = [
    url('admin/', admin.site.urls),
    url('bot/', include('botapi.urls')),
]

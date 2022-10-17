from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('add-project/', admin.site.urls, name='addproject'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

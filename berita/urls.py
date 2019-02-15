
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^berita/$', views.berita),
    url(r'^berita/(?P<judul>[\w-]+)/$', views.kategori, name='kategori'),
]

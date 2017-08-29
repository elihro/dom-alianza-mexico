from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
url(r'^estadisticas/$', views.estadisticas),
    url(r'^las-reglas/$', views.reglas),
]
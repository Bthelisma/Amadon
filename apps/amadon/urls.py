from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cover),
    url(r'^product$', views.index),
    url(r'^amadon/buy$', views.payment),
    url(r'^checkout$', views.checkout),
    url(r'^amadon/checkout$', views.checkout),
]

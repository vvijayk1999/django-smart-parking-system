from django.urls import path

from . import views

urlpatterns = [
    path('auth', views.login, name='auth'),
    path('sample_api', views.sample_api, name='sample_api')
]
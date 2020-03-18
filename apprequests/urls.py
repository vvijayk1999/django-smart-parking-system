from django.urls import path

from . import views

urlpatterns = [
    path('', views.checkSlots, name='checkslots'),
]
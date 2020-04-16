from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about', views.about, name='about'),
    path('slot-info', views.slotInfo, name='slot-info'),
    path('realtime-slot-info',views.realtimeSlotInfo, name='realtime-slot-info'),
    path('reserve', views.reserve, name='reserve')
]
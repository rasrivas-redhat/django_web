from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('addition_action', views.addition, name='')
]

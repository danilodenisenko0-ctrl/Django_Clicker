# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clicker, name='clicker'),
    path('buy/<int:upgrade_id>/', views.buy_upgrade, name='buy_upgrade'),
]
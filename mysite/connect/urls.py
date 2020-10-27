
from django.urls import path
from connect import views



urlpatterns = [
    path('', views.connect, name="connect")
]

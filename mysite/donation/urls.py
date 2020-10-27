from django.urls import path
from . import views

app_name = 'donation'

urlpatterns = [

    path('', views.donation, name="donation"),
    path('success', views.success, name="success")

]
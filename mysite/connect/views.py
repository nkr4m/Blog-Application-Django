from django.shortcuts import render, HttpResponse
from connect.models import Connect
from datetime import datetime
from django.contrib import messages



# Create your views here.

def connect(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        feed = Connect(name = name, email = email, phone = phone, desc = desc ,date = datetime.today())
        feed.save()
        messages.success(request, 'Submission Done Amigo!')


    return render(request, 'connect.html')
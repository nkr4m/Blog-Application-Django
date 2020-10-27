from django.shortcuts import render, HttpResponse
from feedback.models import Feedback
from datetime import datetime
from django.contrib import messages

def index(request):
    if(request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        feed = Feedback(name = name, email = email, phone = phone, desc = desc ,date = datetime.today())
        feed.save()
        messages.success(request, 'Submission Done Amigo!')

    return render(request, 'connect.html')
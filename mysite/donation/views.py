from django.shortcuts import render

# Create your views here.
import razorpay
from .models import Donation

from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from django.core.mail import send_mail

from django.template.loader import render_to_string


def donation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get('amount')) * 100
        email = request.POST.get("email")
        client = razorpay.Client(auth = ("#", "#"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1' })
        print(payment)
        donate = Donation(name = name , amount =amount , email=email, order_id = payment['id'])
        donate.save()

        return render(request, 'donation/index.html' ,{'payment':payment})
    return render(request, 'donation/index.html')



@csrf_exempt
def success(request):
    if request.method == "POST":
        a =  (request.POST)
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
    
        user = Donation.objects.filter(order_id = order_id).first()
        user.paid = True
        user.save()

        '''
        msg_plain = render_to_string('donation/email.txt')
        msg_html = render_to_string('donation/email.html')

        send_mail("Your donation has been recieved", msg_plain, settings.EMAIL_HOST_USER,
                    [user.email], html_message= msg_html
        )

        '''



    return render(request, 'donation/success.html')
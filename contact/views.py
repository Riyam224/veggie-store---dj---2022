import re
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Contact
from  django.core.mail import send_mail
from django.conf import settings


def contact(request):
    info = Contact.objects.first()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']


        send_mail(name , message , settings.EMAIL_HOST_USER , [email]  , fail_silently=False )

    return render(request , 'contact/contact-us.html' , {
        'info': info
    })
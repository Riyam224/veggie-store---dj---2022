
import imp
from tkinter import NE
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse , JsonResponse
from django.views.generic import ListView  , DetailView
from .models import Product , Team , Category , Newsletter
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


class ProductList(ListView):
    model = Product
    template_name = 'products/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.all()
        return context
    


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Product.objects.filter(category=self.get_object().category)[:2]
        return context
    

    # TODO  add email settings

def newsletter_subscribe(request):
    info = Newsletter.objects.all()
    if request.method == 'POST':
        email = request.POST.get('emailInput')
         
        send_mail(
             'hi there',
             'i really like your site',
             settings.EMAIL_HOST_USER,
             [email],
         )

        messages.info(request , 'You Subscribed successfully ... ')
        
    
    context = {
        'info': info
    }
  
   
    return render(request  , 'products/product.html' , context)

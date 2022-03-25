from django.shortcuts import render

# Create your views here.
from products.models import Team


def about(request):
    teams = Team.objects.all()
    return render(request , 'about/about.html', context = {'teams': teams})
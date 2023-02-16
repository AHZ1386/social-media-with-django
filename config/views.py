from django.shortcuts import render
from twitter.models import twitt

def home_page(request):
    context = {
        'twittes': twitt.objects.all()
    }
    return render(request, 'home.html', context)
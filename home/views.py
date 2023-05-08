from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_screen_view(request):
    
    return render(request, "home/home.html", {})

def test_function(request):
    request.navBar
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'Hello/index.html', {})

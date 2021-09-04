from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm

def index (request):
    form = ContactForm()
    
    return render (request, 'portfolio/index.html', {'form': form})

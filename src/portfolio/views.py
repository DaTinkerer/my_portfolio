from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .forms import ContactForm
import json
from django.core.mail import EmailMessage
from decouple import config
def index (request):
    form = ContactForm()
    
    return render (request, 'portfolio/index.html', {'form': form})

def send_message (request):
    if request.method == 'POST':
        data = json.loads(request.body)
        success = 'Message sent!'
        email = EmailMessage(
            subject=data['name'],
            body=data['msg'],
            to=[config('MY_EMAIL')],
            reply_to=[data['email']]
        )
        email.send(fail_silently=False)
        return JsonResponse({'success': success}, status=200)
    return render (request, 'portfolio/index.html')





    

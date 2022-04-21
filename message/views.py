from email import message
from django.shortcuts import render
from django.contrib import messages
from .models import Message
# Create your views here.
def submit_contact(request):
    if request.method == 'POST':
        save_form=Message(name=request.POST['name'], Email=request.POST['email'], subject=request.POST['subject'], message=request.POST['message'])
        save_form.save()
        messages.info(request, 'Your message has been sent! we will get back to you soon!')
        return render(request, 'contact_us.html')
    else:
        return render(request, 'contact.html')
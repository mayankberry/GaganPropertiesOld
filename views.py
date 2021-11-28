from django.shortcuts import render, HttpResponse
from gaganpr.models import contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def Contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      desc = request.POST.get('desc')
      Contact = contact(name = name, email = email, phone = phone, desc = desc)
      Contact.save()
    return render(request, 'contact.html')

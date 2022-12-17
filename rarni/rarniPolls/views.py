from django.http import HttpResponse
from django.http import Http404 
from django.template import loader
from django.shortcuts import render
from .forms import UserForm, EmailForm
from ipware import get_client_ip

    

def testpage(request):
    form = EmailForm() #creates a blank form based on the UserForm class in forms.py
    confirm = ""
    if request.method == 'POST':
        print(request.POST)
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save() #saves it to the database
            form = EmailForm() #clears the form
            confirm = "Thanks for registering!"
    context = {'form':form, 'confirm':confirm} 
    return render(request, 'rarni/index.html', context)

def rendform(request):
    form = UserForm() #creates a blank form based on the UserForm class in forms.py
    confirm = ""
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #saves it to the database
            form = UserForm() #clears the form
            confirm = "Thanks for registering!"
    context = {'form':form, 'confirm':confirm} 
    return render(request, 'rarni/form.html', context) #renders the page with the form

def getIP(request):
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        client_ip = "None"
    context = {'client_ip':client_ip}
    return render(request, 'rarni/ip.html', context)




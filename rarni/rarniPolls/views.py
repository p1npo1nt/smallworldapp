from django.http import HttpResponse
from django.http import Http404 
from django.template import loader
from django.shortcuts import render
from .forms import UserForm

def testpage(request):
    return render(request, 'rarni/index.html')

def rendform(request):
    form = UserForm() #creates a blank form based on the UserForm class in forms.py
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #saves it to the database
            form = UserForm() #clears the form
    context = {'form':form} 
    return render(request, 'rarni/form.html', context) #renders the page with the form

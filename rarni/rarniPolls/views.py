from django.http import HttpResponse
from django.http import Http404 
from django.template import loader
from django.shortcuts import render

def testpage(request):
    return render(request, 'rarni/index.html')

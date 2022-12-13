from django.http import HttpResponse
from django.http import Http404 
from django.template import loader
from django.shortcuts import render

from .models import Question, PpSize

#here we have 4 views: index, detail, results, and vote

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        
    } 
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("404: This question does not exist")
        return render(request, 'polls/detail.html', )
    return render(request, 'polls/detail.html', {'question': question})
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = HttpResponse("You're looking at the results of quesiton %s")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
#
#
#
#
def sizepage(request):
    latest_size_answers = PpSize.objects.all()
    context = {
        'latest_size_answers': latest_size_answers,
    }
    return render(request, 'sizenew/index.html', context)

def sizepage_detail(request, size_id):
    try:
        size = PpSize.objects.get(pk=size_id)

    except PpSize.DoesNotExist:
        raise Http404("404: This size does not exist")
        return render(request,'sizenew/detail.html')
    return render(request, 'sizenew/detail.html', {'size': size})
    return HttpReponse("You're looking at the results of size number %s." % size_id)







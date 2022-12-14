from django.shortcuts import render
from .forms import PlayerForm, StatsForm
from django.template import RequestContext
def playerindex(request):
    form = PlayerForm
    context = {'form': form}
    return render(request, 'footeh/index.html', context)

# Create your views here.

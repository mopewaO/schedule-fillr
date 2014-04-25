from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('homepage/index.html');

def schedule(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('homepage/schedule.html', context_dict, context);

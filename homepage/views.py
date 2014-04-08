from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # request context of the request (eg: client's machine details)
    context = RequestContext(request)

    # dict to pass to template engine as its context
    context_dict ={'boldmessage': "I am bold font from the context"}

    # return rendered response to send to client
    return render_to_response('homepage/index.html', context_dict, context);

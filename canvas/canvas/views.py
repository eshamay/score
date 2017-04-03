from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import datetime

def index(request):
    template = loader.get_template('canvas/index.html')
    context = {
        'some_list': ['a', 'list', 'of', 'strings'],
    }
    return HttpResponse(template.render(context, request))

def test(request):
    now = datetime.datetime.now()
    html = "<html><body>It is blow %s.</body></html>" % now
    return HttpResponse(html)

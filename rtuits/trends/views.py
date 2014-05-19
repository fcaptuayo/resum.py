from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from trends.models import Trend


def index(request):
    latest_poll_list = Trend.objects.all()
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'templates/index.html', context, context_instance=RequestContext(request))    

def detalle(request,ident):
    latest_poll_listw = Trend.objects.get(id=ident)
    contextw = {'latest_poll_list': latest_poll_listw}
    return render(request, 'templates/detail.html', {'dato':latest_poll_listw}, context_instance=RequestContext(request))


def information(request):
        return render(request, 'templates/proyecto.html',context_instance=RequestContext(request))    

def resumen(request,identrs):
    latest_poll_listw = Trend.objects.get(id=identrs)
    contextw = {'latest_poll_list': latest_poll_listw}
    return render(request, 'templates/result.html', {'dato':latest_poll_listw}, context_instance=RequestContext(request))

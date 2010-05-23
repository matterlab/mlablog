from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from mlablog.blog.models import *
from django.template import Template


def home(request):
    List=Post.objects.all()#order_by('-pubdate')
    return render_to_response('homepage.html',{'post_list':List})

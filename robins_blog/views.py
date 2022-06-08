from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def Index(request):
    return HttpResponseRedirect(reverse('blog:blog_list'))

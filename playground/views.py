import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import PlayGround

# Create your views here.
def say_hello(request):
    plays = PlayGround.objects.all()
    return render(request, 'playground/index_list.html', {'playgrounds': plays})
    # return HttpResponse('Hello World')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse ("<em> My Second App </em>")

def index_template(request):
    my_dict = {"response":"Help Page index_template"}
    return render(request, "ProTwo/index.html", context=my_dict)

def static_files(request):
    return render(request, "ProTwo/static_img_display.html", {"caption":"Django Reinhardt:"})
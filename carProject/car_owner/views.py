from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "common/index.html")

def profile_create(request):
    return HttpResponse('Create page')


def profile_details(request):
    return HttpResponse('Details page')


def profile_edit(request):
    return HttpResponse('Edit page')


def profile_delete(request):
    return HttpResponse('Delete page')
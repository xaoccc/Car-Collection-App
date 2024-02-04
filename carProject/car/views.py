from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def car_catalogue(request):
    return HttpResponse('car_catalogue page')

def car_create(request):
    return HttpResponse('Create page')


def car_details(request, pk):
    return HttpResponse('Details page')


def car_edit(request, pk):
    return HttpResponse('Edit page')


def car_delete(request, pk):
    return HttpResponse('Delete page')
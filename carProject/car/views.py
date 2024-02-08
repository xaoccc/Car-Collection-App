from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from carProject.car.models import Car


# Create your views here.
def car_catalogue(request):
    all_cars = Car.objects.all()

    context = {
        'all_cars': all_cars
    }

    return render(request, 'car/car-collection.html', context)

class CarCreateView(CreateView):
    model = Car
    template_name = 'car/car-add.html'
    fields = '__all__'

def car_details(request, pk):
    return HttpResponse('Details page')


def car_edit(request, pk):
    return HttpResponse('Edit page')


def car_delete(request, pk):
    return HttpResponse('Delete page')
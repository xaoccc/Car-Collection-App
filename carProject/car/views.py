from django.http import HttpResponse
from django.shortcuts import render, redirect

from carProject.car.forms import CarCreateForm
from carProject.car.models import Car


# Create your views here.
def car_catalogue(request):
    all_cars = Car.objects.all()

    context = {
        'all_cars': all_cars
    }

    return render(request, 'car/car-collection.html', context)

def car_create(request):
    car_create_form = CarCreateForm(request.POST or None)
    if request.method == "POST":
        if car_create_form.is_valid():
            car_create_form.save()
            return redirect('index')
    context = {
        'car_create_form': car_create_form
    }
    return render(request, 'car/car-add.html', context)


def car_details(request, pk):
    return HttpResponse('Details page')


def car_edit(request, pk):
    return HttpResponse('Edit page')


def car_delete(request, pk):
    return HttpResponse('Delete page')
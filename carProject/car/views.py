from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from carProject.car.models import Car


class CarListView(ListView):
    model = Car
    template_name = 'car/car-collection.html'
    context_object_name = 'all_cars'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car/car-add.html'
    fields = '__all__'

class CarEditView(UpdateView):
    model = Car
    template_name = 'car/car-edit.html'
    fields = '__all__'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    fields = '__all__'
    success_url = reverse_lazy('car-catalogue')


class CarTemplateView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    context_object_name = 'car'

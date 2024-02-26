from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, UpdateView, DeleteView, CreateView
from carProject.car.models import Car
from carProject.car_owner.models import Profile
from carProject.car.forms import CarCreateForm, CarDeleteForm


class GetProfileMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

class CarListView(GetProfileMixin, ListView):
    model = Car
    template_name = 'car/car-collection.html'
    context_object_name = 'all_cars'


class CarCreateView(GetProfileMixin, CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-add.html'


class CarEditView(GetProfileMixin, UpdateView):
    model = Car
    template_name = 'car/car-edit.html'
    fields = '__all__'


class CarDeleteView(GetProfileMixin, DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('car-catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs


class CarDetailView(GetProfileMixin, DetailView):
    model = Car
    template_name = 'car/car-details.html'
    context_object_name = 'car'


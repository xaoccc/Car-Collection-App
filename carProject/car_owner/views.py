from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from carProject.car_owner.models import Profile
from carProject.car_owner.forms import ProfileCreateForm


# Create your views here.
def index(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, "common/index.html", context)

class ProfileCreateView(CreateView):
    form_class = ProfileCreateForm
    template_name = 'profile/profile-add.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'
    context_object_name = 'profile'


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'profile/profile-edit.html'
    fields = '__all__'


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

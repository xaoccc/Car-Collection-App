from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from carProject.car_owner.models import Profile


# Create your views here.
def index(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile
    }

    return render(request, "common/index.html", context)

def profile_create(request):
    return HttpResponse('Create page')
class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profile/profile-add.html'
    fields = ['username', 'email', 'age', 'password']
    success_url = reverse_lazy('index')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'
    context_object_name = 'profile'


def profile_details(request):
    return HttpResponse('Details page')


def profile_edit(request):
    return HttpResponse('Edit page')


def profile_delete(request):
    return HttpResponse('Delete page')
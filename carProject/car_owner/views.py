from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from carProject.car_owner.models import Profile


# Create your views here.
def index(request):
    return render(request, "common/index.html")

def profile_create(request):
    return HttpResponse('Create page')
class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profile/profile-add.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


def profile_details(request):
    return HttpResponse('Details page')


def profile_edit(request):
    return HttpResponse('Edit page')


def profile_delete(request):
    return HttpResponse('Delete page')
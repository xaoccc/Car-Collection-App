from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from carProject.car_owner.models import Profile
from carProject.car_owner.forms import ProfileCreateForm, ProfileEditForm


class IndexView(ListView):
    model = Profile
    template_name = 'common/index.html'
    context_object_name = 'profile'

class ProfileCreateView(CreateView):
    form_class = ProfileCreateForm
    template_name = 'profile/profile-add.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile-details.html'
    context_object_name = 'profile'


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/profile-edit.html'



class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

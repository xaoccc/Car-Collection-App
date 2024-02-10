from django.urls import path, include
from carProject.car_owner import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/',
        include([
            path('create/', views.ProfileCreateView.as_view(), name='profile-create'),
            path('<int:pk>/details/', views.ProfileDetailView.as_view(), name='profile-details'),
            path('<int:pk>/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
            path('<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
        ])
    ),
]
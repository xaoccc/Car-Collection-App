from django.urls import path, include
from carProject.car_owner import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/',
        include([
            path('create/', views.profile_create, name='profile-create'),
            path('details/', views.profile_details, name='profile-details'),
            path('edit/', views.profile_edit, name='profile-edit'),
            path('delete/', views.profile_delete, name='profile-delete'),
        ])
    ),
]
from django.urls import path, include
from carProject.car import views

urlpatterns = [
    path('',
        include([
            path('catalogue/', views.car_catalogue, name='car-catalogue'),
            path('create/', views.car_create, name='car-create'),
            path('<int:pk>/details/', views.car_details, name='car-details'),
            path('<int:pk>/edit/', views.car_edit, name='car-edit'),
            path('<int:pk>/delete/', views.car_delete, name='car-delete'),
        ])
    ),
]
from django.urls import path, include
from carProject.car import views

urlpatterns = [
    path('',
        include([
            path('catalogue/', views.CarListView.as_view(), name='car-catalogue'),
            path('create/', views.CarCreateView.as_view(), name='car-create'),
            path('<int:pk>/details/', views.CarTemplateView.as_view(), name='car-details'),
            path('<int:pk>/edit/', views.CarEditView.as_view(), name='car-edit'),
            path('<int:pk>/delete/', views.CarDeleteView.as_view(), name='car-delete'),
        ])
    ),
]
from django.urls import path, include
from carProject.car_owner import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/',
        include([
            path('create/', views.ProfileCreateView.as_view(), name='profile-create'),
            path('<int:pk>/details/', views.ProfileDetailView.as_view(), name='profile-details'),
            path('<int:pk>/edit/', views.profile_edit, name='profile-edit'),
            path('<int:pk>/delete/', views.profile_delete, name='profile-delete'),
        ])
    ),
]
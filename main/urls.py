from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('<int:pk>/profile_edit', views.ProfileUpdate.as_view(), name='profile_edit'),
]
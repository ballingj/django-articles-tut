from django.contrib import admin
from django.urls import path, include

from .views import HomeView, trips_list


urlpatterns = [
    path("", HomeView.as_view(), name='trip_home'),
    path("list/", trips_list, name='trip_list'),
]

from django.contrib import admin
from django.urls import path, include

from .views import HomeView, trips_list, TripCreateView, TripDetailView, NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView, TripUpdateView, TripDeleteView


urlpatterns = [
    path("", HomeView.as_view(), name='trip_home'),
    path("list/", trips_list, name='trip_list'),
    path("create/", TripCreateView.as_view(), name='trip_create'),
    path("<int:pk>/", TripDetailView.as_view(), name='trip_detail'),
    path("<int:pk>/update/", TripUpdateView.as_view(), name='trip_update'),
    path("<int:pk>/delete/", TripDeleteView.as_view(), name='trip_delete'),
    path("note/", NoteListView.as_view(), name='note_list'),
    path("note/<int:pk>/", NoteDetailView.as_view(), name='note_detail'),
    path("note/create/", NoteCreateView.as_view(), name='note_create'),
    path("note/<int:pk>/update/", NoteUpdateView.as_view(), name='note_update'),
    path("note/<int:pk>/delete/", NoteDeleteView.as_view(), name='note_delete'),
]


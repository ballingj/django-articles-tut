from django.urls import path
from .views import LinkPlantListView, LinkPlantCreateView, LinkPlantUpdateView, LinkPlantDeleteView, profile_view


urlpatterns = [
    path('', LinkPlantListView.as_view(), name="link_plant_list"),
    path('create/', LinkPlantCreateView.as_view(), name="link_plant_create"),
    path('<int:pk>/update/', LinkPlantUpdateView.as_view(), name="link_plant_update"),
    path('<int:pk>/delete/', LinkPlantDeleteView.as_view(), name="link_plant_delete"),
    path('<slug:profile_slug>/', profile_view, name="profile"),
]


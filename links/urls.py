from django.urls import path, include
from links.views import links_list, root_link, link_create


urlpatterns = [
    path('', links_list, name="links_list"),
    path('create/', link_create, name='link_create'),
    path('<str:link_slug>/', root_link, name='root_link'),
]



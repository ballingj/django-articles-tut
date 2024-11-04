from django.urls import path
from todo_app.views import todo_list, todo_completed, todo_delete, todo_create, todo_update


urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('completed/', todo_completed, name='todo_completed'),
    path('create/', todo_create, name='todo_create'),
    path('<int:pk>/update/', todo_update, name='todo_update'),
    path('<int:pk>/delete/', todo_delete, name='todo_delete'),
]
from django.urls import path
from .views import todo_list, todo_create, todo_update, todo_delete

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('<int:id>/update/', todo_update, name='todo_update'),
    path('<int:id>/delete/', todo_delete, name='todo_delete'),
]

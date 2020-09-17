from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo', views.TodoList.as_view(),
         name='todo_index'),
    path('todo/new', views.TodoCreate.as_view(),
         name='todo_create'),
    path('todo/<int:pk>/edit', views.TodoUpdate.as_view(),
         name='todo_edit'),
    path('todo/<int:pk>/delete', views.TodoDelete.as_view(),
         name='todo_delete'),
]

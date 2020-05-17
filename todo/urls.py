from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('airport', views.TodoList.as_view(),
         name='todo_index'),
    path('airport/new', views.TodoCreate.as_view(),
         name='todo_create'),
    path('airport/<int:pk>/edit', views.TodoUpdate.as_view(),
         name='todo_edit'),
    path('airport/<int:pk>/delete', views.TodoDelete.as_view(),
         name='todo_delete'),
]

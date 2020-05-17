from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Todo

FIELDS = ["done", "description"]


def index(request):
    return redirect(reverse_lazy('todo_index'))


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = FIELDS


class TodoList(ListView):
    queryset = Todo.objects.order_by("description")
    template_name = "todo/index.html"


class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "create_edit.html"
    success_url = reverse_lazy("todo_index")


class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'create_edit.html'
    success_url = reverse_lazy("todo_index")


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy("todo_index")

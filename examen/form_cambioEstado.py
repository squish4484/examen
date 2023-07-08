from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Task

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['status']
    template_name = 'task_update.html'
    success_url = reverse_lazy('task_list')
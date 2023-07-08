from django.urls import path
from .views import TaskUpdateView

urlpatterns = [
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
]
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendiente'),
        ('in_progress', 'En progreso'),
        ('completed', 'Completada'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title
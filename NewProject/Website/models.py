from django.db import models

class TaskModel(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
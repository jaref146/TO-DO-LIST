from django.db import models
from datetime import datetime
# Create your models here.

class Todo(models.Model):
    task_name = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    update_date_at = models.DateTimeField( blank=True, null=True)
    def __str__(self):
        return self.task_name

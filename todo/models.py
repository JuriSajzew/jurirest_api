import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
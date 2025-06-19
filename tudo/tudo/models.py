from django.db import models
from datetime import datetime

# Create your models here.

class tudo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    last_update = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
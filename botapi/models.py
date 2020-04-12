# models.py
from django.db import models

# Create your models here.

class Chat(models.Model):
    q = models.CharField(max_length=260)
    a = models.CharField(max_length=260)
    tag = models.CharField(max_length=80)
    def __str__(self):
        return self.q

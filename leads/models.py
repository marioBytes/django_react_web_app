from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120, unique=True)
    message = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.

class Tv_show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    start_date = models.DateField()
    desc = models.TextField(default="Boring")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"
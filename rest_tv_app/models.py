from django.db import models

# Create your models here.
class Tv_showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['date']) == 0:
            errors["start_date"] = "Program requires start date"
        if len(postData['title']) < 2:
            errors["title"] = "Program title be at least 2 characters"
        if len(postData['network']) <3:
            errors["network"] = "Network must be at least 3 characters"
        if len(postData['desc'])>0 and len(postData['desc'])<10:
            errors["desc"] = "Description must be at least 10 characters"


        return errors



class Tv_show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    start_date = models.DateField()
    desc = models.TextField(default="Boring")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Tv_showManager()
    def __str__(self):
        return f"{self.title}"


from django.db import models

# Create your models here.

from django.db import models

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.type}"

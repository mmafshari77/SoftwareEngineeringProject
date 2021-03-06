from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.email

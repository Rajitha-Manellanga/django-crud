from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

from django.db import models


# Create your models here.
class GeneratedPassword(models.Model):
    email = models.EmailField()
    websiteName = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.websiteName

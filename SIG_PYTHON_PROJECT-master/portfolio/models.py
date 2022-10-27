from django.db import models

# Create your models here.
class portfolio(models.Model):
    title = models.CharField(max_length=50, unique=True)
    body = models.TextField()
    url = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
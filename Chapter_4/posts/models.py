from django.db import models

# Create your models here.
class Posts(models.Model):
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=20)
    text = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.date.year}: {self.username}"
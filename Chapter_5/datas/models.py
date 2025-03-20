from django.db import models
from django.utils.text import slugify

# Create your models here.
class BlogPosts(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=150)
    image = models.ImageField(blank=True, default='qr.png')
    slug = models.SlugField(blank= True, unique=True)
    username = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.date.year}-{self.title}'
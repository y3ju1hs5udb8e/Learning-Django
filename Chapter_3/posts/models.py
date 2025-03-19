from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    slug = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.date.month}-{self.title}"

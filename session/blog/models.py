from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    author = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_created=True)
    introduce = models.TextField()

    def __str__(self):
        return self.title

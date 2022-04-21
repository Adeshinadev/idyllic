from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images', blank=True)
    category = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=200)
    Date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.Email}'

from django.db import models


# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField(default=10)
    optional_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Sub_categorie(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    stock = models.IntegerField(default=10)
    optional_description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f'{self.name}, {self.category.name}'


class Product(models.Model):
    sub_category = models.ForeignKey(Sub_categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name

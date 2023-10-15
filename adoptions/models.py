from django.db import models

class Pet(models.Model):
    PET_TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]

    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    vaccination=models.CharField(max_length=50)
    pet_type = models.CharField(max_length=3, choices=PET_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Rehomer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number= models.IntegerField()
    email=models.EmailField()
    password = models.CharField(max_length=100)
from django.db import models


class UserForm1(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)
    date = models.DateField()
    address = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return self.full_name


class UserForm2(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.full_name

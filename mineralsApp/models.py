from django.db import models

# Create your models here.


class Mineral(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=100)
    minerals = models.ManyToManyField(Mineral)

    def __str__(self):
        return self.name


class Researcher(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    patronymic = models.CharField(max_length=300)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.patronymic


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Territory(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=100)
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    minerals = models.ManyToManyField(Mineral)

    def __str__(self):
        return self.name


class Ore(models.Model):
    name = models.CharField(max_length=300)
    minerals = models.ManyToManyField(Mineral)

    def __str__(self):
        return self.name

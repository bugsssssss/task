from django.db import models


class Employee(models.Model):
    full_name = models.CharField(("full name"), max_length=50)  # required
    birthdate = models.DateField(
        ("date of birth"))  # required

    created = models.DateTimeField(
        ("created"),  auto_now_add=True)
    updated = models.DateTimeField(
        ("updated"),  auto_now=True)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.full_name


class Client(models.Model):
    full_name = models.CharField(("full name"), max_length=50)  # required
    birthdate = models.DateField(
        ("date of birth"))  # required

    created = models.DateTimeField(
        ("created"),  auto_now_add=True)
    updated = models.DateTimeField(
        ("updated"),  auto_now=True)

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.full_name

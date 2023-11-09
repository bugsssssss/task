from django.db import models


class Product(models.Model):
    name = models.CharField(("name"), max_length=100)  # required
    quantity = models.PositiveIntegerField(
        ("quantity available"), default=0)  # auto
    price = models.DecimalField(
        ("price"), max_digits=10, decimal_places=2)  # required

    created = models.DateTimeField(
        ("created"),  auto_now_add=True)
    updated = models.DateTimeField(
        ("updated"),  auto_now=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")
        ordering = ['-created']

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(
        "clients.Client", verbose_name=("client"), on_delete=models.PROTECT)  # required
    products = models.ManyToManyField(
        "main.Product", verbose_name=("product"))  # required
    employee = models.ForeignKey("clients.Employee", verbose_name=(
        "employee"), on_delete=models.PROTECT)  # required

    created = models.DateTimeField(
        ("created"),  auto_now_add=True)
    updated = models.DateTimeField(
        ("updated"),  auto_now=True)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return f'Order #{self.id}'

from django.db import models

from django.contrib.auth.models import User

# from user.models import WefUser

# Create your models here.
# class BatchLocation(models.Model):
#     name = models.CharField(max_length=50, null=False, blank=False)
#     # add more properties
#     def __str__(self) -> str:
#         return f"{self.name}"


# class Batch(models.Model):
#     id = models.CharField("Batch Number", primary_key=True, blank=False, null=False)
#     quantity = models.PositiveBigIntegerField(null=False)
#     batchlocation = models.ForeignKey(
#         BatchLocation, on_delete=models.CASCADE, null=False, blank=False
#     )
#     # add more properties

#     def __str__(self) -> str:
#         return f"{self.id}"


# class Mortality(models.Model):
#     pass


class Product(models.Model):
    CATEGORY = (
        ("Stationary", "Stationary"),
        ("Electronics", "Electronics"),
        ("Food", "Food"),
    )

    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.customer}-{self.name}"

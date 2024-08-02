from django.db import models

# Create your models here.
# inventory/models.py

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    warehouse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} - {self.warehouse}"

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)
    warehouse = models.CharField(max_length=255)

    def __str__(self):
        return f"Sale {self.id} - {self.product.name}"

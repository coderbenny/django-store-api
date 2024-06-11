from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Sale(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_id} bought {self.item_id}"
    

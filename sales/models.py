from django.db import models

class Customer(models.Model):
    lname=models.CharField(max_length=200,unique=True)
    fname=models.CharField(max_length=200)


    def __str__(self):
        return self.lname

class Order(models.Model):
    lname = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product=models.CharField(max_length=200)
    quantity = models.IntegerField

    def __str__(self):
        return self.product

class Price(models.Model):
    product = models.ForeignKey(Order, on_delete=models.PROTECT)
    total_price = models.IntegerField()
    Order_date = models.DateField()

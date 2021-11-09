from django.db import models
from django.db.models.aggregates import Max

# Create your models here.

def __str__(self):
    return self.productCode

class Product(models.Model):
    productCode = models.CharField(max_length=100)
    productName = models.CharField(max_length=100)
    sellingPrice = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.productCode

class SalesInvoice(models.Model):
    invoiceNumber = models.CharField(max_length=100)
    invoiceDate = models.CharField(max_length=100)
    customerName = models.CharField(max_length=100)
    totalAmount = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.invoiceNumber

  

class SalesInvoiceDetails(models.Model):
    saleInvoiceId = models.ForeignKey(SalesInvoice,on_delete=models.CASCADE)
    lineNumber = models.BigIntegerField()
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=20,decimal_places=2)
    unitPrice = models.DecimalField(max_digits=20,decimal_places=2)
    amount = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.saleInvoiceId
    


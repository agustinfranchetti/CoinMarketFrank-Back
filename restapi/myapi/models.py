from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    marketCap = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ammount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

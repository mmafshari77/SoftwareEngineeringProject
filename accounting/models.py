from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

# Assets = Liabilities + Owner's Equity
class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateField()
    assets = models.FloatField()
    liablities = models.FloatField()
    owner_equity = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.description



from django.db import models


class Transactions(models.Model):
    date = models.DateTimeField()
    transaction_type = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    
    
    
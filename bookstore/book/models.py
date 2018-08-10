from django.db import models
from account.models import User
# Create your models here.
class Book(models.Model):
    bkName = models.CharField(max_length=128, unique=True)
    authorName = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    pubversion = models.IntegerField()
    price = models.IntegerField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    sold = models.ManyToManyField(User)
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.bkName
    
    class Meta:
        ordering = ['-pubDateTime']
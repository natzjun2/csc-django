from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=200)
    price = models.FloatField()

    class Meta:
        db_table = 'tbl_product'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        db_table = 'tbl_user'


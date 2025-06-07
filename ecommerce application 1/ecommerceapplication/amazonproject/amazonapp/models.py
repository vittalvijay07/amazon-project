from django.db import models

# Create your models here.
class Amazon(models.Model):
    custid=models.IntegerField()
    custname=models.CharField(max_length=20)
    custaddr=models.CharField(max_length=20)
    custphnno=models.IntegerField()
    custphoto=models.ImageField()
    

    
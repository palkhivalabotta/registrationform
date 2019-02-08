from django.db import models

class employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
   # image=models.ImageField(upload_to=file)
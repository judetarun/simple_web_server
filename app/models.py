from django.db import models
class book(models.Model):
    title=models.CharField(max_length=30)
    year=models.DateField()
    author=models.CharField(max_length=20,default="no")
    
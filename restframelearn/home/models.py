from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    fathers_name = models.CharField(max_length=40)

class Category(models.Model):
    category_name = models.CharField(max_length=50)

class book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    #creating foriegn key 
    book_title = models.CharField(max_length=80)
    
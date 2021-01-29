from django.db import models
# ORM model
# Create your models here.

class BookInfo(models.Model): #book information
    #id inherit
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    #key constraint
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
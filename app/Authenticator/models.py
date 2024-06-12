from django.db import models


class Person(models.Model):
  uuid = models.IntegerField(auto_created=True, unique=True)
  name = models.CharField(max_length=20)
  email = models.CharField(max_length=30)
  annual_income = models.IntegerField()
  password = models.CharField(max_length=8)


class Session(models.Model):
  uuid = models.ForeignKey(Person, on_delete=models.CASCADE)
  sid = models.IntegerField()

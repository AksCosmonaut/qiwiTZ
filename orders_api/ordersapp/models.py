from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, null=False)
    price = models.IntegerField()


def __str__(self):
    return "{} - {} - {}".format(self.id, self.description, self.price)

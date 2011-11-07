from django.db import models

# Create your models here.
class Programmer(models.Model):
    name = models.TextField()


class Pair(models.Model):
    first = models.ForeignKey(Programmer, related_name='first')
    second = models.ForeignKey(Programmer, related_name='second')
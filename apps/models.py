from django.db.models import Model, ImageField
from django.db.models.fields import  CharField, DecimalField


# Create your models here.

class Project(Model):
    name = CharField(max_length=255)
    creator_name = CharField(max_length=255)
    salary = DecimalField(max_digits=12, decimal_places=2)
    images = ImageField(upload_to='products/')


from django.contrib.auth.models import User
from django.db.models import Model, ImageField, ForeignKey, CASCADE, DateField, TextChoices, TextField, FileField, \
    DurationField
from django.db.models.fields import  CharField, DecimalField


# Create your models here.

# class User(Model)
class Project(Model):
    name = CharField(max_length=255)
    creator_name = CharField(max_length=255)
    salary = DecimalField(max_digits=12, decimal_places=2)
    images = ImageField(upload_to='products/')
    user = ForeignKey(User, on_delete=CASCADE, related_name='projects', null=True, blank=True)


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(Model):
    name = CharField(max_length=255)
    title = CharField(max_length=255)
    price = DecimalField(max_digits=12, decimal_places=2)
    description = CharField(max_length=255)
    main_image = ImageField(upload_to='products/', null=True, blank=True)
    category = ForeignKey(Category, on_delete=CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Order(Model):
    class OrderType(TextChoices):
        CANCELED = 'canceled', 'Canceled'
        IN_PROGRESS = 'in progress', 'In progress'
        Delayed = 'delayed', 'Delayed'
        DELIVERED = 'delivered', 'Delivered'
    order = CharField(max_length=255)
    date_purchased = DateField(auto_now_add=True)
    total = DecimalField(max_digits=12, decimal_places=2)
    status = CharField(max_length=255, choices=OrderType, default=OrderType.IN_PROGRESS)


    user = ForeignKey(User, on_delete=CASCADE, related_name='orders')
    product = ForeignKey(Product, on_delete=CASCADE, related_name='orders')

    def __repr__(self):
        return self.order


class Film(Model):
    title = TextField()
    video = FileField(upload_to='film/video/')
    main_image = ImageField(upload_to='film/images/')
    duration = CharField(max_length=12)

    def __str__(self):
        return self.title


class Todo(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name




from django.db import models

# Create your models here.

category_items=(
    ("buff","buff"),
    ("chicken","chicken"),
    ("veg","veg")
)
class Form(models.Model):
    name = models.CharField(max_length=30)
    email = models. EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()

class Momo(models.Model):
    title=models.CharField(max_length=200)
    category=models.CharField(choices=category_items,max_length=200)
    image=models.ImageField(upload_to='images')
    price=models.DecimalField(max_digits=8,decimal_places=3)

    def __str__(self):
        return self.title
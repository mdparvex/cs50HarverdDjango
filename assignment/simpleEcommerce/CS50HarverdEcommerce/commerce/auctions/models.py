from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm
from django.db import models
from django.utils import timezone
from PIL import Image


class User(AbstractUser):
    pass


class Category(models.Model):
    Catagory_name = models.CharField(max_length=64)
  
    def __str__(self):
        return self.Catagory_name


class Product(models.Model):
    productname = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='products')
    catagory=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.productname

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Beet(models.Model):
    beetprice = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='beet_set')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.beetprice)


    
class beetForm(ModelForm):
    class Meta:
        model = Beet
        fields = ['beetprice', 'product', 'user']
    
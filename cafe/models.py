from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField('Menu', max_length=50, blank=False)
    price = models.IntegerField('Price', default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'image/', blank=True, null = True)

    def __str__(self):
        return self.name
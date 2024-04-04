from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField('Menu', max_length=50, blank=False)
    price = models.IntegerField('Price', default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s %s %s" %(self.name, self.price, self.description)
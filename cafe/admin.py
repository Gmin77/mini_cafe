from django.contrib import admin
from cafe.models import Menu
# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin) :
    list_display = ('id', 'name', 'price', 'description', 'image')

    readonly_fields = ('image',)


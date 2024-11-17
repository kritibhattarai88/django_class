from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Momo)
class MomoAdmin(admin.ModelAdmin):
    list_display=['id','title','category','image','price']
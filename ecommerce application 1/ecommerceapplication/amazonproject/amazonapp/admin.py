from django.contrib import admin
from amazonapp.models import Amazon
# Register your models here.
class Amazonadmin(admin.ModelAdmin):
    list_display=['custid','custname','custaddr','custphnno','custphoto']
admin.site.register(Amazon,Amazonadmin)
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','position','date_coming','cash','director','get_image','is_director')
    readonly_fields=('get_image',)

    def get_image(self,obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='60'")
    get_image.short_description="Изображение"

@admin.register(EmployeeTree)
class EmployeeTreeAdmin(admin.ModelAdmin):
    list_display=('name','position','date_coming','cash','parent','get_image','is_director')
    readonly_fields=('get_image',)

    def get_image(self,obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='60'")
    get_image.short_description="Изображение"

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display=('name','rank')
    


#admin.site.register(EmployeeTree)

# Register your models here.

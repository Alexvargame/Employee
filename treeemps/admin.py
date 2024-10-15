from django.contrib import admin

from .models import Subs, Emps

@admin.register(Subs)
class SubsAdmin(admin.ModelAdmin):
    list_display=('name','parent')



##@admin.register(Emps)
##class EmpsAdmin(admin.ModelAdmin):
##    list_display=('name','direct')
##

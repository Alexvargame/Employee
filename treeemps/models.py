from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from empls.models import Employee



    

    

class Subs(MPTTModel):
    name=models.CharField(max_length=50,choices=([(e.name,e.name) for e in Employee.objects.all()]))
    parent=TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                          related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by=['name']

class Emps(models.Model):
    
    name=models.CharField(max_length=50,choices=([(e.name,e.name) for e in Employee.objects.all()]))
    direct = TreeForeignKey(Subs, on_delete=models.PROTECT)#, choices=([(e.name,e.name) for e in Employee.objects.filter(is_director=True)]))
##    parent=TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
##                          related_name='directs')
    def __str__(self):
        return f"{self.direct}---{self.name}" 

##    class MPTTMeta:
##        order_insertion_by=['dir']

        
##class (models.Model):
##    name = models.CharField(max_length=50,choices=([(e.name,e.name) for e in Employee.objects.all()]))
  


        


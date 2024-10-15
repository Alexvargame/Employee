from django.db import models
from django.shortcuts import reverse
from datetime import date
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.




class Position(models.Model):
    name=models.CharField("Должность", max_length=30)
    rank=models.PositiveSmallIntegerField("Ранг", blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name="Должность"
        verbose_name_plural="Должности"
        ordering=["rank"]
    



class Employee(models.Model):

    name=models.CharField("ФИО", max_length=50)
    position=models.CharField("Должность", max_length=20,choices=([(pos.name,pos.name) for pos in Position.objects.all()]))
    date_coming=models.DateField("Дата приема", auto_now_add=True )
    cash=models.PositiveSmallIntegerField("Зарплата", default=0)
    #employee=TreeForeignKey('self',verbose_name="Начальник", on_delete=models.SET_NULL, blank=True, null=True,related_name='children',db_column='employee')
    director=models.ForeignKey('self',verbose_name="Начальник", on_delete=models.SET_NULL, blank=True, null=True)
    is_director=models.BooleanField("Есть подчиненные", default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
 

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('employee_detail_url', kwargs={'pk':self.id})
    def get_update_url(self):
        return reverse('employee_update_url', kwargs={'pk':self.id})
    def get_delete_url(self):
        return reverse('employee_delete_url', kwargs={'pk':self.id})
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    class Meta:

        
        verbose_name="Сотрудник"
        verbose_name_plural="Сотрудники"
        
class EmployeeTree(MPTTModel):

    name=models.CharField("ФИО", max_length=50)
    position=models.CharField("Должность", max_length=20,choices=([(pos.name,pos.name) for pos in Position.objects.all()]))
    date_coming=models.DateField("Дата приема", auto_now_add=True )
    cash=models.PositiveSmallIntegerField("Зарплата", default=0)
    parent=TreeForeignKey('self',verbose_name="Начальник", on_delete=models.SET_NULL, blank=True, null=True,related_name='children')
##    director=models.CharField("Начальник", max_length=50, blank=True, null=True,
##                              choices=([(pos.name,pos.name) for pos in Position.objects.all() if pos.name!='младший сотрудник']))
    is_director=models.BooleanField("Есть подчиненные", default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
  #  info = models.TextField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('employee_detail_tree_url', kwargs={'pk':self.id})
    def get_update_url(self):
        return reverse('employee_update_tree_url', kwargs={'pk':self.id})
    def get_delete_url(self):
        return reverse('employee_delete_tree_url', kwargs={'pk':self.id})
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:    
        verbose_name="Сотрудник"
        verbose_name_plural="Сотрудники_Tree"

        
class EmployeeSearch(models.Model):

    name=models.CharField("ФИО", max_length=50, blank=True, null=True)
    position=models.CharField("Должность", max_length=20,choices=([(pos.name,pos.name) for pos in Position.objects.all()]), blank=True, null=True)
    date_coming_b=models.DateField()
    date_coming_e=models.DateField()
    cash_min=models.PositiveSmallIntegerField("Зарплата от", default=0)
    cash_max=models.PositiveSmallIntegerField("Зарплата до", default=1000000)
  

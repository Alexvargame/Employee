from django import forms
from django.forms import fields, widgets

from .models import Employee, Position, EmployeeSearch, EmployeeTree

class SortForm(forms.Form):

    sort_fields=(('name','ФИО'),('position','должность'),('cash','размер зп'),('date_coming','Дата приема'))
    sort_choice=forms.ChoiceField(choices=sort_fields,widget=forms.Select(attrs={'class':'form-control', 'empty_value':True}))


class ReorganisationForm(forms.Form):
    emp_reo=forms.ChoiceField(choices=((emp.name, emp.name) for emp in Employee.objects.all()),widget=forms.Select(attrs={'class':'form-control', 'empty_value':True}))


class DirectorWidget(forms.MultiWidget):
    def __init__(self,n=10,alst=[],attrs=None):

        widgets=[forms.Select(choices=alst, attrs={'class':'form-control', 'empty_value':True, 'initial':''})]*n
        super().__init__(widgets, attrs)


    def decompress(self, value):
        
        return ''

##class ChangeDirectorForm(forms.ModelForm):
####    director=forms.ChoiceField(choices=Employee.objects.all(),widget=forms.Select(attrs={'class':'form-control', 'empty_value':True}))
####    def __init__(self,query,*args, **kwargs):
####        
####        super(ChangeDirectorForm, self).__init__(self,*args, **kwargs)
####        self.fields['director'].choices=Employee.objects.filter(position=query)
##    
##    
##    class Meta:
##        model=Employee
##        fields=['director']
##        widgets={'director':forms.Select(attrs={'class':'form-control'})}
##
##
##        def __init__(self,query=[(emp.name, emp.name) for emp in Employee.objects.all()],*args, **kwargs):
##        
##            super().__init__(self,*args, **kwargs)
##            self.fields['director'].choices=query
        
        
class ChangeDirectorForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields=['director']
        widgets={'director':DirectorWidget()}           
         
class ChangeDirectorFormTree(forms.ModelForm):

    class Meta:
        model=EmployeeTree
        fields=['parent']
        widgets={'parent':DirectorWidget()}     
   
class SearchForm(forms.ModelForm):


    
    class Meta:
        model=EmployeeSearch
        fields=['name','position','cash_min','cash_max','date_coming_e', 'date_coming_b']
        
        widgets={
          
            'name':forms.TextInput(attrs={'class':'form-control','empty_value':True}),
            'position':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'cash_min':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'cash_max':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'date_coming_b':forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}),
            'date_coming_e':forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}),
            }   



class EmployeeForm(forms.ModelForm):


    class Meta:
        model=Employee
        fields=['name','position','cash', 'director','image']
        
        widgets={
          
            'name':forms.TextInput(attrs={'class':'form-control','empty_value':True}),
            'position':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'cash':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'director':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control', 'empty_value':True})
           
            }   

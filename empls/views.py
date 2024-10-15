from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.forms import formset_factory

from .models import Position, Employee, EmployeeTree
from .forms import SortForm, SearchForm, EmployeeForm, ReorganisationForm, ChangeDirectorForm, ChangeDirectorFormTree
from .forms import DirectorWidget


from datetime import date, datetime


def main_menu(request):
    return render(request, 'empls/main.html')

def employee_list(request):

    positions=Position.objects.all()
    employees=Employee.objects.all()
   
    
    emp_dict={}        
    for a in employees:
        key, value=a.name, [e for e in employees if e.director ==a]
        emp_dict[key]=[e for e in employees if e.director ==a]
    
    
    return render(request, 'empls/employee_list.html', context={'employees':employees, 'positions':positions, 'emp_dict':emp_dict})#, 'form':form})


def employee_tree_list(request):


    return render(request, "empls/employee_tree_list.html", {'tree':EmployeeTree.objects.all()})
class EmployeeDetailView(View):
  
    def get(self, request, pk):
        employee=Employee.objects.get(id=pk)
        subordinate=Employee.objects.filter(director=employee)
        
        return render(request, 'empls/employee_detail.html', context={'employee':employee, 'subordinate':subordinate})

class EmployeeDetailViewTree(View):
  
    def get(self, request, pk):
        employee=EmployeeTree.objects.get(id=pk)
        subordinate=EmployeeTree.objects.filter(parent=employee)
        
        return render(request, 'empls/employee_detail_tree.html', context={'employee':employee, 'subordinate':subordinate})


class EmployeeSort(View):
    
    def get(self,request):
        if request.GET:
            
            form=SortForm(request.GET)

            employees=Employee.objects.order_by(request.GET['sort_choice'])

            return render(request, 'empls/employee_sort_list.html',context={'employees':employees, 'form':form})
        else:
            form=SortForm()
            employees=Employee.objects.all()
            return render(request, 'empls/employee_sort_list.html',context={'employees':employees, 'form':form})



class EmployeeReorganisation(View):

    def get (self, request, pk):

        subordinate_dict={}
        emp=Employee.objects.get(id=pk)
        query=[(emp.name, emp.name) for emp in Employee.objects.filter(position=emp.position)]
        subordinate=(Employee.objects.filter(director=pk))
        form=ChangeDirectorForm()
        for sub in Employee.objects.filter(director=pk):      
            key, value=sub, form['director'].as_widget(DirectorWidget(len(subordinate),query))
            subordinate_dict[key]=value       
        
        context={
            'form':form['director'].as_widget(DirectorWidget(len(subordinate),query)),
            'subordinate_dict':subordinate_dict,
            'emp':emp,
            #'s':subordinate_dict,
            #'s1':form['director'].as_widget(DirectorWidget(ln,query))
        }       
        return render(request, 'empls/reorganisation.html', context=context)
    def post(self, request, pk):
        emp=Employee.objects.get(id=pk)
        query=[(emp.name, emp.name) for emp in Employee.objects.filter(position=emp.position)]
        subordinate=Employee.objects.filter(director=pk)
        subordinate_dict={}
        emp=Employee.objects.get(id=pk)
        bound_form=ChangeDirectorForm(request.POST)
        res=[r for r in  bound_form['director'].value() if r!=None]
        for sub in Employee.objects.filter(director=pk):  
            key, value=sub, bound_form['director'].as_widget(DirectorWidget(len(subordinate),query))
            subordinate_dict[key]=value
        query=Employee.objects.filter(position=emp.position)
        
        #if bound_form.is_valid():
        for i in range(len(subordinate)):
            
            emp_key=Employee.objects.get(name=subordinate[i])
            dr=Employee.objects.get(name=res[i])
            emp_key.director=dr
            emp_key.save()

        return redirect(reverse('employee_list_url'))

class EmployeeReorganisationTree(View):

    def get (self, request, pk):

        subordinate_dict={}
        emp=EmployeeTree.objects.get(id=pk)
        query=[(emp.name, emp.name) for emp in EmployeeTree.objects.filter(position=emp.position)]
        subordinate=(EmployeeTree.objects.filter(parent=pk))
        form=ChangeDirectorFormTree()
        for sub in EmployeeTree.objects.filter(parent=pk):      
            key, value=sub, form['parent'].as_widget(DirectorWidget(len(subordinate),query))
            subordinate_dict[key]=value       
        
        context={
            'form':form['parent'].as_widget(DirectorWidget(len(subordinate),query)),
            'subordinate_dict':subordinate_dict,
            'emp':emp,
            #'s':subordinate_dict,
            #'s1':form['director'].as_widget(DirectorWidget(ln,query))
        }       
        return render(request, 'empls/reorganisation.html', context=context)
    def post(self, request, pk):
        emp=EmployeeTree.objects.get(id=pk)
        query=[(emp.name, emp.name) for emp in EmployeeTree.objects.filter(position=emp.position)]
        subordinate=EmployeeTree.objects.filter(parent=pk)
        subordinate_dict={}
        emp=EmployeeTree.objects.get(id=pk)
        bound_form=ChangeDirectorFormTree(request.POST)
        res=[r for r in  bound_form['parent'].value() if r!=None]
        for sub in EmployeeTree.objects.filter(parent=pk):  
            key, value=sub, bound_form['parent'].as_widget(DirectorWidget(len(subordinate),query))
            subordinate_dict[key]=value
        query=EmployeeTree.objects.filter(position=emp.position)
        
        #if bound_form.is_valid():
        for i in range(len(subordinate)):
            
            emp_key=EmployeeTree.objects.get(name=subordinate[i])
            dr=EmployeeTree.objects.get(name=res[i])
            emp_key.parent=dr
            emp_key.save()

        return redirect(reverse('employee_tree_list_url'))
 
##class EmployeeReorganisation(View):
##
##    def get (self, request, pk):
####        ChangeDirectorFormSet=formset_factory(ChangeDirectorForm, extra=len(Employee.objects.filter(director=pk)))
####        formset=ChangeDirectorFormSet()
##        subordinate_dict={}
##        emp=Employee.objects.get(id=pk)
####        for i in range(len(Employee.objects.filter(director=pk))):      
####            key, value=Employee.objects.filter(director=pk)[i], formset[i]
####            subordinate_dict[key]=value       
##        for sub in Employee.objects.filter(director=pk):      
##            key, value=sub, ChangeDirectorForm()
##            subordinate_dict[key]=value       
##        query=[(emp.name, emp.name) for emp in Employee.objects.filter(position=emp.position)]
##      
##        context={
##            'subordinate_dict':subordinate_dict,
##            'emp':emp,
##            's':subordinate_dict,
##        }       
##        return render(request, 'empls/reorganisation.html', context=context)
##    def post(self, request, pk):
####        ChangeDirectorFormSet=formset_factory(ChangeDirectorForm, extra=len(Employee.objects.filter(director=pk)))
####        formset=ChangeDirectorFormSet((request.POST))
##        emp=Employee.objects.get(id=pk)
##        subordinate_dict={}
##        emp=Employee.objects.get(id=pk)
####        for i in range(len(Employee.objects.filter(director=pk))):      
####            key, value=Employee.objects.filter(director=pk)[i], formset[i]
####            subordinate_dict[key]=value       
##        for sub in Employee.objects.filter(director=pk):
##            
##            key, value=sub, ChangeDirectorForm(request.POST, instance=sub)
##            subordinate_dict[key]=value
##        query=Employee.objects.filter(position=emp.position)
##        d=[]
##        for key, value in subordinate_dict.items():
##            if value.is_valid():
##
##                emp_key=Employee.objects.get(name=key)
##                d.append(emp_key)
##                d.append(emp_key.director)
##                emp_key.director.id=value['director'].value()
##                d.append(emp_key.director.id)
##                
##                emp_key=value.save()
##            
##            #else:
##        context={
##           # 'form':bound_form,
##            'subordinate_dict':subordinate_dict,
##            'emp':emp,
##            's': subordinate_dict,
##            's1':d
##            }
##        return render(request, 'empls/reorganisation.html', context=context)
        #return redirect(reverse('employee_list_url'))
        #bound_form=ChangeDirectorForm(request.POST)
        #bound_forms=[ChangeDirectorForm(request.POST)]*len(subordinate)

##    `
##        if bound_form.is_valid():
##            for sub in subordinate:
##                #sub=bound_form.save()
            
            #return redirect(reverse('employee_list_url'))
##        else:
##            context={
##                'form':bound_form,
##                'subordinate':subordinate,
##                'emp':emp,
##                's':query
##                #(dirs,s,s1,bound_ch_form.fields['director'].choices),
##    ##            's1':(bound_ch_form, bound_ch_form['director'], dir(bound_ch_form))
##                }
##            return render(request, 'empls/reorganisation.html', context=context)
            
##      s1=ChangeDirectorForm().fields['director'].choices
##        emp_reo=Employee.objects.get(name=bound_form['emp_reo'].value())
##        dirs=[(emp.name,emp.name) for emp in  Employee.objects.filter(position=emp_reo.position)]
##        s=ChangeDirectorForm(dirs).fields['director'].choices
##       
####        ChangeDirectorForm().fields['director'].choices.queryset=Employee.objects.filter(position=emp_reo.position)
##        bound_ch_form=ChangeDirectorForm(dirs)
##        #bound_ch_form.fields['director'].choices.queryset=Employee.objects.filter(position=emp_reo.position)
##        
##        subordinate=Employee.objects.filter(director=emp_reo.id)
##        context={
##            'form':bound_form,
##            'ch_form':bound_ch_form,
##            'emp_reo':emp_reo.position,
##            'subordinate':subordinate,
##            's':(dirs,s,s1,bound_ch_form.fields['director'].choices),
##            's1':(bound_ch_form, bound_ch_form['director'], dir(bound_ch_form))
##            }
##        return render(request, 'empls/reorganisation.html', context=context)
##            
        


class EmployeeSearch(View):
    initials={'date_coming_b':date(2022,1,1),'date_coming_e': date.today()}
    def get(self,request):

        pos_query=[]
       
        if request.GET:
                        
            bound_form=SearchForm(request.GET, initial=self.initials)
            date_b=[int(i) for i in request.GET['date_coming_b'].split('-')]
            date_e=[int(i) for i in request.GET['date_coming_e'].split('-')]
            if bound_form['position'].value():
                pos_query.append(bound_form['position'].value())
            else:
                for pos in Position.objects.all():
                    pos_query.append(pos.name)
                
            employees=Employee.objects.filter(name__icontains=request.GET['name'],position__in=pos_query,
                                              cash__range=(request.GET['cash_min'],request.GET['cash_max']),
                                              date_coming__range=(date(date_b[0],date_b[1],date_b[2]),date(date_e[0],date_e[1],date_e[2]))
                                              )

            return render(request, 'empls/employee_search_list.html',context={'employees':employees, 's':(request.GET['date_coming_b'],self.initials)})
        else:
            form=SearchForm(initial=self.initials)
            employees=Employee.objects.all()
            return render(request, 'empls/employee_search.html',context={'employees':employees, 'form':form,'s':self.initials})

class EmployeeCreate(View):
    def get(self,request):
        form=EmployeeForm()
        return render(request,'empls/employee_create.html',context={'form':form})
    def post(self,request):
        bound_form=EmployeeForm(request.POST)
        if bound_form.is_valid():
            new_emp=bound_form.save()
            return redirect(new_emp)
        return render(request,'empls/employee_create.html',context={'form':bound_form})

        
class EmployeeUpdate(View):
    def get(self,request, pk):
        emp=Employee.objects.get(id=pk)
        form=EmployeeForm(instance=emp)
        return render(request,'empls/employee_update.html',context={'form':form})
    def post(self,request,pk):
        emp=Employee.objects.get(id=pk)
        pos=Position.objects.get(name=emp.position)
        bound_form=EmployeeForm(request.POST,request.FILES,instance=emp)
        direct=Employee.objects.get(id=request.POST['director'])
        pos_dir_new=Position.objects.get(name=direct.position)
        pos_new=Position.objects.get(name=request.POST['position'])
        

        if bound_form.is_valid():
            
            
            if abs(pos_dir_new.rank-pos_new.rank)==1:
                new_emp=bound_form.save()
                return redirect(new_emp)
            
        return render(request,'empls/employee_update.html',context={'form':bound_form})

        

class EmployeeDelete(View):
    def get(self,request, pk):
        emp=Employee.objects.get(id=pk)
        return render(request,'empls/employee_delete.html',context={'emp':emp})
    def post(self,request,pk):
        emp=Employee.objects.get(id=pk)
        emp.delete()
        return redirect(reverse('employee_list_url'))

                








        
        
        

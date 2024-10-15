from django.urls import path
from .views import *

urlpatterns = [
 
    path('',main_menu, name='main_menu_url'),
    path('employees/',employee_list, name='employee_list_url'),
    path('employees_tree/',employee_tree_list, name='employee_tree_list_url'),
    path('employees/<int:pk>/',EmployeeDetailView.as_view(), name='employee_detail_url'),
    path('sort/',EmployeeSort.as_view(), name='employee_sort_list_url'),
    path('search/',EmployeeSearch.as_view(), name='employee_search_url'),
    path('create/',EmployeeCreate.as_view(), name='employee_create_url'),
    path('employees/<int:pk>/update/',EmployeeUpdate.as_view(), name='employee_update_url'),
    path('employees/<int:pk>/delete/',EmployeeDelete.as_view(), name='employee_delete_url'),
    path('employees/<int:pk>/reorganisation/',EmployeeReorganisation.as_view(), name='reorganisation_url'),
    path('',main_menu, name='main_menu_url'),
    path('employees/',employee_list, name='employee_list_url'),
    path('employees_tree/',employee_tree_list, name='employee_tree_list_url'),
    path('employees_tree/<int:pk>/',EmployeeDetailViewTree.as_view(), name='employee_detail_tree_url'),
##    path('sort/',EmployeeSort.as_view(), name='employee_sort_list_url'),
##    path('search/',EmployeeSearch.as_view(), name='employee_search_url'),
##    path('create/',EmployeeCreate.as_view(), name='employee_create_url'),
##    path('employees/<int:pk>/update/',EmployeeUpdate.as_view(), name='employee_update_url'),
##    path('employees/<int:pk>/delete/',EmployeeDelete.as_view(), name='employee_delete_url'),
    path('employees_tree/<int:pk>/reorganisation/',EmployeeReorganisationTree.as_view(), name='reorganisation_tree_url'),
    
]

from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Employee

class ListAllEmployee(ListView):
  template_name = 'employees/list_all_employees.html'
  paginate_by = 2
  ordering = 'first_name'
  model = Employee
  
class ListEmployeeByDepartment(ListView):
  template_name = 'employees/employees_by_department.html'
  
  def get_queryset(self):
    area = self.kwargs['department_name']
    employees_list = Employee.objects.filter(department__name = area)
    return employees_list
  
class EmployeeSkillsList(ListView):
  template_name = 'employees/employees_skills_list.html'
  context_object_name = 'skills'
  def get_queryset(self):
    employee_id = self.kwargs['employee_id']
    employee = Employee.objects.get(id=employee_id)
    return employee.skills.all()
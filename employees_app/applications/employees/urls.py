from django.urls import path
from . import views

urlpatterns = [
    path('list-employees/', views.ListAllEmployee.as_view()),
    path('employees-by-department/<department_name>/', views.ListEmployeeByDepartment.as_view()),
    path('employee-skills/<employee_id>/', views.EmployeeSkillsList.as_view()),
]
 
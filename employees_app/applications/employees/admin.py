from django.contrib import admin
from .models import Employee, Skill
# Register your models here.

admin.site.register(Skill)

class EmployeeAdmin(admin.ModelAdmin):
  list_display = (
    'first_name', 'last_name', 'department', 'career', 'full_name',
  )
  
  #
  def full_name(self, obj):
    return f'{obj.first_name} {obj.last_name}'
  #
  
  search_fields = ('first_name', 'last_name')
  list_filter = ('career',)
  filter_horizontal = ('skills',)
admin.site.register(Employee, EmployeeAdmin)

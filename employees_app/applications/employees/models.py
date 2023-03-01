from django.db import models
from applications.department.models import Department
# Create your models here.

class Skill(models.Model):
  skill = models.CharField('Habilidad', max_length=50)

  class Meta:
    verbose_name = 'Habilidad'
    verbose_name_plural = 'Habilidades'

  def __str__(self):
      return f'{str(self.id)} - {self.skill}'
  
class Employee(models.Model):
  CAREER_CHOICES = (
    ('0', 'Contador'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Otro')
  )
  first_name = models.CharField('Nombres', max_length=50)
  last_name = models.CharField('Apellidos', max_length=50)
  career = models.CharField('Profesión', max_length=1, choices=CAREER_CHOICES)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to='employee', blank=True, null=True)
  skills = models.ManyToManyField(Skill)
  
  class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    ordering = ['first_name']
    unique_together = ('first_name', 'last_name')
  
  def __str__(self):
      return f'{str(self.id)} - {self.first_name} {self.last_name}'
    
    

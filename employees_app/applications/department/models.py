from django.db import models

# Create your models here.
class Department(models.Model):
  name = models.CharField('Nombre', max_length=50)
  short_name = models.CharField('Nombre corto', max_length=20, blank=True)
  anulate = models.BooleanField('Anulado', default=False)

  class Meta:
    verbose_name = 'Departmento'
    verbose_name_plural = 'Departmentos'
    ordering = ['-name']
    unique_together = ('name', 'short_name')

  def __str__(self):
      return f'{str(self.id)} - {self.name} - {self.short_name}'
  
from django.db import models
from django.core.exceptions import ValidationError



class Department(models.Model):
    """Департамент"""
    name = models.CharField(max_length=255, unique=True)
    director = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='departments')

    def __str__(self):
        return self.name

    @property
    def total_salary(self):
        return self.employees.aggregate(models.Sum('salary'))['salary__sum']

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Employee(models.Model):
    """Сотрудник"""
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, db_index=True)
    patronymic = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='avatars', null=True, blank=True)
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees', blank=True, null=True)

    class Meta:
        unique_together = ('id', 'department')
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.firstname

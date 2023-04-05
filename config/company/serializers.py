from rest_framework import serializers
from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'lastname', 'patronymic', 'photo', 'position', 'salary', 'age', 'department', 'department_name')


class DepartmentSerializer(serializers.ModelSerializer):
    num_employees = serializers.IntegerField(source='employees.count', read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'director', 'num_employees', 'total_salary')

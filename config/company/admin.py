from django.contrib import admin
from .models import Employee, Department
from django.utils.safestring import mark_safe


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1
    readonly_fields = ['firstname', 'lastname', 'patronymic', 'position']
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'firstname', 'lastname', 'patronymic', 'department', 'position', 'salary', 'age')
    list_filter = ('position', 'department', 'age')
    list_search = ('firstname', 'lastname', 'patronymic', 'position')
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} wigth="50" height="60" alt="Изображение сотрудника">')
    get_image.short_description = "Изображение"

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'total_salary')
    inlines = (EmployeeInline,)





#Banner Naming
admin.site.site_title = "BBINFO"
admin.site.site_header = "BBINFO"
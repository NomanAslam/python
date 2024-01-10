from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')
    list_filter = ('company',)

class QualificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('employee',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Color)
admin.site.register(Person)
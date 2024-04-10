from django.contrib import admin

from .models import Employee, JobTitle


class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'phone')
    list_display_links = ('user', )
    search_fields = ('phone', )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(JobTitle, JobTitleAdmin)

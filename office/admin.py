from django.contrib import admin
from office.models import Application,Employee,Role,Project

# Register your models here.

admin.site.register(Role)
admin.site.register(Project)
admin.site.register(Application)
admin.site.register(Employee)

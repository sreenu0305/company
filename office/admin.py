from django.contrib import admin
from office.models import Application,Employee,Role,Project,Team,Gmail

# Register your models here.

admin.site.register(Role)
admin.site.register(Project)
admin.site.register(Application)
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(Gmail)

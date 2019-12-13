
from django.contrib import admin
from .models import alumnus
from import_export.admin import ImportExportModelAdmin
from alumni.resources import alumnusResource

class alumnusAdmin(ImportExportModelAdmin):
    pass

resource_class = alumnusResource

admin.site.register(alumnus, alumnusAdmin)
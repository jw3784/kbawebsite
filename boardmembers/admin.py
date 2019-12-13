from django.contrib import admin

from .models import boardmember

class boardmemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    ordering = ('title',)

admin.site.register(boardmember,boardmemberAdmin)
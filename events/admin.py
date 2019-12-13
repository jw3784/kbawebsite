from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import event

class eventAdmin(SummernoteModelAdmin):
    list_display = ('event_title', 'event_date', 'event_cn', 'event_s')
    summernote_fields = ('event_content',)

admin.site.register(event,eventAdmin)
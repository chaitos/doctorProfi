from django.contrib import admin
from  .models import Appointment, Doctors

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'phone', "email", "date", "time", "doctor")
    list_display_links = ("id", 'name')
    ordering = ['date', 'time', 'name']

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ("id", 'name', 'specialization', "phone", "work_schedule", "email", "available")
    list_display_links = ("id", 'name')
    list_editable = ('available',)

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Doctors, DoctorsAdmin)

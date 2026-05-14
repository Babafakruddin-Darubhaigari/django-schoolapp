from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'age')
    search_fields = ('name',)
    list_filter = ('age',)

admin.site.register(Student, StudentAdmin)
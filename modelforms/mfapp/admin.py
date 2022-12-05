from django.contrib import admin
from .models import mfforms
# Register your models here.


@admin.register(mfforms)
class mfformsAdmin(admin.ModelAdmin):
    '''Admin View for mfforms'''

    list_display = ('id', 'name', 'catagory', 'village')

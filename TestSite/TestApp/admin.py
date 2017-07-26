from django.contrib import admin
from .models import *

# Register your models here.


class HiAdmin(admin.ModelAdmin):
    '''
        Admin View for Hi
    '''
    list_display = ('title', 'body', 'author', 'published_date')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')
    list_per_page = 25

admin.site.register(Hi, HiAdmin)

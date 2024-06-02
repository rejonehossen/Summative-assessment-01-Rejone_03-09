from django.contrib import admin
from myApp.models import *

class displaycustomuser(admin.ModelAdmin):
    list_display=[
        'username',
    ]
    
admin.site.register(customuser,displaycustomuser)
admin.site.register(jobmodel)
admin.site.register(seekerprofilemodel)
from helloRest.models import Box, Hello
from django.contrib import admin

# Register your models here.

class BoxAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'spin')

class HelloAdmin(admin.ModelAdmin):
    # ...
    list_display = ('boxSender', 'boxReceiver', 'date')


admin.site.register(Box, BoxAdmin)
admin.site.register(Hello, HelloAdmin)

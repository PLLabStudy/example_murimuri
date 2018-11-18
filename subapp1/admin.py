from django.contrib import admin
from .models import Example

# Register your models here.

class ExampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Example, ExampleAdmin)

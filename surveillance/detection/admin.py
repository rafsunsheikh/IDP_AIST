from django.contrib import admin
from .models import Detection

class DetectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Detection, DetectionAdmin)

# Register your models here.

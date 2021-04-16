from django.contrib import admin
from .models import Detection, Tower

class DetectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Detection, DetectionAdmin)
admin.site.register(Tower)

# Register your models here.

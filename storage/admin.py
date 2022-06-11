from django.contrib import admin
from .models import Sample, CustomColumn

# Register your models here.
admin.site.register(Sample)
admin.site.register(CustomColumn)

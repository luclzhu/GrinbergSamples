from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import Sample, CustomColumn, UserCustomColumn

# Register your models here.
admin.site.register(Sample)
admin.site.register(CustomColumn)
admin.site.register(UserCustomColumn)


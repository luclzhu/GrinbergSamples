from django.db import models
from django.db.models import Max

# Create your models here.
class Sample(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unpacked_list = []

    name = models.CharField(max_length=200)
    age_at_death = models.PositiveIntegerField(null=True, blank=True)
    time_of_death = models.TimeField(null=True, blank=True)
    day_of_death = models.DateField(null=True, blank = True)
    sex = models.CharField(max_length=2, null=True, blank=True, choices= [
        ('F', 'F'),
        ('M', 'M')
    ])
    case = models.CharField(max_length=200)
    braak = models.PositiveIntegerField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    custom_values = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

class UserCustomColumn(models.Model):
    display_title = models.CharField(max_length=200)
    internal_title = models.CharField(max_length=200)
    data_type = models.CharField(max_length=200, choices = [
        ('int', 'Integer'),
        ('date_time', 'Date and Time'),
        ('date', 'Date Only'),
        ('boolean', 'True/False'),
        ('string','Other')
            ], null=True, blank=True)
    in_use = models.BooleanField(default = False)
    UI_position = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.display_title


class CustomColumn(models.Model):
    title = models.CharField(max_length=208, null=True, blank=True)
    field_type = models.CharField(max_length=200, choices = [
        ('int', 'Integer'),
        ('date_time', 'Date and Time'),
        ('date', 'Date Only'),
        ('boolean', 'True/False'),
        ('string','Other')
                                  ], null=True, blank=True)
    UI_position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
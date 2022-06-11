from django.db import models

# Create your models here.
class Sample(models.Model):
    name = models.CharField(max_length=200)
    case = models.CharField(max_length=200)
    braak = models.PositiveIntegerField(null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    age_at_death = models.PositiveIntegerField(null=True, blank=True)
    time_of_death = models.DateTimeField(null=True, blank=True)
    sex = models.CharField(max_length=2, null=True, blank=True, choices= [
        ('F', 'F'),
        ('M', 'M')
    ])
    custom1 = models.CharField(max_length=200, null=True, blank=True)
    custom2 = models.CharField(max_length=200, null=True, blank=True)
    custom3 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.case

class CustomColumn(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    field_type = models.CharField(max_length=200, choices = [
        ('int', 'Integer'),
        ('date_time', 'Date and Time'),
        ('date', 'Date Only'),
        ('boolean', 'True/False'),
        ('string','Other')
                                  ], null=True, blank=True)
    def __str__(self):
        return self.title
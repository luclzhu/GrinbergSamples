from django.forms import ModelForm
from django import forms
from storage.models import Sample, UserCustomColumn
from .widgets import TimePickerInput, DatePickerInput
from django_json_widget.widgets import JSONEditorWidget

class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'
        widgets = {
            'date_received' : DatePickerInput(),
            'time_of_death': TimePickerInput(),
            'day_of_death' : DatePickerInput(),
            'custom_values' : JSONEditorWidget,
        }


class UserCustomColumnForm(ModelForm):
    class Meta:
        model = UserCustomColumn
        fields = '__all__'

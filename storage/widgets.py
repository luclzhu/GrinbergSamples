from django import forms

class DatePickerInput(forms.DateInput):
    input_type = 'date'
    format = '%m/%d%Y'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'
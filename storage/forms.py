from django.forms import ModelForm
from .models import Sample, CustomColumn

class SampleForm(ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'

class CustomColumnForm(ModelForm):
    class Meta:
        model = CustomColumn
        fields = '__all__'
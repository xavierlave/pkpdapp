from django import forms

from .models import MeasurementData


class DataForm(forms.Form):
    """
    This class defines the basic form for uploading measurement data in form
    of CSV files.
    """
    class Meta:
        model = MeasurementData
        fields = ('file_name',)
    data_file = forms.FileField()

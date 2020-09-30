#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

from django import forms
import pandas as pd

from .models import PharmacodynamicDataModel


class PharmacodynamicDataForm(forms.ModelForm):
    class Meta:
        model = PharmacodynamicDataModel
        fields = ['file_name', 'data_file']

    def clean(self):
        # If not file name provided, use name of file
        if self.cleaned_data['file_name'] is None:
            self.cleaned_data['file_name'] = self.cleaned_data[
                'data_file'].name

        # Get data file
        data_file = self.cleaned_data['data_file'].file

        # Read data as dataframe
        df = pd.read_csv(data_file)

        # Check column names
        if 'Time' not in df.keys():
            raise ValueError('Missing Time column.')
        if 'Y' not in df.keys():
            raise ValueError('Missing Y column.')
        if 'ConcInit' not in df.keys():
            raise ValueError('Missing ConcInit column.')



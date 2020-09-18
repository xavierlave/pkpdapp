#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

from django import forms

from .models import PharmacodynamicDataModel


class PharmacodynamicDataFrom(forms.ModelForm):
    class Meta:
        model = PharmacodynamicDataModel
        fields = ['data_file']

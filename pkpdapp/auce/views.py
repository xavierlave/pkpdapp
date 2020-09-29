#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import PharmacodynamicDataForm


class PharmacodynamicDataView(CreateView):
    template_name = 'auce/data.html'
    form_class = PharmacodynamicDataForm
    success_url = ('/auce/explore')

    #TODO:
    # 1. Save file under unique identifier name
    # 2. Save original file name
    # 3. If a second file is uploaded with the same file name ask whether the file should be uploaded again.
    #   - Can be extended by extracting more information baout the data and cross check that info to have a better
    #     way to figure out identity of dataset.


class PharmacodynamicExploreDataView(TemplateView):
    template_name = 'auce/explore.html'

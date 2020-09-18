#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

from .forms import PharmacodynamicDataForm
from django.views.generic.edit import FormView


class PharmacodynamicDataView(FormView):
    template_name = 'auce/upload.html'
    form_class = PharmacodynamicDataForm
    success_url = '/generic/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

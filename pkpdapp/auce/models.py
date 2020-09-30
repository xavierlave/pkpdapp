#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

from django.db import models


class PharmacodynamicDataModel(models.Model):
    """
    This model class provides the interface to the PD database.
    """
    file_name = models.CharField(
        verbose_name="Study Name", max_length=100, blank=True, null=True)
    data_file = models.FileField(
        verbose_name="Data File", max_length=100, upload_to='uploads/pd_data/')
    # upload_date = models.DateTimeField(auto_now=True)
    # number_id
    # ids

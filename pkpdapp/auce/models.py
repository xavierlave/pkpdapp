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
    data_file = models.FileField(upload_to='uploads/pd_data/')

#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

from django.contrib import admin

from .models import PharmacodynamicDataModel


class PharmacodynamicDataModelAdmin(admin.ModelAdmin):
    readonly_fields = ('upload_date',)


admin.site.register(PharmacodynamicDataModel, PharmacodynamicDataModelAdmin)

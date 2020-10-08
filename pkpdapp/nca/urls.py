#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

from django.urls import path

from . import views
from . import (  # noqa
    demo_nca_app
)


app_name = 'nca'

urlpatterns = [
    path('', views.NCAView.as_view(), name='explore'),
]

#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

import dash_core_components as dcc
import dash_html_components as html
from django.conf import settings
from django_plotly_dash import DjangoDash
import pandas as pd
import plotly.graph_objects as go


# Import data
path = settings.MEDIA_ROOT
data = pd.read_csv(path + '/uploads/pd_data/demo_pd_data.csv')




# Create figure
fig = go.Figure()

# Add data
fig.add_trace(go.Scatter(
    x=data['Time'],
    y=data['Y'],
))

# Set height of image
fig.update_layout(
    height=550
)

# Create dash app
app = DjangoDash('auce_dashboard')

app.layout = html.Div(children=[
    dcc.Graph(
        id='explore-dashboard',
        figure=fig
    )
])

#
# This file is part of PKDPApp (https://github.com/pkpdapp-team/pkpdapp) which
# is released under the BSD 3-clause license. See accompanying LICENSE.md for
# copyright notice and full license details.
#

'''
Temporary demo.
'''

import dash_core_components as dcc
import dash_html_components as html
from django.conf import settings
from django_plotly_dash import DjangoDash

import numpy as np
import pandas as pd 
import plotly
import plotly.colors
import plotly.graph_objects as go


# Import data
path = settings.MEDIA_ROOT
data = pd.read_csv(path + '/data/TCB4dataset.csv')

fig = go.Figure()

# # Define colorscheme
# n_ids = 1000 #len(data['ConcInit'].unique())*len(data['Y_type'].unique())
# colors = plotly.colors.qualitative.Plotly[:n_ids]

# y_types = data['Y_type'].unique()

# buttons_list = []
# current_index = 0

# plots_number = 0
# for index_y, y_type in enumerate(y_types):
#     IDs = selected_data_type['ConcInit'].unique()
#     for index_conc, concentration in enumerate(IDs):
#         plots_number += 1

# for index_y, y_type in enumerate(y_types):

#     selected_data_type = data.loc[data['Y_type'] == y_type]
#     IDs = selected_data_type['ConcInit'].unique()

#     #CREATE BUTTONS        
#     TF_list = np.repeat(False, current_index)
#     TF_list = np.append(TF_list, np.repeat(True, len(IDs)))
#     TF_list = np.append(TF_list, np.repeat(False, plots_number-current_index-len(IDs)))

#     buttons_list.append(
#         dict(   label="Y_type: %s" % y_type,
#                 method="update",
#                 args=[{"visible": TF_list},
#                     {"title": "Y_type: %s" % y_type}])
#     )

#     for index_conc, concentration in enumerate(IDs):

#         mask = selected_data_type['ConcInit'] == concentration
#         # Get observed data for indiviudal
#         observed_times = selected_data_type['Time'][mask].to_numpy()
#         observed_data = selected_data_type['Y'][mask]

#         # Plot data
#         fig.add_trace(go.Scatter(
#             x=observed_times,
#             y=observed_data,
#             #legendgroup="Y type : %s" % y_type,
#             name="Y_type: %s, Concentration: %d" % (y_type,concentration),
#             showlegend=True,
#             visible= True if index_y==0 else False,
#             hovertemplate=(
#                 "<b>Measurement </b><br>" +
#                 "Y_type: %s<br>" % y_type +
#                 "Concentration: %d<br>" % concentration +
#                 "Time: %{x:}<br>" +
#                 "Y: %{y:}<br>" +
#                 "<extra></extra>"),
#             mode="markers",
#             marker=dict(
#                 symbol='circle',
#                 opacity=0.7,
#                 line=dict(color='black', width=1),
#                 color=colors[index_conc]
#              )
#         ))
#         current_index += 1  
#     fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             direction="down",
#             active=0,
#             x=-0.4,
#             y=1,

#             buttons= buttons_list,
#         )
#     ]
# )
# # Set X, Y axis and figure size
# fig.update_layout(
#     autosize=True,
#     xaxis_title='Time in hours',
#     yaxis_title='Concentration',
#     template="plotly_white")

# # Set height of image
# fig.update_layout(
#     height=550
# )

# Create dash app
app = DjangoDash('auce_dashboard')

app.layout = html.Div(children=[
    dcc.Graph(
        id='explore-dashboard',
        figure=fig
    )
])

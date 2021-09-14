import os
from dash_bootstrap_components._components.Card import Card
from dash_bootstrap_components._components.CardBody import CardBody
from dash_bootstrap_components._components.Row import Row
from dash_core_components.Dropdown import Dropdown
from dash_html_components.Col import Col
from dash_html_components.Div import Div
from dash_table import DataTable
from flask.scaffold import F
from numpy import True_
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import io
import requests
import schedule
import time
from dash_table.Format import Format, Sign

dfmajorillness=pd.read_csv('combine1001.csv',sep=',')


majorillness = dfmajorillness[['DATE', 'DEATHS_DUE_TO_MAJOR_ILLNESS', 'DEATHS_DUE_BOTH_COVID_MAJOR_ILLNESS','PREDICTED_DEATHS_DUE_MAJOR_ILLNESS_IF_COVID_NEVER_HAPPEN' ,'DEATH_DUE_TO_ROAD_ACCIDENTS','DEATHS_BOTH_COVID_AND_ACCIDENTS','PREDICTED_ACCIDENTS_IF_COVID_NEVER_HAPPENS']]

# print(cases.head(20).style.background_gradient(cmap='Pastel1'))

DEATHS_DUE_TO_MAJOR_ILLNESS= list(majorillness.DEATHS_DUE_TO_MAJOR_ILLNESS )
DEATHS_DUE_BOTH_COVID_MAJOR_ILLNESS = list(majorillness.DEATHS_DUE_BOTH_COVID_MAJOR_ILLNESS)
PREDICTED_DEATHS_DUE_MAJOR_ILLNESS_IF_COVID_NEVER_HAPPEN = list(majorillness.PREDICTED_DEATHS_DUE_MAJOR_ILLNESS_IF_COVID_NEVER_HAPPEN)
DEATH_DUE_TO_ROAD_ACCIDENTS= list(majorillness.DEATH_DUE_TO_ROAD_ACCIDENTS )
DEATHS_BOTH_COVID_AND_ACCIDENTS = list(majorillness.DEATHS_BOTH_COVID_AND_ACCIDENTS)
PREDICTED_ACCIDENTS_IF_COVID_NEVER_HAPPENS = list(majorillness.PREDICTED_ACCIDENTS_IF_COVID_NEVER_HAPPENS)



fig16 = go.Figure()
fig16.add_trace( go.Scatter(x=majorillness['DATE'], y=majorillness['PREDICTED_DEATHS_DUE_MAJOR_ILLNESS_IF_COVID_NEVER_HAPPEN'],
                    mode='lines',
                    name='PREDICTED DEATHS DUE MAJOR ILLNESS IF COVID NEVER HAPPEN'))
fig16.add_trace( go.Scatter(x=majorillness['DATE'], y=majorillness['DEATHS_DUE_BOTH_COVID_MAJOR_ILLNESS'],
                    mode='lines',
                    name='DEATHS DUE BOTH COVID AND MAJOR ILLNESS'))
fig16.add_trace( go.Scatter(x=majorillness['DATE'], y=majorillness['DEATHS_DUE_TO_MAJOR_ILLNESS'],
                    mode='lines',
                    name='DEATHS DUE TO MAJOR ILLNESS'))     ,
fig16.add_vline(x=24, line_width=3, line_dash="dash", line_color="green",annotation_text="Start of corona virus",annotation_position="top left",)                                  
fig16.update_layout(title='Monthwise Distribution of Deaths(2018-2020)',
                   xaxis_title='Date',
                   yaxis_title='DEATHS',
                   template="plotly_dark")
# fig16.show()
fig17 = go.Figure()
fig17.add_trace( go.Scatter(x=majorillness['DATE'], y=majorillness['PREDICTED_ACCIDENTS_IF_COVID_NEVER_HAPPENS'],
                    mode='lines',
                    name='PREDICTED ACCIDENTAL DEATHS IF COVID NEVER HAPPENS'))
fig17.add_trace( go.Scatter(x=majorillness['DATE'], y=majorillness['DEATHS_BOTH_COVID_AND_ACCIDENTS'],
                    mode='lines',
                    name='DEATHS DUE BOTH COVID AND ACCIDENTS'))
fig17.add_trace( go.Scatter(x=majorillness['DATE'], y=majorillness['DEATH_DUE_TO_ROAD_ACCIDENTS'],
                    mode='lines',
                    name='DEATH DUE TO ROAD ACCIDENTS'))     ,
fig17.add_vline(x=24, line_width=3, line_dash="dash", line_color="green",annotation_text="Start of corona virus",annotation_position="top left",)                                  
fig17.update_layout(title='Monthwise Distribution of Deaths(2018-2020)',
                   xaxis_title='Date',
                   yaxis_title='DEATHS',
                   template="plotly_dark")
# fig17.show()

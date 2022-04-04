
import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.4) #pip install plotly==4.5.4
import plotly.express as px
from dash import html,dcc
from plotly.io.json import to_json_plotly
import plotly.io as pio
import plotly.graph_objects as go
from hermle201_overallGauge import *
from hermle201_barchartUren import *
from hermle201_metingGauge import *
from hermle201_chartBezettingsgraad import *
import dash_bootstrap_components as dbc

df = pd.read_excel('metingenFreesafdeling.xlsx', sheet_name='Hermle 201')

def barchartHermle201():
    return html.Div(children=[
            html.Div([
                dcc.Graph(figure=barchartNettoUren ,id='graphHermle201', config={'displayModeBar': False} ,style={
                        # "width": "50%",
                        # "height": "800px",
                        "display": "inline-block",
                        # "border": "3px #5c5c5c solid",
                        # "padding-top": "5px",
                        # "padding-left": "1px",
                        # "overflow": "hidden",
                        # "top": "50%",
                        # "left": "50%",
                        "margin-top": "10px",
                        # 'vertical-align': 'middle'
                        }),
                dcc.Graph(figure=barchartBezettingsgraad ,id='graphHermle201Bezettingsgraad', config={'displayModeBar': False} ,style={
                        # "width": "50%",
                        # "height": "800px",
                        "display": "inline-block",
                        # "border": "3px #5c5c5c solid",
                        # "padding-top": "5px",
                        # "padding-left": "1px",
                        # "overflow": "hidden",
                        # "top": "50%",
                        # "left": "50%",
                        "margin-top": "10px",
                        # 'vertical-align': 'middle'        
                        })]),
    
            html.Div([dcc.Graph(figure=gaugeMeting,config={'displayModeBar': False},style={
                                "margin-top": "1",
                                'vertical-align': 'middle',
                                "width": "50%",
                                "height": "50%",
                                "display": "inline-block",
                                }),                                        
        
            dcc.Graph(figure=gaugeOverAllMeting,config={'displayModeBar': False},style={
                        "margin-top": "1",
                        'vertical-align': 'middle',
                        "width": "50%",
                        "height": "50%",
                        "display": "inline-block",
                        })]),
])


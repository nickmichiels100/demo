from dash import dcc, html
import dash_bootstrap_components as dbc
import tab_hermle1
import tab_hermle2
import tab_klReichenbacher
import tab_grReichenbacher
from tab_style import *

def tabstripPage():
    return html.Div([
        html.H1('METINGEN', style={'color': 'gray', 'fontSize': 18, 'textAlign': 'center','font_family': 'Open Sans'}),                                                                                                                                                    
        dcc.Tabs(id = "tabs-styled-with-inline", value = 'Hermle_1', children = [
                dcc.Tab(label = 'Hermle_1', value = 'Hermle_1', style = tab_style, selected_style = tab_selected_style, children=[
                    tab_hermle1.barchartHermle201()
                ]),
                dcc.Tab(label = 'Hermle_2', value = 'Hermle_2', style = tab_style, selected_style = tab_selected_style, children=[
                    tab_hermle2.barchartHermle202()
                ]),
                dcc.Tab(label = 'Kl_Reichenbacher', value = 'Kl_Reichenbacher', style = tab_style, selected_style = tab_selected_style, children=[
                    tab_klReichenbacher.barchartKlReichenbacher()
                ]),
                 dcc.Tab(label = 'Gr_Reichenbacher', value = 'Gr_Reichenbacher', style = tab_style, selected_style = tab_selected_style, children=[
                    tab_grReichenbacher.barchartGrReichenbacher()
                ]),  
        ])
    ])

    
  

import pandas as pd     
import plotly.graph_objects as px
import plotly.graph_objects as go

df = pd.read_excel('metingenFreesafdeling.xlsx', sheet_name='Hermle 201')

barchartNettoUren= px.Figure(data=[go.Bar(
    name = 'NettoDraaiUren',
    # data_frame=df,
    x=df["Dag"],
    y=df["NettoDraaiUren"],
    marker_color='DarkOrange'

    ),
    go.Bar(
    name = 'TijdsBestek',
    # data_frame=df,
    x=df["Dag"],
    y=df["Tijdbestek"],
    marker_color='steelblue'
)
])
barchartNettoUren.update_layout(autosize=False,
    width=750,
    height=600,
    barmode='group',
    # paper_bgcolor='black' ,
    xaxis_tickangle=-45,
    plot_bgcolor="white",
    title= {'text': 'Draai Uren Hermle201',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
    ),
    ),
barchartNettoUren.update_yaxes( # the y-axis is in dollars
    # tickprefix="h", 
    showgrid=True,
    showline=True, linewidth=2, linecolor='gray', gridcolor='gray',
    title='Aantal Uren',
    tickwidth=3,ticks='outside', 
)
barchartNettoUren.update_xaxes(tickwidth=3,
ticks='outside', 
showticklabels=True,
showline=True, 
linewidth=2, 
linecolor='gray', 
title='Aantal metingen')

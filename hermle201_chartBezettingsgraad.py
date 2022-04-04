
import pandas as pd     
import plotly.graph_objects as px
import plotly.graph_objects as go

df = pd.read_excel('metingenFreesafdeling.xlsx', sheet_name='Hermle 201')
y = [df['GemiddeldeBezettingsgraad'].iloc[0] for _ in range(len(df['Dag']))]
mean = sum(y) / len(y)



barchartBezettingsgraad= px.Figure(data=[go.Bar(
    name = 'NettoDraaiUren',
    # data_frame=df,
    x=df["Dag"],
    y=df["Bezettingsgraad"],
    marker_color='DarkOrange',
    # texttemplate="$%{y}"
    ),
    
    go.Scatter(
            name = 'Gemiddelde bezettingsgraad',
            x=df['Dag'],
            y= y,
            mode='lines',
            line=dict(
                color="steelblue",
                width=2,
                # dash="dash",
            )),
])

barchartBezettingsgraad.update_layout(autosize=False,
    width=750,
    height=600,
    barmode='group',
    # paper_bgcolor='black' ,
    xaxis_tickangle=-45,
    plot_bgcolor="white",
    title= {'text': 'Bezettingsgraad per dag Hermle201',
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
barchartBezettingsgraad.update_yaxes( # the y-axis is in dollars
    # tickprefix="h", 
    showgrid=True,
    showline=True, linewidth=2, linecolor='gray', gridcolor='gray',
    title='Bezettingsgraad in %',
    tickwidth=3,ticks='outside', 
)
barchartBezettingsgraad.update_xaxes(tickwidth=3,
ticks='outside', 
showticklabels=True,
showline=True, 
linewidth=2, 
linecolor='gray', 
title='Aantal metingen')

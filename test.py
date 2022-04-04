import pandas as pd     #(version 1.0.0)
import plotly        #(version 4.5.4) #pip install plotly==4.5.4
import plotly.express as px
from dash import html,dcc
from plotly.io.json import to_json_plotly
import plotly.io as pio
import plotly.graph_objects as go
from flask import Flask,render_template
import pandas as pd
import numpy as np

import plotly.graph_objs as go
import plotly.offline as plt

df = pd.read_excel('metingenFreesafdeling.xlsx', sheet_name='Hermle 201')



trace = go.Bar(x=df["Dag"], y=df["NettoDraaiUren"])
layout = go.Layout(title="NettoDraaiUren", xaxis=dict(title="Dagen"),
yaxis=dict(title="NettoDraaiUren"), )
data = trace
fig = go.Figure(data=data, layout=layout)
plt.plot(fig)
import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel('overall bezettingsgraad.xlsx', sheet_name='Hermle 201')
df1 = pd.DataFrame(df)

gaugeMeting = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = df1.iloc[0]['Bezettingsgraad']*100,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Meting Bezettingsgraad %", 'font': {'size': 15, 'color':'black'}},
    delta = {'reference': 100, 'increasing': {'color': "RebeccaPurple", 'symbol':'%'}},
    gauge = {
        'axis': {'range': [0, 100], 'tickwidth': 3, 'tickcolor': "DarkOrange"},
        'bar': {'color': "DarkOrange"},
        'bgcolor': "white",
        'borderwidth': 0,
        'bordercolor': "black",
        'steps': [
            {'range': [0,100], 'color': 'steelblue'}]},
    ))

gaugeMeting.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})


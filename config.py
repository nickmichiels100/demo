from dash import Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    # 'https://codepen.io/chriddyp/pen/bWLwgP.css'
dashApp = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}])

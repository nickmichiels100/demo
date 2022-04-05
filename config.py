from dash import Dash
import os
from random import randint
import flask

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    # 'https://codepen.io/chriddyp/pen/bWLwgP.css'
dashApp = Dash(__name__,server=server, external_stylesheets=external_stylesheets, meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}])

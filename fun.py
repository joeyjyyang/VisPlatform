# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#title of web page
app.title = 'Dash Page'

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'xaxis' : dict(
                    title='x Axis',
                    titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'
                )),
                'yaxis' : dict(
                    title='y Axis',
                    titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f'
                ))
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
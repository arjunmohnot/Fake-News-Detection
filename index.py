import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask
from flask_restful import Resource, Api
from flask import request
import time
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output,State
import mod
import time

# external JS
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js",
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    },

    {
        'href': 'https://fonts.googleapis.com/css?family=Varela',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }

    
]



app = dash.Dash(__name__,    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)


app.title = 'Fake News Predictor | An open source tool to predict fake news using machine learning.'

app.config['suppress_callback_exceptions']=True

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

PLOTLY_LOGO = "/"




#server = Flask('my_app')
#app = dash.Dash(server=server)
api = Api(server)

todos = {}
class HelloWorld(Resource):
    def get(self):
        return " "

    def put(self):
        
        sT=str(request.form['data'])
        numericValue=mod.runs(str(sT))*10
        return str(numericValue)

api.add_resource(HelloWorld, '/hello')



# Update the index

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':

        # Default path is / . It will render Page_1_layout
        
        return page_1_layout

    elif pathname=='/validate':

        return page_2_layout

    else:
        return []
    # You could also return a 404 "URL not found" page here


page_1_layout = html.Div([


        # Creating a Navbar

        dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/keras-logo-small-wb-1.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("FakeNews Detection", className="ml-4")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/",
            ),

            
            dbc.NavbarToggler(id="navbar-toggler"),
           
        ],
        color="dark",      
        dark=True,
        sticky="top",
    ),


    
     html.Div([    
     html.Div([

        dcc.Interval(id="interval", interval=250, n_intervals=0),
        html.Div([


        html.Div(id='variables',children=[],style={"display":"None"}),

         # Inside this class we are making dcc.Upload which will upload our image.
            
       dbc.Card(
            [
                dbc.CardHeader("FakeNews Detection \u2b50"),
                dbc.CardBody(
                    [html.Div([




                html.Div([

                 html.Div([
                  html.H5('Enter Your News 		\ud83d\udcbb'),
                       
                 html.Div([

                                    
                                    dcc.Input(
                                    id="fake-news-text",
                                    placeholder='Enter Your News',
                                    type='text',
                                    value='',
                                    style={"width":"50%"}
                           
                                ),
                                html.Div([
                                 dbc.Button("Submit 	\ud83d\udc4b", id="fake-news-button", className="mr-1",color="warning",outline=True,style={"margin-top":"3%","margin-top":"5px",'border':"#FFC107 2px solid "})
       ],className="twelve columns"),   
                                    
                            ],className="twelve columns",style={'margin-bottom':'10px'}),

                    ],className='twelve columns'),


                  ],className='twelve columns'),
         ],className="ten columns offset-by-one")  ]), ]
        ),],style={ 'margin-top':'3%'}),   


         html.Div(id='output-image',style={"margin-top":"10px","margin-bottom":"10px"}),



          html.Div(id='output-image-1',style={"margin-top":"10px","margin-":"10px"}),


    ],className='ten columns offset-by-one'),
     ]),

])


@app.callback(Output('output-image', 'children'),
              [Input('fake-news-button','n_clicks')],
              [State('fake-news-text', 'value')])
def update_graph_interactive_images(buttons,text):

    if text=="":
        return ''

    numericValue=mod.runs(str(text))*10

    print(numericValue)
    
    gauge=daq.Gauge(
    showCurrentValue=True,
    color='#FFC107',
    value=numericValue,
    label='True-Meter',
    max=10,
    min=0,
)  
    
    return gauge





page_2_layout = html.Div([])



if __name__ == '__main__':
    app.run_server(debug=True)

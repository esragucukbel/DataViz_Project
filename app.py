# importing all necessary libs
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import dash
import os
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings("ignore")

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)

# Data reading
df_map = pd.read_excel(os.path.abspath(parent_dir+'/data/'+'aggregated_map_data.xlsx'))
df_attacks = pd.read_excel(os.path.abspath(parent_dir+'/data/'+'aggregated_attacktype_data.xlsx'))
df_yearly = pd.read_excel(os.path.abspath(parent_dir+'/data/'+'aggregated_yearly_data.xlsx'))


# World map
def update_map():

    df_map["hover_text"] = "Country: " + df_map["country_txt"].astype(str) + "<br>" + "Unsafety Index: " + df_map["calculated_index"].round(decimals= 2).astype(str) + "<br>"+"# of Killed and Wounded People: " +  df_map["total_kills_injured"].astype(str)+ "<br>"+"# of Killed People: "+  df_map["nkill"].astype(str)+ "<br>"+ "# of Wounded People: "+  df_map["nwound"].astype(str)
    
    trace = go.Choropleth(locations=df_map["id"],
                          z=df_map["calculated_index"],
                          text=df_map["hover_text"], 
                          hoverinfo="text" ,
                          colorscale="rdylgn",
                          reversescale = True,
                          marker={"line": {'color': 'rgb(180,180,180)','width': 0.5}},
                          colorbar={"thickness": 20,"len": 0.7, "x": 0.9, "y": 0.7,
                                   'title': {"text": 'Safety Index', "side": "bottom"},
                                 }
                         )   
    return {"data": [trace],
            "layout": go.Layout(height=800, width= 1200 ,
                                geo={'showframe': False,
                                     'showcoastlines': False,
                                     'projection': {'type': "miller"}})}



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Dashboard'


app.layout = html.Div([
    html.Div([html.H1("Global Terrorism Dashboard")],
                 style={'textAlign': "center", "padding-bottom": "30"}, 
                 className="six-column"),
    html.Div([dcc.Graph(id="world-map", 
                       style = {'textAlign': "center"}, 
                       figure = update_map(), className="twelve columns"), 
              html.A('Source: Global Terrorism Database(GTD)',href = 'https://www.start.umd.edu/gtd/', 
                      style={'fontStyle': "italic", 'color': '#273746'})]), 
    html.Div([html.H2('First 15 Countries with Most Organized and Unorganized Attacks'),
              dcc.Graph(id="horizontal-bar")], 
             className="twelve columns"),
    html.H2(id = 'country-name',  children=["init"] , 
            style={'textAlign': "center", "padding-bottom": "30"} ),
    html.Div(dcc.Graph(id="incidents"),  id = 'incident-box', 
             style = {'visibility': 'hidden'}, className="five columns"),
    html.Div(dcc.Graph(id="fatalities"),  id = 'fatalities-box', 
             style = {'visibility': 'hidden'}, className="five columns"),
    
])


##### Figure Updates with CallBacks ##### 
@app.callback(
    dash.dependencies.Output('country-name', 'children'),
    [dash.dependencies.Input('world-map', 'clickData')])
def update_title(clickData):
    text = ''
    if clickData is not None:
        selected_country = clickData['points'][0]['location']
        text = str(selected_country)  
    return text

@app.callback(
    dash.dependencies.Output('horizontal-bar', 'figure'),
    [dash.dependencies.Input('world-map', 'clickData')])
def update_horizontal_bar(clickData):

    fig = go.Figure()
    years = df_attacks['iyear'].sort_values().unique()

    for step in years:
        countries = df_attacks[df_attacks['iyear']==step]
        fig.add_trace(go.Bar(
            visible=False,
            y=countries['country_txt'],
            x=countries['organized'],
            name='Organized',
            orientation='h',
            marker=dict(
                color='rgba(246, 78, 139, 0.6)',
                line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
            )
        ))
        fig.add_trace(go.Bar(
            visible=False,
            y=countries['country_txt'],
            x=countries['unorganized'],
            name='Unorganized',
            orientation='h',
            marker=dict(
                color='#5885AF',
                opacity = 0.8,
                line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
            )
        ))

    fig.data[-1].visible = True
    fig.data[-2].visible = True

    steps = []
    for i in range(len(years)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},],  # layout attribute
        )
        step["args"][0]["visible"][i * 2] = True  # Toggle i'th trace to "visible"
        if i * 2 < len(fig.data) - 1:
            step["args"][0]["visible"][i * 2 + 1] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=48,
        currentvalue={"prefix": "Selected Year: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        barmode='stack'
    )

    fig['layout']['sliders'][0]['currentvalue']['prefix']='Year: '
    for i, date in enumerate(years, start = 0):
        fig['layout']['sliders'][0]['steps'][i]['label']=str(date)
        
#     fig.update_layout(margin=dict(t=120))
    fig['layout']['sliders'][0]['pad']=dict(t= -360,)
    
    return fig
        



@app.callback(
    [dash.dependencies.Output('incidents', 'figure'), dash.dependencies.Output('incident-box', 'style')],
    [dash.dependencies.Input('world-map', 'clickData')])
def update_incidents(clickData):
    df_agg = ''
    if clickData is not None:
        selected_country =clickData['points'][0]['location']
        df_agg = df_yearly[df_yearly['id'] == selected_country].groupby(by=['iyear','country',
                                                                            'country_txt','id', 
                                                                            'isOrganized']).agg({
                                                                                        'total_attacks':'sum'}).reset_index()
    fig = px.line(df_agg, x="iyear", y="total_attacks", color='isOrganized',
                  labels={
                     "iyear": "<b>Year</b>",
                     "total_attacks": "<b>Number of Incidents</b>",
                     "isOrganized": " "
                 }, title="<b>Number of Incidents by Years</b>")
    
    return fig,  {'visibility':'visible'}

@app.callback(
    [dash.dependencies.Output('fatalities', 'figure'), dash.dependencies.Output('fatalities-box', 'style')],
    [dash.dependencies.Input('world-map', 'clickData')])
def update_fatalities(clickData):
    df_agg = ''
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    if clickData is not None:
        selected_country =clickData['points'][0]['location']
        df_agg = df_yearly[df_yearly['id'] == selected_country].groupby(by=['iyear','country',
                                                                        'country_txt','id']).agg({
                                                                                        'nkill':np.sum,
                                                                                        'nwound':np.sum  }).reset_index()
    # Add traces
    fig.add_trace(
        go.Line(x=df_agg['iyear'], y=df_agg['nwound'], name="Injuries", line=dict(color="#D4AC0D")),
        secondary_y=False,
    )

    fig.add_trace(
        go.Line(x=df_agg['iyear'], y=df_agg['nkill'], name="Fatalities", line=dict(color="#943126")),
        secondary_y=True,
    )     
    
    # Add figure title
    fig.update_layout(
        title_text="<b>Number of Injuries and Fatalities by Years</b>"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="<b>Year</b>")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Injuries</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Fatalities</b> ", secondary_y=True)

    
    return fig, {'visibility':'visible'}
  
app.run_server(debug=False)
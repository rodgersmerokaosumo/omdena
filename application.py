import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import folium
from folium import plugins
# load data
df = pd.read_csv('kenyan_power_plants.csv')
df_grp  = df.groupby(['name']).mean()
df_grp = df_grp.reset_index()


center = [-0.3500, 39.6050]
map_kenya = folium.Map(location=center, zoom_start=8)
#display map
locations = []
for index, row in df.iterrows():
    locations.append([row['latitude'], row['longitude']])

marker_cluster = plugins.FastMarkerCluster(locations).add_to(map_kenya)


# initialize app
app = dash.Dash(__name__)
cols = ['capacity_mw', 'estimated_generation_gwh_2013', 'estimated_generation_gwh_2014',
        'estimated_generation_gwh_2015', 'estimated_generation_gwh_2016', 'estimated_generation_gwh_2017']
plants = list(df['name'].unique())
# set app layout
app.layout = html.Div(children=[
    html.H1('Kenyan Power Plants', style={'textAlign':'center'}),
    html.Br(),
    html.Div([
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in cols],
            value='capacity_mw',
            id='dropdown',
            style={"width": "50%", "offset":1,},
            clearable=False,
        ),
    ]),
    html.Section(className="sections section_a", children = [
        html.Article([
        dcc.Graph(id='barplots')
],  className="plot", style={'display': 'inline-block'}),

        html.Br(),
        html.Article([
        dcc.Graph(id='pie-plots')
], className="plot"),
        
    ]),
    html.Section(className="sections section_b", children = [
        html.Article([
        dcc.Graph(id='scatter-plots')
], className="plot")
        ])
        
    ])

# callbacks
@app.callback(
    Output(component_id='barplots', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)
def update_bars(feature):
    fig = px.bar(df, x='name', y=feature,  title=f" Bar Plot showing {feature}", width=600, height=450)
    fig.update_xaxes(nticks= 5)
    fig.update_layout(title_x=0.5)
    return fig

@app.callback(
    Output(component_id='pie-plots', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)
def update_pies(feature):
    fig = px.pie(df, values=feature, names='name', title=f'Pie Plots for Proportions of Plants in Kenya')
    fig.update_layout(showlegend=False)
    fig.update_layout(title_x=0.5)
    return fig

@app.callback(
    Output(component_id='scatter-plots', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)
def update_scatter(feature):
    fig = px.scatter(df_grp, x=feature, y="name", color="name", symbol="name", size = feature, title="Average Performance Kenyan Power Plants" \
        , width=850, height=450)
    fig.update_layout(showlegend=False)
    fig.update_layout(title_x=0.5)
    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
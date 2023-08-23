import pandas as pd 
import numpy as np 

import dash 
from dash import dcc, html, Input, Output, State 
import dash_bootstrap_components as dbc

import plotly.graph_objects as go 
import plotly_express as px 



####### Dataset #######

df = pd.read_csv("superstore_dataset.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"], dayfirst= True)
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"], dayfirst= True)

dff = df.to_dict()




####### Layout #######

app = dash.Dash(__name__)

app.layout = dbc.Container([
    
    ])
    
if __name__ == "__main__":
    app.run_server(debug = True)
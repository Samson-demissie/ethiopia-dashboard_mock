from jupyter_dash import JupyterDash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Extended mock humanitarian data for Ethiopia
data_humanitarian = {
    "Region": ["Addis Ababa", "Oromia", "Amhara", "Tigray", "SNNPR", "Afar"],
    "Population": [3000000, 35000000, 20000000, 6000000, 20000000, 1500000],
    "Literacy Rate": [92, 50, 55, 60, 45, 35],
    "Food Insecurity Rate": [10, 45, 30, 40, 50, 60],
    "IDPs": [50000, 800000, 300000, 200000, 400000, 100000],
    "Refugees": [10000, 20000, 15000, 50000, 25000, 8000],
    "Malnutrition Rate": [5, 15, 20, 18, 25, 30],
    "Water Access Rate": [90, 60, 65, 70, 50, 40],
}

mock_data = pd.DataFrame(data_humanitarian)

fig_population_bar = px.bar(mock_data, x="Region", y="Population", title="Population by Region")
fig_population_hist = px.histogram(mock_data, x="Population", nbins=5, title="Population Distribution (Histogram)")
fig_literacy_line = px.line(mock_data, x="Region", y="Literacy Rate", title="Literacy Rate by Region")
fig_food_insecurity = px.line(mock_data, x="Region", y="Food Insecurity Rate", markers=True, title="Food Insecurity Rate by Region")
fig_idps_bar = px.bar(mock_data, x="Region", y="IDPs", title="Internally Displaced Persons (IDPs) by Region")
fig_malnutrition_scatter = px.scatter(mock_data, x="Malnutrition Rate", y="Water Access Rate", color="Region", title="Malnutrition vs Water Access")

app = JupyterDash(__name__)

app.layout = html.Div([
    html.H1(
        "Ethiopia Humanitarian Dashboard",
        style={
            "textAlign": "center",
            "color": "blue",
            "fontSize": "60px",
            "backgroundColor": "yellow"
        }
    ),
    html.Div("A visual overview of various indicators.", style={"textAlign": "left", "fontSize": "10px", "color": "lightgray"}),

    html.Div([
        dcc.Graph(figure=fig_population_bar),
        dcc.Graph(figure=fig_literacy_line),
        dcc.Graph(figure=fig_food_insecurity)
    ], style={
        "display": "grid",
        "gridTemplateColumns": "1fr 1fr",
        "gap": "10px",
        "marginLeft": "200px"
    }),

    html.Div([
        html.Div(
            dcc.Graph(figure=fig_idps_bar),
            style={
                "width": "20%",
                "display": "inline-block",
                "verticalAlign": "top",
                "backgroundColor": "#e0e0e0"
            }
        ),
        html.Div(
            dcc.Graph(figure=fig_malnutrition_scatter),
            style={
                "width": "60%",
                "display": "inline-block",
                "marginLeft": "5px",
                "border": "2px dashed red"
            }
        ),
    ], style={"marginTop": "20px"}),

    html.Div([
        dcc.Graph(figure=fig_population_hist)
    ], style={
        "textAlign": "right",
        "backgroundColor": "#fff",
        "border": "1px dotted black",
        "padding": "30px"
    }),

    html.Div([
        html.P(
            "Disclaimer: Data may be inaccurate or outdated.",
            style={"fontSize": "25px", "color": "red", "marginLeft": "30px"}
        ),
        html.P(
            "Source: Mocked data for demonstration purposes only.",
            style={"fontSize": "12px", "color": "black", "marginLeft": "100px"}
        ),
        html.P(
            "Note: Regions not exhaustive.",
            style={"fontSize": "15px", "color": "purple", "marginTop": "50px"}
        ),
    ]),

    html.Div("End of Dashboard", style={"textAlign": "center", "color": "green", "fontSize": "14px"})
],
style={
    "backgroundColor": "#f0f0f0",
    "margin": "0px auto",
    "width": "90%",
    "border": "5px solid pink"
})

app.run_server(mode='external')

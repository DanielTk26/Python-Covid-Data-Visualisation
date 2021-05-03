import pandas as pd
import plotly.express as px

dataFrame = pd.read_csv("data.csv")

chart = px.scatter(dataFrame, x = "Date", y = "Cases", color = "Country", title = "Number of COVID-19 cases in various Countries",
    labels={
                "Cases": "Cases in thousands",
                "Country": "Countries"
            })


chart.show()
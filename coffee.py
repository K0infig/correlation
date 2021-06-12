import csv
import plotly.express as px

with open("coffe.csv") as file:
    df = csv.DictReader(file)
    fig = px.scatter(df, x= "Coffee in ml", y ="sleep in hours")
    fig.show()
import csv
import plotly.express as px

with open("icecream.csv") as file:
    df = csv.DictReader(file)
    fig = px.scatter(df, x= "Temperature", y ="Ice-cream Sales( ₹ )")
    fig.show()
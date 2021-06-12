import csv
import numpy as np
import plotly.express as px

def plotGraph(dataPath):
    with open(dataPath) as file:
        df = csv.DictReader(file)
        fig = px.scatter(df, x= "Temperature", y ="Ice-cream Sales( ₹ )")
        fig.show()

def getDataSource(dataPath):
    ice_cream_sales =[];
    temperature =[]

    with open(dataPath) as file:
        reader = csv.DictReader(file)

        for row in reader:
            ice_cream_sales.append(float(row['Ice-cream Sales( ₹ )']))
            temperature.append(float(row['Temperature']))

    return { "x": ice_cream_sales, "y": temperature}


def calcCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    
    print(" The co-efficient of correation is: ", correlation[0,1])


def setup():

    dataPath="icecream.csv"

    dataSource= getDataSource(dataPath)
    calcCorrelation(dataSource)


setup()

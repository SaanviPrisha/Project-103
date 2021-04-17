import pandas as pd
import plotly.express as px

data = pd.read_csv("covid-19_data.csv")
dataFrame = pd.DataFrame(data)

graph = px.scatter(dataFrame,x = "date" , y = "cases", color = "country", title="Covid-19 Cases")
graph.show()
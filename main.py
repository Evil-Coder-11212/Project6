import pandas as pd
import plotly.figure_factory  as ff
import numpy

# My new method
df = pd.read_csv("./data.csv")

fig = ff.create_distplot([df["Avg Rating"]], ["Mobile Brand"])

fig.show()
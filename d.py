import csv
import pandas as pd
import plotly.express as px

df=pd.read_csv("d.csv")
fig=px.scatter(df,x="student_id",y="level",size="attempt",size_max=30)
fig.show()
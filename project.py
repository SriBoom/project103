import pandas
import plotly_express

df=pandas.read_csv("data.csv")
fig=plotly_express.scatter(df,x="date",y="cases",color="country", size_max=60)
fig.show()

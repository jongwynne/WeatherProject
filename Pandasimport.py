import pandas as pd
import plotly.tools as tls
import plotly.plotly as py
py.sign_in('joncrazylivecom', 'M5uNJGhWf7A6m4RI2wTU')
import cufflinks as cf
carsales = pd.read_csv('C:\Users\Student22\Desktop\usedcars.csv')
csbyyear = carsales.groupby(['year']).mean()
csbyyear.scatter_matrix()

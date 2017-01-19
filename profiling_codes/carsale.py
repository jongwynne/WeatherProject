import scipy
import numpy as np
import pandas as pd
import plotly.plotly as py
# import visplots
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from sklearn import preprocessing, metrics
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from scipy.stats.distributions import randint
init_notebook_mode()
carsales = pd.read_csv(r"C:\Users\Student22\Desktop\usedcars.csv", sep=",")

cs = carsales[['km', 'year', 'powerPS', 'avgPrice']]
# print cs.describe()
bins = [412, 3244, 7648, 20409, 66936]
group_names = ['Cheap', 'Okay', 'Good', 'Expensive']
cs['binned'] = pd.cut(cs['avgPrice'], bins)
cs['categories'] = pd.cut(cs['avgPrice'], bins, labels=group_names)
print cs
npArray = np.array(cs)
Y = npArray[:, 5]
yFrequency = scipy.stats.itemfreq(Y)

data = [
    Bar(
    x = ['Cheap', 'Okay', 'Good', 'Expensive'],
    y = [yFrequency[0][1], yFrequency[1][1], yFrequency[2][1], yFrequency[3][1]],
    marker = dict(color=['yellow', 'green', 'blue', 'blue'])
    )
]
layout = Layout(
    xaxis = dict(title = "Car Prices"),
    yaxis = dict(title = "Counts"),
    width = 500
)

fig = dict(data = data, layout = layout)
iplot(fig)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#from sklearn.model_selection import train_test_split

from xgboost import XGBRFRegressor, XGBRFClassifier
import xgboost as xgb

from sklearn.metrics import mean_squared_error

# import warnings
# warnings.filterwarnings('ignore')

plt.style.use('fivethirtyeight')
color_pal = sns.color_palette()

data = pd.read_csv(r'C:\To lenovo\Baramej_Courses\projects\python\Time Series Predicting Xgboost\PJME_hourly.csv')

data = data.set_index('Datetime')
data.index = pd.to_datetime(data.index)

data['hour'] = data.index.hour
data['dayofweek'] = data.index.dayofweek
data['month'] = data.index.month
data['quarter'] = data.index.quarter
data['year'] = data.index.year
data['dayofyear'] = data.index.dayofyear

print(data.head())   

train_set = data.loc[data.index<'01-01-2015']
test_set = data.loc[data.index >= '01-01-2015']

x_train =  train_set.drop('PJME_MW', axis=1)
y_train = train_set['PJME_MW']

x_test = test_set.drop('PJME_MW', axis=1)
y_test = test_set['PJME_MW']

model = XGBRFRegressor(n_estimator=1000, early_stopping_round = 50)

model.fit(x_train, y_train)

model.score(x_train, y_train)

pred = model.predict(x_test)
mean_sq_error = mean_squared_error(pred, y_test)
mean_sq_error

np.sqrt(mean_squared_error(pred, y_test))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("50_Startups.csv")
x=data.iloc[ : , :-1].values
y=data.iloc[ : , -1].values

from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder
cl=ColumnTransformer(transformers=[('encoder' , OneHotEncoder() , [3])] , remainder='passthrough')
x=np.array(cl.fit_transform(x))
#print(x)

from sklearn.model_selection import train_test_split
x_train , x_test ,  y_train , y_test=train_test_split(x ,y , test_size=0.2 ,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train , y_train)  #here our model train and redy to predict

#Predict the test set result
y_predict=regressor.predict(x_test)  #this predict the value of x_test , and we compare these with y_test

np.printoptions(precision=2)  #this will give 2 numbers after decimal.
print(np.concatenate((y_predict.reshape(len(y_predict) , 1) , y_test.reshape(len(y_test) ,1)),1))

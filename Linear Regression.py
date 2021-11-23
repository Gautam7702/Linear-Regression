# In this program, we use regression model to find the relation between headsize and Brain weight

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize']  = (20.0,10.0)
data = pd.read_csv('headbrain.csv')          # we read the data from headbreain.csv and create a 2d array which is stored in data
x = data['Head Size(cm^3)'].values  # x stores the head size (in (cm^3) )
y = data['Brain Weight(grams)'].values #y stores the Brain Weight (in grams)

mean_x  = np.mean(x)  # we calculate the mean of x using numpy module
mean_y = np.mean(y)   # we calculate the mean of y using numpy module

m = len(x)  # m contains the total number of values 
numer = 0
denom = 0
 
# here we calculate the value of slope of regression line using the formula
for i in range(m):
    numer += (x[i]-mean_x)*(y[i]-mean_y)
    denom +=  (x[i]-mean_x)**2

slope = numer/denom 
c = mean_y - slope*mean_x

max_x = np.max(x)+100
min_x  = np.min(x) -100

xIngraph = np.linspace(min_x,max_x,1000)
yIngraph = c + slope*xIngraph

Xentered = float(input("Enter your head size in cm^3 "))
Yprobable = c+ (slope * Xentered)
print("Your possible Brain weigt  is ",Yprobable," grams")
#plotting the line
plt.plot(xIngraph,yIngraph,color= '#58b970',label = 'Regression Line')
#plotting Scatter Points
plt.scatter(x,y,c='#ef5423',label='Scatter Plot')
plt.xlabel('Head size in cm^3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()








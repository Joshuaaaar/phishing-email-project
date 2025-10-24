import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("code/Phishing_Email.csv")

# Getting X data 
x = df.drop('Email Type', axis=1)
# Getting Y data
y = df['Email Type']

# Splitting between training and testing set

x_train , x_test , y_train, y_testt = train_test_split(x,y,test_size=0.2,random_state=100)
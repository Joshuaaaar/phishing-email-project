import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv("Phishing_Email.csv")

# Getting X data 

x = df["Email Text"].fillna("")
# Getting Y data
y = df['Email Type']

# Splitting between training and testing set

x_train , x_test , y_train, y_testt = train_test_split(x,y,test_size=0.2,random_state=100 , stratify=y)

# Turning text into numbers 

vec = TfidfVectorizer(stop_words="english")
x_train_vec = vec.fit_transform(x_train)
x_test_vec = vec.transform(x_test)


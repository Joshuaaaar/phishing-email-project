from dataSet import x_train_vec , x_test_vec, y_testt , y_train
from sklearn.linear_model import LogisticRegression

cl = LogisticRegression(max_iter=1000) 
cl.fit(x_train_vec,y_train)


y_cl_train_pred = cl.predict(x_train_vec)
y_cl_test_pred = cl.predict(x_test_vec)


print(y_cl_train_pred)
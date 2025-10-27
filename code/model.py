from dataSet import x_train_vec , x_test_vec, y_testt , y_train , vec
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, log_loss
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib



cl = LogisticRegression(max_iter=1000) 
cl.fit(x_train_vec,y_train)


y_cl_test_pred = cl.predict(x_test_vec)

# Peformance checking

accur_test = accuracy_score(y_testt, y_cl_test_pred)


# joblib

joblib.dump(cl, "phishing_model.joblib")
joblib.dump(vec, "vectorized.joblib")

#Testing custom input 

#new_email_vec = vec.transform(new_email)

#prediction = cl.predict(new_email_vec)[0]

#print(prediction)

#print(accur_test)

#print(classification_report(y_testt,y_cl_test_pred))


#print(confusion_matrix(y_testt,y_cl_test_pred))
from dataSet import x_train_vec , x_test_vec, y_testt , y_train , vec
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, log_loss
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
import joblib



#cl = LogisticRegression(max_iter=1000) 
#cl.fit(x_train_vec,y_train)

param_grid = {
    
    "C": [0.1,0.5,1,2,5,10],
    
    "penalty":["l1","l2"],
    
    "class_weight":[None,  "balanced"],
    
    "solver":["liblinear"],
    
    "max_iter":[2000],
}

grid = GridSearchCV(
    LogisticRegression(), param_grid, scoring='f1', cv=5, n_jobs=-1,verbose=0
)

grid.fit(x_train_vec,y_train)
better_cl = grid.best_estimator_

y_cl_test_pred = better_cl.predict(x_test_vec)

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

print(classification_report(y_testt,y_cl_test_pred))


print(confusion_matrix(y_testt,y_cl_test_pred))
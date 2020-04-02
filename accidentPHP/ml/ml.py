import pandas as pd
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
data = pd.read_csv('Accident_DataSet.csv')

X_train = data.iloc[:, :-1].values
y_train = data['acc_severity'].values

testing=[[30.1 , 50.1 , 60 , 1]]
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB()
gnb.fit(X_train, y_train) 
gnb_predictions = gnb.predict(testing) 

print(gnb_predictions)

import pickle
pickl = {'GNBmodel': gnb}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )
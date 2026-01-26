# Libraries
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
# Packages
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn import svm
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix

# 1. Data Selection and Loading

data1=pd.read_csv("file1.csv")
print("<----Dataset---->")
print("*****************")
print(data1.head(10))

    # Have a look at the shuffle five thousand records
shuffled = shuffle(data1)
print(shuffled.head(5000))
data=shuffled.head(5000)
print(" <-----Shuffled dataset------>")
print("******************************")
print(data.head(10))

warnings.filterwarnings("ignore")

# 2. Preprocessing

print("<----Preprocessing----->")
print("***********************")
data2=data.isnull().sum()
print(data2)

    # Unwanted Column Removal
print("<------Removing Unwanted Column------->")
print("***************************************")

data=data.drop(['Flow_ID','Src_IP','Dst_IP','Flow_IAT_Mean','Flow_Pkts/s','Flow_IAT_Std','Bwd_Pkt_Len_Std','Flow_Byts/s','Idle_Mean','Idle_Std','Src_Port','Dst_Port'], axis=1)
data=data.drop(['Timestamp'], axis=1)
print(data.head(10))
print()

    # Label Encoding
    # create a LabelEncoder object
print("<-----Label Encoding------->")
print("****************************")

labelencoder=LabelEncoder()
data["Sub_Cat"]=LabelEncoder().fit_transform(data["Sub_Cat"])
data["Cat"]=LabelEncoder().fit_transform(data["Cat"])
#data["Label"]=LabelEncoder().fit_transform(data["Label"])
print("Label Encoding Dataset")
print(data.head(50))
print()

# Clustering

X1 = data.iloc[:, [65, 72]].values  
kmeans = KMeans(n_clusters=2, init='k-means++', random_state= 42)  
y1=kmeans.fit_predict(data) 
print(y1)

# Splitting the data into features and target sets
print("<--------Data Splitting--------->")
print("*********************************")

    #Splitting the values into xand y
x=data
y=y1
print("Data Splitted into x and y")
print("X Label Dataset")
print("Y Label Dataset")
print()

# 3. Feature Selection

print("<-----Feature Selection-------->")
print("********************************")

x =abs(x)
# Using ChiSquare Algorithm
chi2_selector = SelectKBest(chi2, k=25)
X = chi2_selector.fit_transform(x, y)
#print(X_kbest.head(20))
print('Original number of features:', x.shape)
print('Reduced number of features:', X.shape)
print()

# 4. Data Splitting

print("<--------Data Splitting--------->")
print("*******************************")
 # splitting the data into the training and test set.
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=(0.25),random_state=1)
print()

# 5. Classification

print("<----Algorithm Implementation------>")
print("************************************")
print()
print("Support Vector Machine")
print("**********************")

clf = svm.SVC() # Linear Kernel
clf.fit(x_train, y_train)
y_pred1 = clf.predict(x_test)
acc_dt2=accuracy_score(y_test,y_pred1)
result1=(acc_dt2*100) 
print("Accuracy of  Support Vector machine:", result1)
print()

print("<---------Classification Report ---------->")
print("*******************************************")
print(metrics.classification_report(y_test, y_pred1))
print()

print("Confusion Matrix")
print("****************")
 #calculate the confusion matrix
cf_matrix = confusion_matrix(y_test,y_pred1)
print(cf_matrix)
print()
print('Confusion matrix\n\n')
sns.heatmap(cf_matrix, annot=True)
plt.title("Confusion Matrix")
plt.show()          
print()


print("Artifical Neural Network")
print("************************")

    #create a classifier object
ann = Sequential()
ann.add(Dense(6, input_dim=25, activation= "relu"))
#ann.add(Dropout(0.2))
ann.add(Dense(5, activation= "relu"))
#ann.add(Dropout(0.2))
ann.add(Dense(1, activation= "sigmoid"))

ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])  
              
ann.summary()
ann.fit(x_train, y_train, epochs=10, batch_size=1)
pred=ann.predict(x_test)
y_pred1 = pred.reshape(-1)
y_pred1[y_pred1<0.5] = 0
y_pred1[y_pred1>=0.5] = 1
y_pred1 = y_pred1.astype('int')
result2=accuracy_score(y_test,y_pred1)*100
print(result2)
print()

print("<---------Classification Report ---------->")
print("*******************************************")
print(metrics.classification_report(y_test, y_pred1))
print()

print("Confusion Matrix")
print("****************")
 #calculate the confusion matrix
cf_matrix = confusion_matrix(y_test,y_pred1)
print(cf_matrix)
print()
print('Confusion matrix\n\n')
sns.heatmap(cf_matrix, annot=True)
plt.title("Confusion Matrix")
plt.show()          
print()

print("<-------Comparision Graph------->")
print("********************************")
    #Comparision Graph b/w two algo
vals=[result1,result2]
inds=range(len(vals))
labels=[" SVM","ANN"]
fig,ax = plt.subplots()
rects = ax.bar(inds, vals)
ax.set_xticks([ind for ind in inds])
ax.set_xticklabels(labels)
plt.title('Comparison graph')
plt.show()                

print("<------Prediction Status-------->")
print("*********************************")

if y_pred1[0]==0:
    print("Anomoly")
else:
    print("Normal")
print()






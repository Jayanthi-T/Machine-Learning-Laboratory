MACHINE LEARNING LABORATORY
1817119_JAYANTHI T
✫ EXP 8 : K-Nearest Neighbor Learning Algorithm
[ ]
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()
x = iris.data
y = iris.target
print("Iris Data set loaded..")
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
print("Dataset is split into training and testing...") 
print("Size of training data and its label", x_train.shape, y_train.shape)
print("Size of testing data and its label", x_test.shape, y_test.shape)
for i in range(len(iris.target_names)):
    print("Label", i, "-", str(iris.target_names[i]))
from sklearn.neighbors import KNeighborsClassifier as knn
classifier = knn(n_neighbors=1)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print("Results of Classification using K-nn with K=1")
for r in range(0,len(x_test)):
    print("Sample:", str(x_test[r]), "Actual-label:", str(y_test[r]), "Predicted-label:",
str(y_pred[r]))
print("Classification Accuracy:", classifier.score(x_test, y_test))
from sklearn.metrics import classification_report, confusion_matrix
print('Confusion Matrix')
print(confusion_matrix(y_test,y_pred))
print('Accuracy Metrics')
print(classification_report(y_test,y_pred))

Iris Data set loaded..
Dataset is split into training and testing...
Size of training data and its label (135, 4) (135,)
Size of testing data and its label (15, 4) (15,)
Label 0 - setosa
Label 1 - versicolor
Label 2 - virginica
Results of Classification using K-nn with K=1
Sample: [6.3 3.3 6.  2.5] Actual-label: 2 Predicted-label: 2
Sample: [4.5 2.3 1.3 0.3] Actual-label: 0 Predicted-label: 0
Sample: [7.9 3.8 6.4 2. ] Actual-label: 2 Predicted-label: 2
Sample: [5.6 2.7 4.2 1.3] Actual-label: 1 Predicted-label: 1
Sample: [5.  2.3 3.3 1. ] Actual-label: 1 Predicted-label: 1
Sample: [6.5 3.  5.8 2.2] Actual-label: 2 Predicted-label: 2
Sample: [6.4 3.2 4.5 1.5] Actual-label: 1 Predicted-label: 1
Sample: [5.  3.4 1.5 0.2] Actual-label: 0 Predicted-label: 0
Sample: [5.5 4.2 1.4 0.2] Actual-label: 0 Predicted-label: 0
Sample: [7.2 3.2 6.  1.8] Actual-label: 2 Predicted-label: 2
Sample: [4.9 2.4 3.3 1. ] Actual-label: 1 Predicted-label: 1
Sample: [5.1 3.3 1.7 0.5] Actual-label: 0 Predicted-label: 0
Sample: [6.2 2.2 4.5 1.5] Actual-label: 1 Predicted-label: 1
Sample: [6.  2.9 4.5 1.5] Actual-label: 1 Predicted-label: 1
Sample: [5.2 3.5 1.5 0.2] Actual-label: 0 Predicted-label: 0
Classification Accuracy: 1.0
Confusion Matrix
[[5 0 0]
 [0 6 0]
 [0 0 4]]
Accuracy Metrics
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         5
           1       1.00      1.00      1.00         6
           2       1.00      1.00      1.00         4

    accuracy                           1.00        15
   macro avg       1.00      1.00      1.00        15
weighted avg       1.00      1.00      1.00        15

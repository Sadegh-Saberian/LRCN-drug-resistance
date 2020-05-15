# importing necessary libraries
from sklearn import datasets
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import ROC_PR
from sklearn.multiclass import OneVsRestClassifier
import numpy as np

res = []

def svm(X, y, i):
    global res
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, shuffle=True)

    X = np.append(X_train, X_test, axis=0)
    y = np.append(y_train, y_test, axis=0)

    cvscores1 = []

    for i2 in range(0, 10):
        length = int(len(X) / 10)
        if i2 == 0:
            X_train = X[length:]
            X_test = X[0:length]
            y_train = y[length:]
            y_test = y[0:length]
        elif i2 != 9:
            X_train = np.append(X[0:length * i2], X[length * (i2 + 1):], axis=0)
            X_test = X[length * i2:length * (i2 + 1)]
            y_train = np.append(y[0:length * i2], y[length * (i2 + 1):], axis=0)
            y_test = y[length * i2:length * (i2 + 1)]
        else:
            X_train = X[0:length * i2]
            X_test = X[length * i2:]
            y_train = y[0:length * i2]
            y_test = y[length * i2:]

        from sklearn.svm import SVC
        svm_model_linear = SVC(kernel='linear', C=1).fit(X_train, y_train)
        score1 = ROC_PR.ROC_ML(svm_model_linear, X_test, y_test, "SVM", i2)
        accuracy = svm_model_linear.score(X_test, y_test)
        print(accuracy)
        res.append(accuracy)

        print("Area for 1")
        cvscores1.append(score1)

    f = open('result/SVMResult' + str(i) + '.txt', 'w')
    for ele in cvscores1:
        f.write(str(ele) + '\n')

    # training a linear SVM classifier


def lr(X, y, i):
    global res
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, shuffle=True)

    X = np.append(X_train, X_test, axis=0)
    y = np.append(y_train, y_test, axis=0)

    cvscores1 = []

    for i2 in range(0, 10):
        length = int(len(X) / 10)
        if i2 == 0:
            X_train = X[length:]
            X_test = X[0:length]
            y_train = y[length:]
            y_test = y[0:length]
        elif i2 != 9:
            X_train = np.append(X[0:length * i2], X[length * (i2 + 1):], axis=0)
            X_test = X[length * i2:length * (i2 + 1)]
            y_train = np.append(y[0:length * i2], y[length * (i2 + 1):], axis=0)
            y_test = y[length * i2:length * (i2 + 1)]
        else:
            X_train = X[0:length * i2]
            X_test = X[length * i2:]
            y_train = y[0:length * i2]
            y_test = y[length * i2:]

        from sklearn.linear_model import LogisticRegression
        lr_model_linear = LogisticRegression(C=1).fit(X_train, y_train)
        score1 = ROC_PR.ROC_ML(lr_model_linear, X_test, y_test, "LR", i)

        accuracy = lr_model_linear.score(X_test, y_test)
        print(accuracy)
        res.append(accuracy)

        print("Area for 1")
        cvscores1.append(score1)

    f = open('result/LRResult' + str(i) + '.txt', 'w')
    for ele in cvscores1:
        f.write(str(ele) + '\n')




def model_run(df_train, labels):
    # dividing X, y into train and test data
    global res
    # TODO check before run
    for i in range(0, len(labels)):
        print(i)
        res.append(i)
        print(res)
        dfCurrentDrug = labels[i]
        X = df_train.values.tolist()
        y = dfCurrentDrug.values.tolist()
        for i2 in range(len(y) - 1, -1, -1):
            if y[i2][0] != 0.0 and y[i2][0] != 1.0:
                del y[i2]
                del X[i2]
        svm(X, y, i)
        lr(X, y, i)
    f = open('result/mlResult.txt', 'w')
    for ele in res:
        f.write(str(ele) + '\n')
    f.close()


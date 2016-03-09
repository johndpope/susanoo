# coding: utf-8
import sys
import sklearn.svm
import pickle
import numpy as np
X, y = pickle.load(open(sys.argv[1], "rb"))
classifier = sklearn.svm.LinearSVC(C = 0.0001)
#classifier = sklearn.svm.SVC(C = 0.01)
classifier.fit(X, y)
pickle.dump(classifier, open(sys.argv[2], 'wb'))


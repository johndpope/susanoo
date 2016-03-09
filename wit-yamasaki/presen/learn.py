# coding: utf-8
import sys
import sklearn.svm
import pickle
import numpy as np
for key in ["horikita", "matsuko", "demon", "aina", "kanna"]:
    X, y = pickle.load(open("features_%s.data" % key, "rb"))
    classifier = sklearn.svm.LinearSVC(C = 0.0001)
    #classifier = sklearn.svm.SVC(C = 0.01)
    classifier.fit(X, y)
    pickle.dump(classifier, open("model_%s.data" % key, 'wb'))


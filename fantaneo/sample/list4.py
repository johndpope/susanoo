import sys
import pickle
# (1)
classifier = pickle.load(open(sys.argv[1]))
X, y = pickle.load(open(sys.argv[2]))
# (2)
y_predict = classifier.predict(X)
# (3)
correct = 0
for i in range(len(y)):
    if y[i] == y_predict[1]: correct += 1
    print('Accuracy: %f' % (float(correct) / len(y)))

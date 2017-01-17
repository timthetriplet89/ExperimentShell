from __future__ import division
from sklearn.model_selection import train_test_split
from sklearn import datasets
from decimal import getcontext, Decimal
import random
import HardCodedClassifier

iris = datasets.load_iris()

randomNum = random.randrange(99)

# train_test_split: http://scikit-learn.org/stable/modules/cross_validation.html
train_data, test_data, train_targets, test_targets = train_test_split(iris.data, iris.target, test_size=0.3, random_state=randomNum)

hardCodedClassifier = HardCodedClassifier.HardCodedClassifier()

hardCodedClassifier.fit(train_data,train_targets)

predictions = hardCodedClassifier.predict(test_targets)

countAccuratePredictions = 0

num_rows_test_data, num_cols = test_data.shape

for i in range(num_rows_test_data):
    if predictions[i] == test_targets[i]:
        countAccuratePredictions += 1

percentAccuracy = countAccuratePredictions / test_targets.size * 100

getcontext().prec = 2
print "%d%% Accuracy - %d accurate predictions out of %d items" % (percentAccuracy, countAccuratePredictions, test_targets.size)
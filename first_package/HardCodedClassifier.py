import numpy as np

class HardCodedClassifier(object):

    def __init__(self):
        pass

    def fit(self, train_data, train_targets):
        num_rows, num_cols = train_data.shape
        print("Training classifier on %d instances") % num_rows

    # This function needs to return an array with the same
    # number of entries as test_data.
    #
    # NEEDS TO BE TESTED
    #
    def predict(self, test_data):
        # num_rows, num_cols = test_data.shape            # This doesn't work and I don't know why
        # print "Classifying %d instances" % num_rows
        predictions = []
        for instance in test_data:
            predictions.append(0)
        return predictions

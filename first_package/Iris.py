
# Currently this class is not being used.

class Iris (object):

    # sepalLength = 0
    # sepalWidth  = 0
    # petalLength = 0
    # petalWidth  = 0
    # classification = ""

    def __init__(self, sepalLength, sepalWidth, petalLength, petalWidth, classification):
        self.sepalLength = sepalLength
        self.sepalWidth = sepalWidth
        self.petalLength = petalLength
        self.petalWidth = petalWidth
        self.classification = classification

    def getSepalLength(self):
        return self.sepalLength

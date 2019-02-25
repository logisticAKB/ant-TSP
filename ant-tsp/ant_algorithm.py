import numpy as np


class AntAlgorithm():
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def run(self):
        print(self.matrix)

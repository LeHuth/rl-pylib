import numpy as np
class graph:
    _id = -1
    _points = np.array()

    def __init__(self, points, id):
        self._points = points
        self._id = id
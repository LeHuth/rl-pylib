import numpy as np


class Graph:

    def __init__(self, points, uid, func, x, slope, b, lines):
        self._points = points
        self._uid = uid
        self._func = func
        self._x = x
        self._slope = slope
        self._b = b
        self._lines = lines

    def appendPoint(self, point):
        pass

    def getPoints(self):
        return self._points

    def getUID(self):
        return self._uid

    def getFunc(self):
        return self._func

    def getX(self):
        return self._x

    def getB(self):
        return self._b

    def getLines(self):
        return self._lines

    def setPoints(self, points):
        self._points = points

    def setUID(self, uid):
        self._uid = uid

    def setFunc(self, func):
        self._func = func



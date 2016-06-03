import Config as c


class Node:
    def __init__(self):
        self.backpath = []
        self.score = 0


class FancyNode:
    def __init__(self):
        self.backpaths = []


class Backpath:
    def __init__(self):
        self.score = 0
        self.properties = {}

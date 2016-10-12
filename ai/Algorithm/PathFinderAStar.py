"""
Class  cooperative A*
"""


class PathFinderAStar:
    node = 0

    def __init__(self, test):
        self.node = test

    def test(self):
        self.node = 4

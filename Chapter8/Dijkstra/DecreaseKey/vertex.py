class Vertex:

    def __init__(self, label: str, weight: int = float("inf"), key: int = None, index: int = None):
        self.label = label
        self.weight = weight
        self.key = key
        self.index = index



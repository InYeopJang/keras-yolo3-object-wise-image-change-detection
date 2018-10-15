class RectLabel:
    def __init__(self, label, xmin, ymin, xmax, ymax):
        self.label = label
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax


class ImageLabel:
    def __init__(self, path):
        self.path = path
        self.rectLabels = []

    def addRectLabel(self, label, xmin, ymin, xmax, ymax):
        self.rectLabels.append(RectLabel(label, xmin, ymin, xmax, ymax))
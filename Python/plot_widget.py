from collections import deque

import pyqtgraph as pg


class PlotWidget(pg.PlotWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.max_points = 300

        self.x = deque(maxlen=self.max_points)
        self.y = deque(maxlen=self.max_points)

        self.index = 0

        self._setup_plot()

    def _setup_plot(self):

        self.setBackground("w")

        self.showGrid(x=True, y=True)

        self.setLabel("left", "Position", units="°")
        self.setLabel("bottom", "Samples")

        self.setYRange(-360, 360)

        self.curve = self.plot(
            pen=pg.mkPen(color=(0, 100, 255), width=2)
        )

    def addPosition(self, position: float):

        self.x.append(self.index)
        self.y.append(position)

        self.index += 1

        self.curve.setData(self.x, self.y)

    def clearPlot(self):

        self.x.clear()
        self.y.clear()

        self.index = 0

        self.curve.clear()
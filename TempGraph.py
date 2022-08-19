import pyqtgraph as pg
from random import randint
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot


class Graph(PlotWidget):

    def __init__(self, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)

        self.x = list(range(10))
        self.y = [randint(10, 250) for _ in range(10)]

        self.setBackground('w')
        self.setTitle("Temperature History", color="b", size="20pt")

        styles = {"color": "#f00", "font-size": "20px"}
        self.setLabel("left", "Temperature (°C)", **styles)
        self.setLabel("bottom", "Seconds", **styles)

        self.setYRange(10, 250, padding=0)

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.plot(self.x, self.y, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]
        self.y.append(randint(10, 250))

        self.data_line.setData(self.x, self.y)

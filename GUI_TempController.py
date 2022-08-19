from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
from TempController_ui import Ui_TempCont
from TempGraph import Graph


class ControllerMain(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(ControllerMain, self).__init__(parent)
        self.ui = Ui_TempCont()
        self.ui.setupUi(self)
        self.setWindowTitle("Temperature Controller")


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = ControllerMain()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout

import sys
import matplotlib

matplotlib.use('Qt5Agg')

from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=8, height=7, dpi=300):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel("Tries number")
        self.axes.set_ylabel("Global price")
        self.axes.set_title("Graph showing the Global price at each try")
        super(MplCanvas, self).__init__(fig)


class GraphPopUp(QWidget):

    def __init__(self, x , y):
        super(GraphPopUp, self).__init__()

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot(x, y,**{'marker': 'o'})
        vbox = QVBoxLayout()
        vbox.addWidget(self.sc)
        self.setLayout(vbox)

        self.show()






"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GraphPopUp([1,2,3,4],[12,13,14,15])
    app.exec_()
"""


















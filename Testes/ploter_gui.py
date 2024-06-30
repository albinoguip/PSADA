from PySide6 import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.fft_frame = FftFrame(self)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.fft_frame)
        self.setLayout(self.layout)
        self.setCentralWidget(self.fft_frame)

class FftFrame(QtGui.QFrame):
    def __init__(self, parent=None):
        super(FftFrame, self).__init__(parent)
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.parent = parent
        self.graph_view = GraphView('fftFrame', 'FFT Transform:', 'FFT Transform of Signal', self)

    def resizeEvent(self, event):
        self.graph_view.setGeometry(self.rect())


class GraphView(QtGui.QWidget):
    def __init__(self, name, title, graph_title, parent = None):
        super(GraphView, self).__init__(parent)

        self.name = name
        self.graph_title = graph_title

        self.dpi = 100
        self.fig = Figure((5.0, 3.0), dpi = self.dpi, facecolor = (1,1,1), edgecolor = (0,0,0))
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        self.Title = QtGui.QLabel(self)
        self.Title.setText(title)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.Title)
        self.layout.addWidget(self.canvas)
        self.layout.setStretchFactor(self.canvas, 1)
        self.setLayout(self.layout)
        self.canvas.show()

    def update_graph(self, data, title = None):
        self.axes.clear()
        self.axes.plot(data)
        if title != None:
            self.axes.set_title(title)

        self.canvas.draw()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
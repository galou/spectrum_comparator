from PyQt5 import Qt

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SpectraFigureCanvas(FigureCanvas):
    def __init__(self, parent, spectrum1, spectrum2):
        self.spectrum1 = spectrum1
        self.spectrum2 = spectrum2
        fig = plt.Figure()
        self.axes = fig.add_subplot(1, 1, 1)

        self.compute_initial_figure()

        super().__init__(fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   Qt.QSizePolicy.Expanding,
                                   Qt.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        self.axes.plot(self.spectrum1.mass_values, label=self.spectrum1.name)
        self.axes.plot(self.spectrum2.mass_values, label=self.spectrum2.name)
        self.axes.legend()
        self.axes.grid(True)

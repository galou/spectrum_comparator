# -*- coding: utf-8 -*-

from PyQt5 import Qt

from spectrum import Spectrum
from figure_canvas import SpectraFigureCanvas

# Load from ui
# from PyQt5 import uic
# form_class = uic.loadUiType('spectrum_comparator.ui')[0]
# or use the generated file
from spectrum_comparator_ui import Ui_MainWindow as form_class


class Window(Qt.QMainWindow, form_class):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.spectrums = []
        self.spectrum1 = None
        self.spectrum2 = None
        self.fig_canvas = None

        # Setup callbacks.
        self.action_load_spectrum.triggered.connect(self.load_spectrum_callback)
        self.action_quit.triggered.connect(self.quit_callback)
        self.comboBoxSpectrumChoice1.currentIndexChanged.connect(
            self.spectrum_choice1_callback)
        self.comboBoxSpectrumChoice2.currentIndexChanged.connect(
            self.spectrum_choice2_callback)

    def load_spectrum_callback(self):
        filenames, _ = Qt.QFileDialog.getOpenFileNames(self, 'Open spectrum(s)',
                                                       filter='*.scn')
        for filename in filenames:
            spectrum = Spectrum(filename)
            self.spectrums.append(spectrum)
            self.comboBoxSpectrumChoice1.addItem(spectrum.name, spectrum)
            self.comboBoxSpectrumChoice2.addItem(spectrum.name, spectrum)

    def quit_callback(self):
        self.close()

    def spectrum_choice1_callback(self, index):
        self.spectrum1 = self.comboBoxSpectrumChoice1.itemData(index)
        self.update_plot()

    def spectrum_choice2_callback(self, index):
        self.spectrum2 = self.comboBoxSpectrumChoice2.itemData(index)
        self.update_plot()

    def update_plot(self):
        if self.spectrum1 and self.spectrum2:
            if self.fig_canvas:
                self.layout_widget_comp.removeWidget(self.fig_canvas)
                # self.layout_widget_comp.removeItem(1)
            self.fig_canvas = SpectraFigureCanvas(self.widget_comp,
                                                  self.spectrum1,
                                                  self.spectrum2)
            self.layout_widget_comp.addWidget(self.fig_canvas)

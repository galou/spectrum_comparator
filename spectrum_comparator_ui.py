# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrum_comparator.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tab_widget.setObjectName("main_tab_widget")
        self.tab_comp = QtWidgets.QWidget()
        self.tab_comp.setObjectName("tab_comp")
        self.layout_tab_comp = QtWidgets.QHBoxLayout(self.tab_comp)
        self.layout_tab_comp.setObjectName("layout_tab_comp")
        self.widget_comp = QtWidgets.QWidget(self.tab_comp)
        self.widget_comp.setObjectName("widget_comp")
        self.layout_widget_comp = QtWidgets.QVBoxLayout(self.widget_comp)
        self.layout_widget_comp.setContentsMargins(0, 0, 0, 0)
        self.layout_widget_comp.setObjectName("layout_widget_comp")
        self.widget_spectrum_choice = QtWidgets.QWidget(self.widget_comp)
        self.widget_spectrum_choice.setObjectName("widget_spectrum_choice")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_spectrum_choice)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBoxSpectrumChoice1 = QtWidgets.QComboBox(self.widget_spectrum_choice)
        self.comboBoxSpectrumChoice1.setObjectName("comboBoxSpectrumChoice1")
        self.horizontalLayout.addWidget(self.comboBoxSpectrumChoice1)
        self.comboBoxSpectrumChoice2 = QtWidgets.QComboBox(self.widget_spectrum_choice)
        self.comboBoxSpectrumChoice2.setObjectName("comboBoxSpectrumChoice2")
        self.horizontalLayout.addWidget(self.comboBoxSpectrumChoice2)
        self.layout_widget_comp.addWidget(self.widget_spectrum_choice)
        self.layout_tab_comp.addWidget(self.widget_comp)
        self.main_tab_widget.addTab(self.tab_comp, "")
        self.verticalLayout.addWidget(self.main_tab_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_load_spectrum = QtWidgets.QAction(MainWindow)
        self.action_load_spectrum.setObjectName("action_load_spectrum")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.menu_file.addAction(self.action_load_spectrum)
        self.menu_file.addAction(self.action_quit)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_comp), _translate("MainWindow", "Comparison"))
        self.menu_file.setTitle(_translate("MainWindow", "&File"))
        self.action_load_spectrum.setText(_translate("MainWindow", "L&oad spectrum"))
        self.action_load_spectrum.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_quit.setText(_translate("MainWindow", "&Quit"))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


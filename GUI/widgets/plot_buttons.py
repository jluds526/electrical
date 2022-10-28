from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PlotButtons(QWidget):
    def __init__(self, plot):
        super(PlotButtons, self).__init__(None)
        self.plot = plot
        self.plot_reset = False
        self.rescale_axes = False
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        # Reset plot button
        self.reset_plot_button = QPushButton(self)
        self.reset_plot_button.setText("Reset Plot")
        self.reset_plot_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.reset_plot_button.clicked.connect(self.resetPlot)

        self.example_button = QPushButton(self)
        self.example_button.setText("Example Button")
        self.example_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        # Add the widget for resizing the plot axes
        resize_input_widgets = QSplitter(Qt.Vertical)
        row1 = QSplitter(Qt.Horizontal)
        row2 = QSplitter(Qt.Horizontal)
        row3 = QSplitter(Qt.Horizontal)

        self.textbox1 = QLineEdit(self)
        self.textbox1.resize(100,100)
        self.textbox1.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.textbox2 = QLineEdit(self)
        self.textbox2.resize(100,100)
        self.textbox2.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.textbox3 = QLineEdit(self)
        self.textbox3.resize(100,100)
        self.textbox3.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.textbox4 = QLineEdit(self)
        self.textbox4.resize(100,100)
        self.textbox4.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.rescale_axes_button = QPushButton(self)
        self.rescale_axes_button.setText("Rescale Axes")
        self.rescale_axes_button.setStyleSheet("font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.rescale_axes_button.clicked.connect(self.rescaleAxes)

        row1.addWidget(self.textbox1)
        row1.addWidget(self.textbox2)
        row2.addWidget(self.textbox3)
        row2.addWidget(self.textbox4)
        row3.addWidget(self.rescale_axes_button)

        resize_input_widgets.addWidget(row1)
        resize_input_widgets.addWidget(row2)
        resize_input_widgets.addWidget(row3)

        hbox.addWidget(self.reset_plot_button)
        hbox.addWidget(self.example_button)
        hbox.addWidget(resize_input_widgets)
        self.setLayout(hbox)

    def resetPlot(self):
        self.plot.clear()
        self.plot_reset = True
    
    def setPlotResetFlag(self, flag):
        self.plot_reset = flag
    
    def getPlotResetFlag(self):
        return self.plot_reset
    
    def rescaleAxes(self):
        self.x_min = int(self.textbox1.text())
        self.x_max = int(self.textbox2.text())
        self.y_min = int(self.textbox3.text())
        self.y_max = int(self.textbox4.text())
        self.rescale_axes = True

    def getRescaleAxesFlag(self):
        return self.rescale_axes
    
    def setRescaleAxesFlag(self, flag):
        self.rescale_axes = flag
    
    def getXAxesLimits(self):
        return [self.x_min, self.x_max]
    
    def getYAxesLimits(self):
        return [self.y_min, self.y_max]

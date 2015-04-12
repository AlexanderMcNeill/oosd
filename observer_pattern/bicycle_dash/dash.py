__author__ = 'alexmcneill'

import sys
from PyQt4 import QtCore, QtGui, uic
import bicycle
import caloriemeter
import speedometer

qtCreatorFile = "dashboard.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class DashApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.bike = bicycle.Bicycle()
        self.calories = caloriemeter.CalorieMeter(self.bike)
        self.speedo = speedometer.Speedometer(self.bike)
        self.rpm_input.editingFinished.connect(self.update_meters)

    def update_meters(self):
        new_rpms = int(self.rpm_input.text())
        self.bike.rpms = new_rpms

        self.bike.update_observers()
        self.kph_display.setText(str(self.speedo.speed))
        self.calories_display.setText(str(self.calories.calories))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = DashApp()
    window.show()
    sys.exit(app.exec_())

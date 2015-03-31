__author__ = 'alexmcneill'

import sys
from PyQt4 import QtCore, QtGui, uic


qtCreatorFile = "bicycle_dash.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class BicycleApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = BicycleApp()
    window.show()
    sys.exit(app.exec_())
# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        QtWidgets.QMainWindow.setWindowTitle(self, "iStats: iMessage Statistics")
        QtWidgets.QMainWindow.setMinimumSize(self, 900, 500)

        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

from lab.app import main
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from rounded_image_widget import RoundedImageWidget
import icon_rc

from fns import *
import os
import random


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/lab.ui")
        uic.loadUi(ui_path, self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainUi()
    main_window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
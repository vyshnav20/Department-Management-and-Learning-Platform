# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Editsub(object):
    def setupUi(self, Editsub):
        Editsub.setObjectName("Editsub")
        Editsub.resize(1500, 594)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/mainicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Editsub.setWindowIcon(icon)
        Editsub.setStyleSheet("#Editsub { background-color: #333333;}\n"
"\n"
"QPushButton {\n"
"border: 2px solid transparent; \n"
"border-radius: 10px;\n"
"background-color: rgba(0, 0, 0, 0.5);\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);\n"
"}\n"
"QPushButton:hover {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);\n"
"color: black;\n"
"border: 2px solid transparent; \n"
"border-color: black; \n"
"}\n"
"\n"
"\n"
"\n"
"QLabel {color: white;}\n"
"\n"
"#Box,#scrollAreaWidgetContents{ background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);\n"
" border-radius: 15px;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #555555;\n"
"    padding: 20px;}\n"
"\n"
"QLineEdit,QPlainTextEdit,QComboBox,QDateEdit{\n"
"    background-color: #333333; /* Dark background */\n"
"    color: #CCCCCC; /* Light gray text */\n"
"    border: 1px solid #555555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #333333; /* Dark background */\n"
"    color: #FFFFFF; /* White text */\n"
"    border: 1px solid #29a19c;\n"
"    selection-background-color: #29a19c;\n"
"    selection-color: #1e1e1e;\n"
"}\n"
"\n"
"QCalendarWidget {\n"
"    background-color: #333333; /* Dark background */\n"
"    color: #CCCCCC; /* Light gray text */\n"
"    border: 1px solid #555555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-family: \'Dungeon\'; \n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* Navigation buttons */\n"
"QCalendarWidget QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black background */\n"
"    color: white;\n"
"    border: none;\n"
"    height: 25px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"    border: 1px solid transparent;\n"
"    border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71); /* Gradient background */\n"
"    color: black;\n"
"    border: 1px solid transparent;\n"
"    border-color: black;\n"
"}\n"
"\n"
"/* Month and year navigation buttons */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #333333; /* Match the main background */\n"
"    border: none;\n"
"}\n"
"\n"
"/* Day of the week header */\n"
"QCalendarWidget QTableView QHeaderView::section {\n"
"    background-color: #555555;\n"
"    color: #CCCCCC;\n"
"    border: 1px solid #555555;\n"
"   font-family: \'Dungeon\'; \n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* Selected date */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    font-size: 12px; /* Font size of the dates */\n"
"    color: #CCCCCC; /* Text color of the dates */\n"
"    selection-background-color: #29a19c; /* Selected date background */\n"
"    selection-color: #1e1e1e; /* Selected date text color */\n"
"   font-family: \'Dungeon\'; \n"
"    font-size: 14px; \n"
"}\n"
"\n"
"/* General dates */\n"
"QCalendarWidget QTableView {\n"
"    background-color: #333333;\n"
"    border: 1px solid #555555;\n"
"    alternate-background-color: #3b3b3b;\n"
"     font-family: \'Dungeon\'; \n"
"    font-size: 14px;  \n"
"}\n"
"\n"
"/* The month view navigation buttons (left, right, month, year) */\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::down-arrow {\n"
"    image: none;\n"
"}\n"
"\n"
"/* Year and month selector */\n"
"QCalendarWidget QSpinBox {\n"
"    background-color: #333333; /* Match the main background */\n"
"    color: #CCCCCC; /* Light gray text */\n"
"    border: 1px solid #555555;\n"
"    font-family: \'Dungeon\'; \n"
"    font-size: 14px;  \n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
"    background-color: #333333;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button:hover, QCalendarWidget QSpinBox::down-button:hover {\n"
"    background-color: #29a19c;\n"
"}\n"
"\n"
"/* Menu for month selection */\n"
"QCalendarWidget QMenu {\n"
"    background-color: #333333; /* Dark background */\n"
"    color: #CCCCCC; /* Light gray text */\n"
"    border: 1px solid #555555;\n"
"    font-family: \'Dungeon\'; \n"
"    font-size: 14px; \n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Editsub)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(Editsub)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 65))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 75))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Dungeon")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.Box = QtWidgets.QWidget(Editsub)
        self.Box.setObjectName("Box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.Box)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(157, 45))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setMinimumSize(QtCore.QSize(132, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setMinimumSize(QtCore.QSize(196, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setMinimumSize(QtCore.QSize(550, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addWidget(self.widget_4)
        self.scrollArea = QtWidgets.QScrollArea(self.Box)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1462, 149))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.Box)
        self.widget_3 = QtWidgets.QWidget(Editsub)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Exit = QtWidgets.QPushButton(self.widget_3)
        self.Exit.setMaximumSize(QtCore.QSize(117, 16777215))
        self.Exit.setObjectName("Exit")
        self.horizontalLayout_2.addWidget(self.Exit)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget_3)
        self.buttonBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_2.addWidget(self.widget_3)

        self.retranslateUi(Editsub)
        QtCore.QMetaObject.connectSlotsByName(Editsub)

    def retranslateUi(self, Editsub):
        _translate = QtCore.QCoreApplication.translate
        Editsub.setWindowTitle(_translate("Editsub", "New Question"))
        Editsub.setWhatsThis(_translate("Editsub", "Add a question for a particular Subject"))
        self.label_5.setText(_translate("Editsub", "COMPILATION"))
        self.label_2.setText(_translate("Editsub", "Test Cases"))
        self.label_4.setText(_translate("Editsub", "Input"))
        self.label_7.setText(_translate("Editsub", "Expected Result"))
        self.label_8.setText(_translate("Editsub", "Your Output"))
        self.Exit.setText(_translate("Editsub", "Exit"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editsub = QtWidgets.QDialog()
    ui = Ui_Editsub()
    ui.setupUi(Editsub)
    Editsub.show()
    sys.exit(app.exec_())
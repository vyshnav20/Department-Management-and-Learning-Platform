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


class forgotpass(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/fp.ui")
        uic.loadUi(ui_path,self)


class submit_test(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/sub_test.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

class edit_sub(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/editsub.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)


class addexam(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/newsub.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)



class viewqns(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/viewqn.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)


    def update(self):
        self.popup=updtdialogbox()
        if self.popup.exec_() == QtWidgets.QDialog.Accepted:
            q=[]
            q.append(self.lineEdit_2.text())
            q.append(self.lineEdit_3.text())
            q.append(self.plainTextEdit.toPlainText())
            q.append(self.lineEdit.text())
            updt_qn(q)
            self.close()

class newqns(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/newqns.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

    def newq(self):
        q=[]
        q.append(self.comboBox_2.currentText())
        q.append(self.comboBox_3.currentText())
        q.append(self.plainTextEdit.toPlainText())
        q.append(self.lineEdit.text())
        add_qn(q)
        self.close()

class updtdialogbox(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/updatedialog.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

class deldialogbox(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/deldialog.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)

class dialogbox(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/dialogbox.ui")
        uic.loadUi(ui_path,self)
        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, 'buttonBox')

        # Check if the button box is found
        if self.buttonBox is None:
            print("Error: ButtonBox not found. Please check the object name in the UI file.")
        else:
            # Connect the button box signals to the appropriate slots
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)


class labs(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1941, 985)
        MainWindow.setMinimumSize(QSize(0, 400))
        icon = QIcon()
        icon.addFile(u":/icons/mainicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#centralwidget {background-color: #333333;}\n"
"#Sub1, #menu, #q1_header, #q2_header,#new_2,#new_3,#container_3,#new_4,#name_widget{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #292929, stop: 1 #1a1a1a);\n"
"color: #FFFFFF;\n"
"border: 1px solid #555555;}\n"
"#qn_1, #qn_2 {\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #444444, stop: 1 #333333);\n"
"color: #CCCCCC;\n"
"border: 1px solid #555555;\n"
"}\n"
"#container_4\n"
"{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);\n"
"border-radius: 15px;\n"
"}\n"
"QScrollArea {\n"
"border-radius: 20px;\n"
"border: 1px solid #555555;\n"
" }\n"
"QScrollArea > QWidget > QWidget {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton {\n"
"border: 2px solid transparent; \n"
"border-radius: 10px;\n"
""
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
"QLabel {\n"
"color: #CCCCCC;}\n"
"QPlainTextEdit {\n"
"background-color: #333333;\n"
"color: #CCCCCC;\n"
"border: 1px solid #555555;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"}\n"
"QComboBox {\n"
"background-color: #333333;\n"
"color: #CCCCCC;\n"
"border: 1px solid #555555;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"background-color: #333333; \n"
"color: #FFFFFF; \n"
"border: 1px solid #29a19c;\n"
"selection-background-color: #29a19c;\n"
"selection-color: #1e1e1e;\n"
"}\n"
"QTabWidget::pane {"
                        "\n"
"border-radius: 15px;\n"
"border: 1px solid #555555;\n"
"}\n"
"QTabBar::tab {\n"
"border: 2px solid transparent; \n"
"border-radius: 10px;\n"
"background-color: rgba(0, 0, 0, 0.5);\n"
"padding: 10px 20px;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);\n"
"}\n"
"QTabBar::tab:hover {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);\n"
"color: black;\n"
"border: 2px solid transparent; \n"
"border-color: red;\n"
" }\n"
"QTabBar::tab:selected {\n"
"background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2980b9, stop: 0.3 #3498db, stop: 1 #2ecc71);\n"
"color: black;\n"
"border: 2px solid transparent; \n"
"border-color: black;\n"
" }\n"
"\n"
"#stud_home,#stud_profile\n"
"{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop:"
                        " 1 #2e3f50);\n"
"color: #FFFFFF;\n"
"border: 1px solid #555555;\n"
"padding: 20px;}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_24 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.Sub1 = QWidget(self.centralwidget)
        self.Sub1.setObjectName(u"Sub1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sub1.sizePolicy().hasHeightForWidth())
        self.Sub1.setSizePolicy(sizePolicy)
        self.Sub1.setMinimumSize(QSize(0, 0))
        self.Sub1.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.Sub1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sem = QLabel(self.Sub1)
        self.sem.setObjectName(u"sem")
        self.sem.setMaximumSize(QSize(135, 16777215))
        font = QFont()
        font.setFamily(u"Orbitron")
        font.setPointSize(14)
        self.sem.setFont(font)

        self.horizontalLayout.addWidget(self.sem)
        self.sub_2 = QLabel(self.Sub1)
        self.sub_2.setObjectName(u"sub_2")
        self.sub_2.setMaximumSize(QSize(550, 16777215))
        font1 = QFont()
        font1.setFamily(u"Orbitron")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.sub_2.setFont(font1)
        self.sub_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.sub_2)

        self.sub_3 = QLabel(self.Sub1)
        self.sub_3.setObjectName(u"sub_3")
        self.sub_3.setMaximumSize(QSize(550, 16777215))
        self.sub_3.setFont(font1)
        self.sub_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.sub_3)
        self.sub = QLabel(self.Sub1)
        self.sub.setObjectName(u"sub")
        font1 = QFont()
        font1.setFamily(u"Orbitron")
        font1.setPointSize(14)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.sub.setFont(font1)
        self.sub.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.sub)


        self.verticalLayout_24.addWidget(self.Sub1)

        self.container1 = QWidget(self.centralwidget)
        self.container1.setObjectName(u"container1")
        self.horizontalLayout_2 = QHBoxLayout(self.container1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.menu = QWidget(self.container1)
        self.menu.setObjectName(u"menu")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.menu.setFont(font2)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Roll = QWidget(self.menu)
        self.Roll.setObjectName(u"Roll")
        self.Roll.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.Roll)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.roll_label = QLabel(self.Roll)
        self.roll_label.setObjectName(u"roll_label")
        self.roll_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.roll_label)

        self.roll = QLabel(self.Roll)
        self.roll.setObjectName(u"roll")
        font3 = QFont()
        font3.setFamily(u"Digital-7 Mono")
        font3.setPointSize(20)
        self.roll.setFont(font3)

        self.horizontalLayout_3.addWidget(self.roll)


        self.verticalLayout_2.addWidget(self.Roll)

        self.q1 = QPushButton(self.menu)
        self.q1.setObjectName(u"q1")
        font4 = QFont()
        font4.setFamily(u"Orbitron")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.q1.setFont(font4)

        self.verticalLayout_2.addWidget(self.q1)

        self.q2 = QPushButton(self.menu)
        self.q2.setObjectName(u"q2")
        self.q2.setFont(font4)

        self.verticalLayout_2.addWidget(self.q2)
        self.q2_3 = QPushButton(self.menu)
        self.q2_3.setObjectName(u"q2_3")
        self.q2_3.setFont(font4)

        self.verticalLayout_2.addWidget(self.q2_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.submit = QPushButton(self.menu)
        self.submit.setObjectName(u"submit")
        self.submit.setFont(font4)

        self.verticalLayout_2.addWidget(self.submit)

        self.logout = QPushButton(self.menu)
        self.logout.setObjectName(u"logout")
        self.logout.setFont(font4)

        self.verticalLayout_2.addWidget(self.logout)


        self.horizontalLayout_2.addWidget(self.menu)

        self.Qns = QWidget(self.container1)
        self.Qns.setObjectName(u"Qns")
        self.horizontalLayout_4 = QHBoxLayout(self.Qns)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.stackedWidget = QStackedWidget(self.Qns)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.q1_page = QWidget()
        self.q1_page.setObjectName(u"q1_page")
        self.verticalLayout_15 = QVBoxLayout(self.q1_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.q1_header = QWidget(self.q1_page)
        self.q1_header.setObjectName(u"q1_header")
        self.q1_header.setMinimumSize(QSize(0, 50))
        self.q1_header.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_17 = QHBoxLayout(self.q1_header)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.q2_title_2 = QLabel(self.q1_header)
        self.q2_title_2.setObjectName(u"q2_title_2")
        font5 = QFont()
        font5.setFamily(u"Orbitron")
        font5.setPointSize(20)
        self.q2_title_2.setFont(font5)
        self.q2_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.q2_title_2)


        self.verticalLayout_15.addWidget(self.q1_header)

        self.qn_1 = QWidget(self.q1_page)
        self.qn_1.setObjectName(u"qn_1")
        self.verticalLayout_13 = QVBoxLayout(self.qn_1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_6 = QWidget(self.qn_1)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 1, 0, 1)
        self.plainTextEdit_2 = QPlainTextEdit(self.widget_6)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        font6 = QFont()
        font6.setFamily(u"Agency FB")
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setWeight(75)
        self.plainTextEdit_2.setFont(font6)
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.plainTextEdit_2)


        self.verticalLayout_13.addWidget(self.widget_6)

        self.widget_13 = QWidget(self.qn_1)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_3 = QLabel(self.widget_13)
        self.label_3.setObjectName(u"label_3")
        font7 = QFont()
        font7.setFamily(u"Orbitron")
        font7.setPointSize(16)
        self.label_3.setFont(font7)

        self.horizontalLayout_15.addWidget(self.label_3)

        self.label_8 = QLabel(self.widget_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_8)

        self.comboBox_4 = QComboBox(self.widget_13)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 35))
        self.comboBox_4.setMaximumSize(QSize(175, 16777215))
        font8 = QFont()
        font8.setFamily(u"Orbitron")
        font8.setPointSize(12)
        self.comboBox_4.setFont(font8)

        self.horizontalLayout_15.addWidget(self.comboBox_4)


        self.verticalLayout_13.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.qn_1)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.plainTextEdit_4 = QPlainTextEdit(self.widget_14)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        font9 = QFont()
        font9.setFamily(u"Agency FB")
        font9.setPointSize(18)
        self.plainTextEdit_4.setFont(font9)

        self.horizontalLayout_5.addWidget(self.plainTextEdit_4)


        self.verticalLayout_13.addWidget(self.widget_14)


        self.verticalLayout_15.addWidget(self.qn_1)

        self.stackedWidget.addWidget(self.q1_page)
        self.q2_page = QWidget()
        self.q2_page.setObjectName(u"q2_page")
        self.verticalLayout_12 = QVBoxLayout(self.q2_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.q2_header = QWidget(self.q2_page)
        self.q2_header.setObjectName(u"q2_header")
        self.q2_header.setMinimumSize(QSize(0, 50))
        self.q2_header.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_16 = QHBoxLayout(self.q2_header)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.q2_title = QLabel(self.q2_header)
        self.q2_title.setObjectName(u"q2_title")
        self.q2_title.setFont(font5)
        self.q2_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.q2_title)


        self.verticalLayout_12.addWidget(self.q2_header)

        self.qn_2 = QWidget(self.q2_page)
        self.qn_2.setObjectName(u"qn_2")
        self.verticalLayout_10 = QVBoxLayout(self.qn_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_2 = QWidget(self.qn_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_11 = QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 1, 0, 1)
        self.plainTextEdit = QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFont(font6)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.plainTextEdit)


        self.verticalLayout_10.addWidget(self.widget_2)

        self.widget = QWidget(self.qn_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font7)

        self.horizontalLayout_14.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font7)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 35))
        self.comboBox.setMaximumSize(QSize(175, 16777215))
        self.comboBox.setFont(font8)

        self.horizontalLayout_14.addWidget(self.comboBox)


        self.verticalLayout_10.addWidget(self.widget)

        self.widget_5 = QWidget(self.qn_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEdit_3 = QPlainTextEdit(self.widget_5)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        font10 = QFont()
        font10.setFamily(u"Agency FB")
        font10.setPointSize(18)
        font10.setBold(False)
        font10.setWeight(50)
        self.plainTextEdit_3.setFont(font10)

        self.verticalLayout_3.addWidget(self.plainTextEdit_3)


        self.verticalLayout_10.addWidget(self.widget_5)


        self.verticalLayout_12.addWidget(self.qn_2)

        self.stackedWidget.addWidget(self.q2_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_page.setStyleSheet(u"#Box {\n"
"    border-radius: 15px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #555555;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: #3A3A3A; /* Dark Grey */\n"
"    color: #FFFFFF;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #1C1C1C; /* Light Grey */\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.login_page)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.container = QFrame(self.login_page)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.container)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(450, 175, 450, 350)
        self.Box = QFrame(self.container)
        self.Box.setObjectName(u"Box")
        self.Box.setFrameShape(QFrame.StyledPanel)
        self.Box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.Box)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 75))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font11 = QFont()
        font11.setFamily(u"Dungeon")
        font11.setPointSize(25)
        self.label_4.setFont(font11)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(7)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(112, 40, 145, -1)
        self.username = QLabel(self.Box)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(190, 0))
        self.username.setMaximumSize(QSize(150, 16777215))
        font12 = QFont()
        font12.setFamily(u"Orbitron")
        font12.setPointSize(18)
        font12.setKerning(True)
        self.username.setFont(font12)
        self.username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.username)

        self.username_edit = QLineEdit(self.Box)
        self.username_edit.setObjectName(u"username_edit")
        self.username_edit.setFont(font9)
        self.username_edit.setEchoMode(QLineEdit.Normal)
        self.username_edit.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_edit)

        self.password = QLabel(self.Box)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(190, 0))
        self.password.setMaximumSize(QSize(150, 16777215))
        font13 = QFont()
        font13.setFamily(u"Orbitron")
        font13.setPointSize(18)
        self.password.setFont(font13)
        self.password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.password)

        self.password_edit = QLineEdit(self.Box)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setFont(font9)
        self.password_edit.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_edit)

        self.fp = QPushButton(self.Box)
        self.fp.setObjectName(u"fp")
        font14 = QFont()
        font14.setFamily(u"Orbitron")
        self.fp.setFont(font14)
        self.fp.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.fp)

        self.login = QPushButton(self.Box)
        self.login.setObjectName(u"login")
        self.login.setFont(font14)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.login)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.incp = QLabel(self.Box)
        self.incp.setObjectName(u"incp")
        font15 = QFont()
        font15.setFamily(u"Orbitron")
        font15.setPointSize(12)
        font15.setBold(True)
        font15.setWeight(75)
        self.incp.setFont(font15)
        self.incp.setStyleSheet(u"*{color:red}")

        self.verticalLayout_4.addWidget(self.incp)


        self.horizontalLayout_6.addWidget(self.Box)


        self.verticalLayout_6.addWidget(self.container)

        self.stackedWidget.addWidget(self.login_page)

        
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: #3A3A3A; /* Dark Grey */\n"
"    color: #FFFFFF;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: #1C1C1C; /* Light Grey */\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.container_3 = QFrame(self.page)
        self.container_3.setObjectName(u"container_3")
        self.container_3.setFrameShape(QFrame.StyledPanel)
        self.container_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.container_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.tabWidget = QTabWidget(self.container_3)
        self.tabWidget.setObjectName(u"tabWidget")
        font16 = QFont()
        font16.setFamily(u"Dungeon")
        font16.setPointSize(15)
        self.tabWidget.setFont(font16)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tr_page = QWidget()
        self.tr_page.setObjectName(u"tr_page")
        self.verticalLayout = QVBoxLayout(self.tr_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.container_2 = QFrame(self.tr_page)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setFrameShape(QFrame.StyledPanel)
        self.container_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.container_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.widget_3 = QWidget(self.container_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 680))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollarea = QWidget()
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setGeometry(QRect(0, 0, 1661, 661))
        self.scrollarea.setStyleSheet(u"")
        self.horizontalLayout_67 = QHBoxLayout(self.scrollarea)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.Box_2 = QFrame(self.scrollarea)
        self.Box_2.setObjectName(u"Box_2")
        sizePolicy.setHeightForWidth(self.Box_2.sizePolicy().hasHeightForWidth())
        self.Box_2.setSizePolicy(sizePolicy)
        self.Box_2.setFrameShape(QFrame.StyledPanel)
        self.Box_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Box_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        css = """
    #qn_list {
        border-radius: 15px;
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #292929, stop: 1 #1a1a1a
        );
        color: #FFFFFF;
        border: 1px solid #555555;
    }
    """
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.generate_qn_lists(css, sizePolicy)    


        self.horizontalLayout_67.addWidget(self.Box_2, 0, Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollarea)

        self.horizontalLayout_13.addWidget(self.scrollArea)

        self.verticalLayout_21.addWidget(self.widget_3)

        self.new_2 = QWidget(self.container_2)
        self.new_2.setObjectName(u"new_2")
        self.new_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_19 = QHBoxLayout(self.new_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(500, -1, 500, -1)
        self.newqns = QPushButton(self.new_2)
        self.newqns.setObjectName(u"newqns")
        self.newqns.setMaximumSize(QSize(75, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newqns.setIcon(icon1)
        self.newqns.setIconSize(QSize(44, 31))

        self.horizontalLayout_19.addWidget(self.newqns)


        self.verticalLayout_21.addWidget(self.new_2)


        self.verticalLayout.addWidget(self.container_2)

        self.tabWidget.addTab(self.tr_page, "")
        self.subj = QWidget()
        self.subj.setObjectName(u"subj")
        self.verticalLayout_8 = QVBoxLayout(self.subj)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.container_4 = QWidget(self.subj)
        self.container_4.setObjectName(u"container_4")
        self.verticalLayout_9 = QVBoxLayout(self.container_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_8 = QWidget(self.container_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 800))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Box_4 = QFrame(self.widget_8)
        self.Box_4.setObjectName(u"Box_4")
        sizePolicy.setHeightForWidth(self.Box_4.sizePolicy().hasHeightForWidth())
        self.Box_4.setSizePolicy(sizePolicy)
        self.Box_4.setFrameShape(QFrame.StyledPanel)
        self.Box_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.Box_4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        css = """
    #sub_list{
        border-radius: 15px;
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #292929, stop: 1 #1a1a1a
        );
        color: #FFFFFF;
        border: 1px solid #555555;
    }
    """
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.generate_sub_lists(css, sizePolicy)        


        self.horizontalLayout_23.addWidget(self.Box_4, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.widget_8)

        self.new_4 = QWidget(self.container_4)
        self.new_4.setObjectName(u"new_4")
        self.new_4.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_25 = QHBoxLayout(self.new_4)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(500, -1, 500, -1)
        self.new_sub = QPushButton(self.new_4)
        self.new_sub.setObjectName(u"new_sub")
        self.new_sub.setMaximumSize(QSize(75, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_sub.setIcon(icon1)
        self.new_sub.setIconSize(QSize(44, 31))

        self.horizontalLayout_25.addWidget(self.new_sub)


        self.verticalLayout_9.addWidget(self.new_4)


        self.verticalLayout_8.addWidget(self.container_4)

        self.tabWidget.addTab(self.subj, "")

        self.verticalLayout_17.addWidget(self.tabWidget)


        self.verticalLayout_20.addWidget(self.container_3)

        self.stackedWidget.addWidget(self.page)
        self.stud_home = QWidget()
        self.stud_home.setObjectName(u"stud_home")
        self.verticalLayout_19 = QVBoxLayout(self.stud_home)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.name_widget = QWidget(self.stud_home)
        self.name_widget.setObjectName(u"name_widget")
        self.name_widget.setMinimumSize(QSize(0, 50))
        self.name_widget.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_20 = QHBoxLayout(self.name_widget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.name = QLabel(self.name_widget)
        self.name.setObjectName(u"name")
        self.name.setFont(font6)
        self.name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.name)


        self.verticalLayout_19.addWidget(self.name_widget)

        self.qn_3 = QWidget(self.stud_home)
        self.qn_3.setObjectName(u"qn_3")
        self.verticalLayout_16 = QVBoxLayout(self.qn_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_16 = QWidget(self.qn_3)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout = QGridLayout(self.widget_16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(35)
        self.gridLayout.setVerticalSpacing(70)
        self.buttons = []
        icon_paths = [f":/icons/icons/{i + 1}.png" for i in range(16)]
        for i in range(4):
            for j in range(4):
                button = QPushButton(self.centralwidget)
                button.setObjectName(f"b{4*i + j + 1}")
                button.setMinimumSize(QSize(0, 100))
                pixmap = QPixmap(icon_paths[4 * i + j])
                button.setIcon(QIcon(pixmap))
                button.setIconSize(QSize(64, 64))
                self.gridLayout.addWidget(button, i, j, 1, 1)
                self.buttons.append(button)


        self.verticalLayout_16.addWidget(self.widget_16, 0, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.qn_3)

        self.stackedWidget.addWidget(self.stud_home)
        self.stud_profile = QWidget()
        self.stud_profile.setObjectName(u"stud_profile")
        self.stud_profile.setStyleSheet(u"")
        self.img = RoundedImageWidget(self.stud_profile)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(20, 20, 241, 191))
        self.name_3 = QLabel(self.stud_profile)
        self.name_3.setObjectName(u"name_3")
        self.name_3.setGeometry(QRect(20, 210, 241, 57))
        self.name_3.setFont(font6)
        self.name_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.stud_profile)
        self.unavilable = QWidget()
        self.unavilable.setObjectName(u"unavilable")
        self.verticalLayout_18 = QVBoxLayout(self.unavilable)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.name_widget_2 = QWidget(self.unavilable)
        self.name_widget_2.setObjectName(u"name_widget_2")
        self.name_widget_2.setMinimumSize(QSize(0, 50))
        self.name_widget_2.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_21 = QHBoxLayout(self.name_widget_2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.name_2 = QLabel(self.name_widget_2)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setFont(font6)
        self.name_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.name_2)


        self.verticalLayout_18.addWidget(self.name_widget_2)

        self.stackedWidget.addWidget(self.unavilable)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.Qns)


        self.verticalLayout_24.addWidget(self.container1)

        MainWindow.setCentralWidget(self.centralwidget)




        self.menu.hide()
        self.Sub1.hide()
        self.incp.hide()
        self.q1.clicked.connect(self.showq1)
        self.q2.clicked.connect(self.showq2)
        self.newqns.clicked.connect(self.addqns)
        self.new_sub.clicked.connect(self.newexam)
        self.login.clicked.connect(self.logins)
        self.logout.clicked.connect(self.logouts)
        self.fp.clicked.connect(self.forgotpasswd)
        self.submit.clicked.connect(self.compile)
        self.q2_3.clicked.connect(self.show_home)
        self.buttons[9].clicked.connect(self.lab_Exam)
        self.buttons[0].clicked.connect(self.prf)
        self.buttons[1].clicked.connect(self.un)
        self.buttons[2].clicked.connect(self.un)
        self.buttons[3].clicked.connect(self.un)
        self.buttons[4].clicked.connect(self.un)
        self.buttons[5].clicked.connect(self.un)
        self.buttons[6].clicked.connect(self.un)
        self.buttons[7].clicked.connect(self.un)
        self.buttons[8].clicked.connect(self.un)
        self.buttons[10].clicked.connect(self.un)
        self.buttons[11].clicked.connect(self.un)
        self.buttons[12].clicked.connect(self.un)
        self.buttons[13].clicked.connect(self.un)
        self.buttons[14].clicked.connect(self.un)
        self.buttons[15].clicked.connect(self.un)
        self.img.setImage("F:/QT/lab/src/lab/icons/vy.jpg")
        
        

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def prf(self):
        self.stackedWidget.setCurrentIndex(5)
    def un(self):
        self.stackedWidget.setCurrentIndex(6)

    def compile(self):
        self.subtest=submit_test()
        q=0
        rollno=self.roll.text()
        if int(rollno) % 2 == 0:
            l=qnss(1)
            q+=2
        else:
            l=qnss(0)
        sub_id=l[-1]
        if (self.stackedWidget.currentIndex()==0):
            q+=1
            code=self.plainTextEdit_4.toPlainText()
            r=run_code(code,[q,sub_id])    
        else:
            q+=2   
            code=self.plainTextEdit_3.toPlainText()
            r=run_code(code,[q,sub_id])    
        self.subtest.inp.setText(r[-1][0])
        self.subtest.exp_op.setText(r[-1][1])
        self.subtest.op.setPlainText(str(r[0][0]))
        if(r[0][1]==0 or r[-1][1] !=str(r[0][0])):
            pixmap = QPixmap(":/icons/rej.png")
            self.subtest.label.setPixmap(pixmap)
        self.subtest.inp_2.setText(r[-1][2])
        self.subtest.exp_op_2.setText(r[-1][3])
        self.subtest.op_2.setPlainText(str(r[1][0]))
        if(r[1][1]==0 or r[-1][3] !=str(r[1][0])):
            pixmap = QPixmap(":/icons/rej.png")
            self.subtest.label_10.setPixmap(pixmap)
        self.subtest.exec_()
            



    def forgotpasswd(self):
        self.frgpass=forgotpass()
        self.frgpass.Box_2.hide()
        self.frgpass.label_9.hide()
        self.frgpass.label_10.hide()
        self.frgpass.label_15.hide()
        self.frgpass.label_14.hide()
        self.frgpass.otp.clicked.connect(self.sendotp)
        self.frgpass.submit.clicked.connect(self.uppass)
        self.frgpass.uppass.clicked.connect(self.passup)
        self.frgpass.exec_()

    def passup(self):
        passd=self.frgpass.passwd.text()
        if(passd != self.frgpass.repass.text()):
            self.frgpass.label_14.show()
        else:
            update_pass(self.user,passd)
            self.frgpass.close()

    def uppass(self):
        if(str(self.otp) == self.frgpass.otp2.text()):
            self.frgpass.stackedWidget.setCurrentIndex(1)
        else:
            self.frgpass.label_15.show()

    def sendotp(self):
        self.frgpass.label_10.show()
        self.user=self.frgpass.username.text()
        self.otp=1000
        self.otp = random.randint(1000, 9999)
        awa_msg(otp,user)
        self.frgpass.Box_2.show()
        self.frgpass.label_9.show()        
        self.frgpass.label_10.hide()

    def subcss(self):
        css = """
    #sub_list{
        border-radius: 15px;
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #292929, stop: 1 #1a1a1a
        );
        color: #FFFFFF;
        border: 1px solid #555555;
    }
    """
        return css

    def elcss(self):
        css = """
    #qn_list {
        border-radius: 15px;
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #292929, stop: 1 #1a1a1a
        );
        color: #FFFFFF;
        border: 1px solid #555555;
    }
    """
        return css


    def create_sub_list(self, index, css, sizePolicy,val):
        s="Sem "+str(val[0])+" - "+val[1]+" - "+str(val[2])
        sub_list = QWidget(self.Box_4)
        sub_list.setObjectName(u"sub_list_{}".format(index))
        sub_list.setMaximumSize(QSize(16777215, 75))
        sub_list.setStyleSheet(css.replace("#sub_list", "#sub_list_{}".format(index)))
        verticalLayout_7 = QVBoxLayout(sub_list)
        verticalLayout_7.setObjectName(u"verticalLayout_7_{}".format(index))

        Sub1_2 = QWidget(sub_list)
        Sub1_2.setObjectName(u"Sub1_2_{}".format(index))
        sizePolicy.setHeightForWidth(Sub1_2.sizePolicy().hasHeightForWidth())
        Sub1_2.setSizePolicy(sizePolicy)
        Sub1_2.setMinimumSize(QSize(0, 0))
        Sub1_2.setMaximumSize(QSize(16777215, 85))
        horizontalLayout_8 = QHBoxLayout(Sub1_2)
        horizontalLayout_8.setObjectName(u"horizontalLayout_8_{}".format(index))
        
        Question = QLabel(Sub1_2)
        Question.setObjectName(u"Question_{}".format(index))
        font16 = QFont()
        font16.setFamily(u"Agency FB")
        font16.setPointSize(25)
        Question.setFont(font16)
        Question.setText(s)
        
        horizontalLayout_8.addWidget(Question)
        
        font14 = QFont()
        font14.setFamily(u"Orbitron")
        
        pushButton_2 = QPushButton(Sub1_2)
        pushButton_2.setObjectName(u"pushButton_2")
        pushButton_2.setMinimumSize(QSize(0, 35))
        pushButton_2.setMaximumSize(QSize(68, 16777215))
        pushButton_2.setFont(font14)
        icon = QIcon()
        icon.addFile(u":/icons/del.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_2.setIcon(icon)
        pushButton_2.setIconSize(QSize(45, 35))

        horizontalLayout_8.addWidget(pushButton_2)
        pushButton_2.clicked.connect(lambda _, idx=index: self.handle_sub_delete([val[1],]))

        pushButton = QPushButton(Sub1_2)
        pushButton.setObjectName(u"pushButton_{}".format(index))
        pushButton.setMinimumSize(QSize(0, 35))
        pushButton.setMaximumSize(QSize(115, 16777215))
        
        pushButton.setFont(font14)
        pushButton.setText("Edit")
        
        horizontalLayout_8.addWidget(pushButton)
        pushButton.clicked.connect(lambda _, idx=index: self.handle_edit([val[1],]))

        verticalLayout_7.addWidget(Sub1_2)
        return sub_list

    def generate_sub_lists(self, css, sizePolicy):
        for i in reversed(range(self.verticalLayout_27.count())):
            widget_to_remove = self.verticalLayout_27.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

        self.sub_lists = []
        subs=admin_sub()
        for i in range(len(subs)):
            sub_list = self.create_sub_list(i, css, sizePolicy,subs[i])
            self.qn_lists.append(sub_list)
            self.verticalLayout_27.addWidget(sub_list, 0, Qt.AlignTop)    

    def handle_sub_delete(self, val):
        self.popup=deldialogbox()
        if self.popup.exec_() == QtWidgets.QDialog.Accepted:
            delete_sub(val)            
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            self.generate_qn_lists(self.elcss(), sizePolicy)
            self.generate_sub_lists(self.subcss(), sizePolicy)

    def handle_edit(self, val):
        l=editsubj(val)
        self.editsubje=edit_sub()
        self.editsubje.lineEdit_2.setText(str(l[0]))
        self.editsubje.lineEdit_3.setText(l[1])
        date = QDate(l[2].year, l[2].month, l[2].day)
        self.editsubje.dateEdit.setDate(date)
        self.editsubje.Update.clicked.connect(self.update_sub)
        self.editsubje.exec_()

    def update_sub(self):
        q=[]
        q.append(self.editsubje.lineEdit_3.text())
        dates=self.editsubje.dateEdit.date()
        date =dates.toString('yyyy-MM-dd')
        q.append(date)
        update_exm(q)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.generate_sub_lists(self.subcss(), sizePolicy)
        self.editsubje.close()

    def create_qn_list(self, index, css, sizePolicy,val):
        s="Sem "+str(val[1])+" - "+val[2]+" - "+val[0]+"- ( "+str(val[3])+" )"
        qn_list = QWidget(self.Box_2)
        qn_list.setObjectName(u"qn_list_{}".format(index))
        qn_list.setMaximumSize(QSize(16777215, 75))
        qn_list.setStyleSheet(css.replace("#qn_list", "#qn_list_{}".format(index)))
        verticalLayout_7 = QVBoxLayout(qn_list)
        verticalLayout_7.setObjectName(u"verticalLayout_7_{}".format(index))

        Sub1_2 = QWidget(qn_list)
        Sub1_2.setObjectName(u"Sub1_2_{}".format(index))
        sizePolicy.setHeightForWidth(Sub1_2.sizePolicy().hasHeightForWidth())
        Sub1_2.setSizePolicy(sizePolicy)
        Sub1_2.setMinimumSize(QSize(0, 0))
        Sub1_2.setMaximumSize(QSize(16777215, 85))
        horizontalLayout_8 = QHBoxLayout(Sub1_2)
        horizontalLayout_8.setObjectName(u"horizontalLayout_8_{}".format(index))
        
        Question = QLabel(Sub1_2)
        Question.setObjectName(u"Question_{}".format(index))
        font16 = QFont()
        font16.setFamily(u"Agency FB")
        font16.setPointSize(25)
        Question.setFont(font16)
        Question.setText(s)
        
        horizontalLayout_8.addWidget(Question)
        
        font14 = QFont()
        font14.setFamily(u"Orbitron")
        
        pushButton_2 = QPushButton(Sub1_2)
        pushButton_2.setObjectName(u"pushButton_2")
        pushButton_2.setMinimumSize(QSize(0, 35))
        pushButton_2.setMaximumSize(QSize(68, 16777215))
        pushButton_2.setFont(font14)
        icon = QIcon()
        icon.addFile(u":/icons/del.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_2.setIcon(icon)
        pushButton_2.setIconSize(QSize(45, 35))

        horizontalLayout_8.addWidget(pushButton_2)
        pushButton_2.clicked.connect(lambda _, idx=index: self.handle_delete(idx, [val[3],val[0]]))

        pushButton = QPushButton(Sub1_2)
        pushButton.setObjectName(u"pushButton_{}".format(index))
        pushButton.setMinimumSize(QSize(0, 35))
        pushButton.setMaximumSize(QSize(115, 16777215))
        
        pushButton.setFont(font14)
        pushButton.setText("View")
        
        horizontalLayout_8.addWidget(pushButton)
        pushButton.clicked.connect(lambda _, idx=index: self.handle_view(idx, [val[3],val[0]]))

        verticalLayout_7.addWidget(Sub1_2)
        return qn_list

    def generate_qn_lists(self, css, sizePolicy):
        for i in reversed(range(self.verticalLayout_22.count())):
            widget_to_remove = self.verticalLayout_22.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

        self.qn_lists = []
        quns=admin()
        for i in range(len(quns)):
            qn_list = self.create_qn_list(i, css, sizePolicy,quns[i])
            self.qn_lists.append(qn_list)
            self.verticalLayout_22.addWidget(qn_list, 0, Qt.AlignTop)
        


    def handle_delete(self, index, val):
        self.popup=deldialogbox()
        if self.popup.exec_() == QtWidgets.QDialog.Accepted:
            delete_qn(val)
            
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            self.generate_qn_lists(self.elcss(), sizePolicy)

    def handle_view(self, index, val):
        l=viewq(val)
        self.viewques=viewqns()
        self.viewques.lineEdit_2.setText(str(l[0]))
        self.viewques.lineEdit_3.setText(l[1])
        self.viewques.plainTextEdit.setPlainText(l[2])
        self.viewques.lineEdit.setText(l[3])
        self.viewques.Update.clicked.connect(self.viewques.update)
        self.viewques.exec_()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.generate_qn_lists(self.elcss(), sizePolicy)

    def addqns(self):
        self.newques=newqns()
        s=subjects()
        self.newques.comboBox_3.addItems(s)
        qid =qids(self.newques.comboBox_3.currentText())
        self.newques.comboBox_2.addItems(qid)
        self.newques.comboBox_3.currentIndexChanged.connect(self.update_q_id)
        self.newques.Addqns.clicked.connect(self.newques.newq)
        self.newques.exec_()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.generate_qn_lists(self.elcss(), sizePolicy)
       
    def update_q_id(self):
        val= self.newques.comboBox_3.currentText()
        self.newques.comboBox_2.clear()
        qid =qids(val)
        self.newques.comboBox_2.addItems(qid)

    def newexam(self):
        self.nexm=addexam()
        self.nexm.comboBox_2.addItems(["1","2","3","4 "])
        sub=subname(1)
        self.nexm.comboBox_3.addItems(sub)
        self.nexm.comboBox_2.currentIndexChanged.connect(self.update_subname)
        self.nexm.Addqns.clicked.connect(self.insert_exam)
        self.nexm.exec_()
        
    def update_subname(self):
        val= self.nexm.comboBox_2.currentText()
        self.nexm.comboBox_3.clear()
        sub =subname(val)
        self.nexm.comboBox_3.addItems(sub)

    def insert_exam(self):
        sub=self.nexm.comboBox_3.currentText()
        dates=self.nexm.dateEdit.date()
        date =dates.toString('yyyy-MM-dd')
        in_ex(sub,date)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.generate_sub_lists(self.subcss(), sizePolicy)
        self.nexm.close()


    def logouts(self):
        self.popup=dialogbox()
        if self.popup.exec_() == QtWidgets.QDialog.Accepted:
            self.menu.hide()
            self.Sub1.hide()
            self.incp.hide()
            self.username_edit.setText("")
            self.password_edit.setText("")
            self.stackedWidget.setCurrentIndex(2)

    def logins(self):
        user=self.username_edit.text()
        passw=login_user(user)
        if (user=="admin" and passw=="admin"):
            self.Sub1.show()
            self.menu.show()
            self.q1.hide()
            self.q2.hide()
            self.submit.hide()
            self.roll.hide()
            self.sem.hide()
            self.sub_2.hide()
            self.sub_3.hide()
            self.q2_3.hide()
            self.sub.setText("College of Engineering Trivandrum\t\t\t\t\t\t\t\t\t\t Department of Computer Applications")
            self.sub.setAlignment(Qt.AlignCenter)
            self.roll_label.setText("Welcome\n"+user)
            self.stackedWidget.setCurrentIndex(3)

        elif(passw and self.password_edit.text()==passw):
            sd=stud_profile(user)
            self.q2_3.show()
            self.menu.show()
            self.Sub1.show()
            self.q1.hide()
            self.q2.hide()
            self.submit.hide()
            self.roll.hide()
            self.roll_label.hide()
            self.sem.hide()
            self.name.setText(sd[1]+" : "+sd[0])
            self.stackedWidget.setCurrentIndex(4)
            
        else:
            self.incp.show()
            self.username_edit.setText("")
            self.password_edit.setText("")

    def show_home(self):
        self.q2_3.show()
        self.menu.show()
        self.Sub1.show()
        self.q1.hide()
        self.q2.hide()
        self.submit.hide()
        self.roll_label.hide()
        self.roll.hide()
        self.sem.hide()
        self.stackedWidget.setCurrentIndex(4)
            


    def lab_Exam(self):
        user=self.username_edit.text()
        self.menu.show()
        self.Sub1.show()
        self.q1.show()
        self.q2.show()
        self.submit.show()
        self.sem.show()
        self.roll.show()
        self.sub_2.show()
        self.sub_3.show()
        self.q2_3.hide()
        self.roll_label.show()
        self.sub.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.roll_label.setText("Roll NO:")
        self.stackedWidget.setCurrentIndex(0)
        self.roll.setText(user[-2:])
        self.displayqns()

    def showq1(self):
        self.stackedWidget.setCurrentIndex(0)

    def showq2(self):
        self.stackedWidget.setCurrentIndex(1)

    def displayqns(self):
        rollno=self.roll.text()
        if int(rollno) % 2 == 0:
            l=qnss(1)
        else:
            l=qnss(0)
        self.sub.setText(l[0])
        self.sem.setText("Semester:"+str(l[1]))
        self.plainTextEdit_2.setPlainText(l[2])
        self.plainTextEdit.setPlainText(l[3])
        self.q2_title_2.setText(l[4])
        self.q2_title.setText(l[5])
        self.comboBox_4.addItems(langs(l[6]))
        self.comboBox.addItems(langs(l[6]))
        


        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCA LAB"))
        self.sub_2.setText(_translate("MainWindow", "College of Engineering, Trivandrum"))
        self.sub_3.setText(_translate("MainWindow", "Department of Computer Applications"))
        self.roll_label.setText(_translate("MainWindow", "Roll No:"))
        self.q1.setText(_translate("MainWindow", "Question 1"))
        self.q2.setText(_translate("MainWindow", "Question 2"))
        self.q2_3.setText(_translate("MainWindow", u"Home"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.label_3.setText(_translate("MainWindow", "YOUR ANSWER:"))
        self.label_8.setText(_translate("MainWindow", "Choose Option"))
        self.plainTextEdit_4.setPlaceholderText(_translate("MainWindow", "Enter code here"))
        self.label.setText(_translate("MainWindow", "YOUR ANSWER:"))
        self.label_2.setText(_translate("MainWindow", "Choose Option"))
        self.plainTextEdit_3.setPlaceholderText(_translate("MainWindow", "Enter code here"))
        self.label_4.setText(_translate("MainWindow", "LOGIN"))
        self.username.setText(_translate("MainWindow", "Username:"))
        self.username_edit.setPlaceholderText(_translate("MainWindow", "Enter username"))
        self.password.setText(_translate("MainWindow", "Password:"))
        self.password_edit.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.fp.setText(_translate("MainWindow", "Forgot Password?"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.incp.setText(_translate("MainWindow", "Incorrect Username or Password!!!"))
        self.newqns.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tr_page), _translate("MainWindow", u"Questions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subj), _translate("MainWindow", u"Subjects"))
        self.buttons[0].setText(_translate("MainWindow", u"Profile"))
        self.buttons[1].setText(_translate("MainWindow", u"Attendance"))
        self.buttons[2].setText(_translate("MainWindow", u"Result"))
        self.buttons[3].setText(_translate("MainWindow", u"Notes"))
        self.buttons[4].setText(_translate("MainWindow", u"Exam Schedule"))
        self.buttons[5].setText(_translate("MainWindow", u"Time Table"))
        self.buttons[6].setText(_translate("MainWindow", u"Academic Analysis"))
        self.buttons[7].setText(_translate("MainWindow", u"Subjects"))
        self.buttons[8].setText(_translate("MainWindow", u"Assignments"))
        self.buttons[9].setText(_translate("MainWindow", u"LAB EXAM"))
        self.buttons[10].setText(_translate("MainWindow", u"Question Bank"))
        self.buttons[11].setText(_translate("MainWindow", u"Study Materials"))
        self.buttons[12].setText(_translate("MainWindow", u"Viedo Lectures"))
        self.buttons[13].setText(_translate("MainWindow", u"Semester Registration"))
        self.buttons[14].setText(_translate("MainWindow", u"Tutorials"))
        self.buttons[15].setText(_translate("MainWindow", u"Survey"))
        self.name_3.setText(_translate("MainWindow", u"VYSHNAV M"))
        self.name_2.setText(_translate("MainWindow", u"Currently Unavilable!!!! Page under Development"))
        for i, button in enumerate(self.buttons):
            button.setStyleSheet(f"""
                QPushButton#{button.objectName()} {{
                   border: 2px solid transparent; 
border-radius: 10px;
background-color: rgba(0, 0, 0, 0.5);
padding: 10px 20px;
font-size: 16px;
font-weight: bold;
color: white;
border-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #a9a9a9, stop: 0.3 #d3d3d3, stop: 1 #ffffff );
                }}
                QPushButton#{button.objectName()}:hover {{
                    background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #a9a9a9, stop: 0.3 #d3d3d3, stop: 1 #ffffff);
color: whit;
border: 2px solid transparent; 
border-color: black; 
                }}
            """)

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = labs()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

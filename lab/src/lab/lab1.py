# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'labLHruWA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1941, 985)
        MainWindow.setMinimumSize(QSize(0, 400))
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"    background-color: #333333; /* Dark background */\n"
"}\n"
"\n"
"#Sub1, #menu, #q1_header, #q2_header,#new_2,#new_3,#container_3{\n"
"    border-radius: 15px;\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #292929, stop: 1 #1a1a1a\n"
"    );\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"#qn_1, #qn_2 {\n"
"    border-radius: 15px;\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #444444, stop: 1 #333333\n"
"    );\n"
"    color: #CCCCCC; /* Light gray text */\n"
"    border: 1px solid #555555;\n"
"}\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #3498db, stop: 1 #f39c12);\n"
"   	color: black;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1: "
                        "0, y1: 0, x2: 1, y2: 1, stop: 0 #c0392b, stop: 0.3 #e74c3c, stop: 1 #f39c12);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f39c12;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel {\n"
"    color: #CCCCCC; /* Light gray text */\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #333333; /* Dark background */\n"
"    color: #CCCCCC; /* Light gray text */\n"
"    border: 1px solid #555555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
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
"QTabWidget::pane {\n"
"                border-radius: 15px;\n"
""
                        "                 background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);\n"
"                border: 1px solid #555555;\n"
"            }\n"
"            QTabBar::tab {\n"
"                border: none;\n"
"                border-radius: 10px;\n"
"              background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #3498db, stop: 1 #f39c12);\n"
"   	color: black;\n"
"                padding: 10px 20px;\n"
"                font-size: 18px;\n"
"				margin-right:5px;\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #c0392b, stop: 0.3 #e74c3c, stop: 1 #f39c12);\n"
"color: white;\n"
"            }\n"
"")
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
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.q1.setFont(font4)

        self.verticalLayout_2.addWidget(self.q1)

        self.q2 = QPushButton(self.menu)
        self.q2.setObjectName(u"q2")
        self.q2.setFont(font4)

        self.verticalLayout_2.addWidget(self.q2)

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
        font14.setBold(True)
        font14.setWeight(75)
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
        self.widget_3.setMinimumSize(QSize(0, 800))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Box_2 = QFrame(self.widget_3)
        self.Box_2.setObjectName(u"Box_2")
        sizePolicy.setHeightForWidth(self.Box_2.sizePolicy().hasHeightForWidth())
        self.Box_2.setSizePolicy(sizePolicy)
        self.Box_2.setFrameShape(QFrame.StyledPanel)
        self.Box_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Box_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.qn_list = QWidget(self.Box_2)
        self.qn_list.setObjectName(u"qn_list")
        self.qn_list.setMaximumSize(QSize(16777215, 75))
        self.verticalLayout_23 = QVBoxLayout(self.qn_list)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.Sub1_2 = QWidget(self.qn_list)
        self.Sub1_2.setObjectName(u"Sub1_2")
        sizePolicy.setHeightForWidth(self.Sub1_2.sizePolicy().hasHeightForWidth())
        self.Sub1_2.setSizePolicy(sizePolicy)
        self.Sub1_2.setMinimumSize(QSize(0, 0))
        self.Sub1_2.setMaximumSize(QSize(16777215, 85))
        self.Sub1_2.setStyleSheet(u"")
        self.horizontalLayout_18 = QHBoxLayout(self.Sub1_2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.Question = QLabel(self.Sub1_2)
        self.Question.setObjectName(u"Question")
        font17 = QFont()
        font17.setFamily(u"Agency FB")
        font17.setPointSize(25)
        self.Question.setFont(font17)

        self.horizontalLayout_18.addWidget(self.Question)

        self.pushButton = QPushButton(self.Sub1_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        self.pushButton.setMaximumSize(QSize(68, 16777215))
        self.pushButton.setFont(font14)
        icon = QIcon()
        icon.addFile(u":/icons/del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(45, 35))

        self.horizontalLayout_18.addWidget(self.pushButton)

        self.pushButton_6 = QPushButton(self.Sub1_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 35))
        self.pushButton_6.setMaximumSize(QSize(115, 16777215))
        self.pushButton_6.setFont(font14)

        self.horizontalLayout_18.addWidget(self.pushButton_6)


        self.verticalLayout_23.addWidget(self.Sub1_2)


        self.verticalLayout_22.addWidget(self.qn_list, 0, Qt.AlignTop)


        self.horizontalLayout_13.addWidget(self.Box_2)


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
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_17.addWidget(self.tabWidget)


        self.verticalLayout_20.addWidget(self.container_3)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.Qns)


        self.verticalLayout_24.addWidget(self.container1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.q1, self.q2)
        QWidget.setTabOrder(self.q2, self.logout)
        QWidget.setTabOrder(self.logout, self.plainTextEdit_2)
        QWidget.setTabOrder(self.plainTextEdit_2, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.plainTextEdit_4)
        QWidget.setTabOrder(self.plainTextEdit_4, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.plainTextEdit_3)
        QWidget.setTabOrder(self.plainTextEdit_3, self.username_edit)
        QWidget.setTabOrder(self.username_edit, self.password_edit)
        QWidget.setTabOrder(self.password_edit, self.fp)
        QWidget.setTabOrder(self.fp, self.login)
        QWidget.setTabOrder(self.login, self.submit)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MCA LAB", None))
        self.sem.setText(QCoreApplication.translate("MainWindow", u"Semester", None))
        self.sub.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.roll_label.setText(QCoreApplication.translate("MainWindow", u"Roll No:", None))
        self.roll.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.q1.setText(QCoreApplication.translate("MainWindow", u"Question 1", None))
        self.q2.setText(QCoreApplication.translate("MainWindow", u"Question 2", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.q2_title_2.setText(QCoreApplication.translate("MainWindow", u"Question 1 Title", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Question", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Your Answer", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Choose Option", None))
        self.plainTextEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter code here", None))
        self.q2_title.setText(QCoreApplication.translate("MainWindow", u"Question 2 Title", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Question", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your Answer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Choose Option", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter code here", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter username", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.fp.setText(QCoreApplication.translate("MainWindow", u"Forgot Password?", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.incp.setText(QCoreApplication.translate("MainWindow", u"Incorrect Username or Password!!!", None))
        self.Question.setText(QCoreApplication.translate("MainWindow", u"Question", None))
        self.pushButton.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.newqns.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tr_page), QCoreApplication.translate("MainWindow", u"Questions", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Subjects", None))
    # retranslateUi


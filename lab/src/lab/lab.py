from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import icon_rc


from fns import *
import os

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
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"    background-color: #333333; /* Dark background */\n"
"}\n"
"\n"
"#Sub1, #menu, #q1_header, #q2_header {\n"
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
"\n"
"QPushButton {\n"
"    border: 1px solid #29a19c;\n"
"    border-radius: 15px;\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 #3e3e3e, stop: 1 #2e2e2e\n"
"    );\n"
"    color: #FFFFFF;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #29a19c;\n"
"    color: #1e1e1e;\n"
"}\n"
"\n"
"QPus"
                        "hButton:pressed {\n"
"    background-color: #206a67;\n"
"    color: #FFFFFF;\n"
"}\n"
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
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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


        self.verticalLayout.addWidget(self.Sub1)

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
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ffa502, stop: 0.3 #ff7f50, stop: 1 #ff6348);\n"
"    color: #FFFFFF;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #48C9B0, stop: 0.3 #5DADE2, stop: 1 #85C1E9);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ff6348;\n"
"}\n"
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
"    backgrou"
                        "nd-color: #1C1C1C; /* Light Grey */\n"
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
        self.tr_page = QWidget()
        self.tr_page.setObjectName(u"tr_page")
        self.tr_page.setStyleSheet(u"\n"
"#widget_3 {\n"
"    border-radius: 15px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #29323c, stop: 0.3 #485563, stop: 1 #2e3f50);\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #555555;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #ffa502, stop: 0.3 #ff7f50, stop: 1 #ff6348);\n"
"    color: #FFFFFF;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #48C9B0, stop: 0.3 #5DADE2, stop: 1 #85C1E9);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ff6348;\n"
"}\n"
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
"  "
                        "  background-color: #1C1C1C; /* Light Grey */\n"
"}\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.tr_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.container_2 = QFrame(self.tr_page)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setFrameShape(QFrame.StyledPanel)
        self.container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.container_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.container_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Box_2 = QFrame(self.widget_3)
        self.Box_2.setObjectName(u"Box_2")
        sizePolicy.setHeightForWidth(self.Box_2.sizePolicy().hasHeightForWidth())
        self.Box_2.setSizePolicy(sizePolicy)
        self.Box_2.setFrameShape(QFrame.StyledPanel)
        self.Box_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Box_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")

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

        # Now, call the function to generate qn_lists
        self.generate_qn_lists(css, sizePolicy)


            

        self.horizontalLayout_10.addWidget(self.Box_2, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.widget_3)


        self.verticalLayout_9.addWidget(self.container_2)

        self.stackedWidget.addWidget(self.tr_page)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.Qns)


        self.verticalLayout.addWidget(self.container1)

        MainWindow.setCentralWidget(self.centralwidget)




        self.menu.hide()
        self.Sub1.hide()
        self.incp.hide()
        self.q1.clicked.connect(self.showq1)
        self.q2.clicked.connect(self.showq2)
        self.login.clicked.connect(self.logins)
        self.logout.clicked.connect(self.logouts)
        
        

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def create_qn_list(self, index, css, sizePolicy):
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
        Sub1_2.setMaximumSize(QSize(16777215, 50))
        horizontalLayout_8 = QHBoxLayout(Sub1_2)
        horizontalLayout_8.setObjectName(u"horizontalLayout_8_{}".format(index))
        
        Question = QLabel(Sub1_2)
        Question.setObjectName(u"Question_{}".format(index))
        font16 = QFont()
        font16.setFamily(u"Agency FB")
        font16.setPointSize(25)
        Question.setFont(font16)
        Question.setText(f"Question {index+1}")
        
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

        pushButton = QPushButton(Sub1_2)
        pushButton.setObjectName(u"pushButton_{}".format(index))
        pushButton.setMinimumSize(QSize(0, 35))
        pushButton.setMaximumSize(QSize(115, 16777215))
        
        pushButton.setFont(font14)
        pushButton.setText("View")
        
        horizontalLayout_8.addWidget(pushButton)

        verticalLayout_7.addWidget(Sub1_2)
        return qn_list

    def generate_qn_lists(self, css, sizePolicy):
        self.qn_lists = []

        for i in range(5):
            qn_list = self.create_qn_list(i, css, sizePolicy)
            self.qn_lists.append(qn_list)
            self.verticalLayout_16.addWidget(qn_list, 0, Qt.AlignTop)


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
            self.sub.setText("LAB Questions")
            self.sub.setAlignment(Qt.AlignCenter)
            self.roll_label.setText("Welcome\n"+user)
            self.stackedWidget.setCurrentIndex(3)
        elif(passw and self.password_edit.text()==passw):
            self.menu.show()
            self.Sub1.show()
            self.q1.show()
            self.q2.show()
            self.submit.show()
            self.sem.show()
            self.sub.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
            self.roll_label.setText("Roll NO:")
            self.stackedWidget.setCurrentIndex(0)
            self.roll.setText(user[-2:])
            self.displayqns()
        else:
            self.incp.show()
            self.username_edit.setText("")
            self.password_edit.setText("")


    def showq1(self):
        self.stackedWidget.setCurrentIndex(0)

    def showq2(self):
        self.stackedWidget.setCurrentIndex(1)

    def displayqns(self):
        sub = "MCA20101"
        l=qnss(sub)
        self.sub.setText(l[0])
        self.sem.setText("Semester:"+str(l[1]))
        self.plainTextEdit_2.setPlainText(l[2])
        self.plainTextEdit.setPlainText(l[3])
        self.q2_title_2.setText(l[4])
        self.q2_title.setText(l[5])
        self.comboBox_4.addItems(langs(sub))
        self.comboBox.addItems(langs(sub))
        


        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MCA LAB"))
        self.roll_label.setText(_translate("MainWindow", "Roll No:"))
        self.q1.setText(_translate("MainWindow", "Question 1"))
        self.q2.setText(_translate("MainWindow", "Question 2"))
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
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = labs()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

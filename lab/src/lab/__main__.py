from lab.app import main
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from rounded_image_widget import RoundedImageWidget
import icon_rc

from cssfn import *
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


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        ui_path = os.path.abspath("F:/QT/lab/src/lab/lab.ui")
        uic.loadUi(ui_path, self)
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
        self.stackedWidget.setCurrentIndex(2)
        self.buttons[9].clicked.connect(self.lab_Exam)
        self.buttons[0].clicked.connect(self.prf)
        self.buttons[1].clicked.connect(self.un)
        self.buttons[2].clicked.connect(self.un)
        self.buttons[3].clicked.connect(self.un)
        self.buttons[4].clicked.connect(self.exmschedule)
        self.buttons[5].clicked.connect(self.un)
        self.buttons[6].clicked.connect(self.un)
        self.buttons[7].clicked.connect(self.studsub)
        self.buttons[8].clicked.connect(self.un)
        self.buttons[10].clicked.connect(self.un)
        self.buttons[11].clicked.connect(self.un)
        self.buttons[12].clicked.connect(self.un)
        self.buttons[13].clicked.connect(self.un)
        self.buttons[14].clicked.connect(self.un)
        self.buttons[15].clicked.connect(self.un)
        self.img.setImage("F:/QT/lab/src/lab/icons/vy.jpg")
        self.theme.clicked.connect(self.changeTheme)
        self.setStyleSheet(getDarkTheme())
        self.retranslateUi()

    
    def changeTheme(self):
        if self.styleSheet() == getDarkTheme():
            self.setStyleSheet(getLightTheme())  
            self.applyLightThemeStyles()
            icon1 = QIcon()
            icon1.addFile(u":/icons/icons/light.png", QSize(), QIcon.Normal, QIcon.Off)
            self.theme.setIcon(icon1)
            self.theme.setIconSize(QSize(70, 40))
        else:
            self.setStyleSheet(getDarkTheme()) 
            self.applyDarkThemeStyles()
            icon1 = QIcon()
            icon1.addFile(u":/icons/icons/dark.png", QSize(), QIcon.Normal, QIcon.Off)
            self.theme.setIcon(icon1)
            self.theme.setIconSize(QSize(70, 40))
            
    def applyDarkThemeStyles(self):
        dark_css = """#sub_list_2{
        border-radius: 15px;
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #292929, stop: 1 #1a1a1a
        );
        color: #FFFFFF;
        border: 1px solid #555555;}
        """
        self.applyStylesToElements(dark_css)

    def applyLightThemeStyles(self):
        light_css = """
        #sub_list_2{
    border-radius: 15px;
    background-color: qlineargradient(
        x1: 0, y1: 0, x2: 1, y2: 1,
        stop: 0 #f0f0f0, stop: 1 #e0e0e0
    );
    color: #000000;
    border: 1px solid #aaaaaa;}
    """
        self.applyStylesToElements(light_css)

    def applyStylesToElements(self, css):
        # Apply styles to sub_list elements
        for i in reversed(range(self.verticalLayout_27.count())):
            item = self.verticalLayout_27.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                widget.setStyleSheet(css.replace("#sub_list_2", "#sub_list_{}".format(i)))

        # Apply styles to sub_list_2 elements
        for i in reversed(range(self.verticalLayout_29.count())):
            item = self.verticalLayout_29.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                widget.setStyleSheet(css.replace("#sub_list_2", "#sub_list_2_{}".format(i)))

        # Apply styles to qn_list elements
        for i in reversed(range(self.verticalLayout_22.count())):
            item = self.verticalLayout_22.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                widget.setStyleSheet(css.replace("#sub_list_2", "#qn_list_{}".format(i)))

        for i in reversed(range(self.gridLayout_2.count())):
            item = self.gridLayout_2.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                widget.setStyleSheet(css.replace("#sub_list_2", "#exm_list_2_{}".format(i)))
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MCA LAB"))
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
        self.name_4.setText(_translate("MainWindow", "Student Profile"))
        self.ktuid.setText(_translate("MainWindow", "KTU-ID"))
        self.phno.setText(_translate("MainWindow", "Phone Number"))
        self.gender.setText(_translate("MainWindow", "Gender"))
        self.email.setText(_translate("MainWindow", "E-mail"))
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

    def exmschedule(self):
        css = """
    #sub_list_2{
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
        self.generate_exmschedule(css, sizePolicy)
        self.stackedWidget.setCurrentIndex(7)


    def create_exmschedule(self, index, css, sizePolicy,val):
        sub_list = QWidget(self.Box_6)
        sub_list.setObjectName(u"exm_list_2_{}".format(index))
        sub_list.setMinimumSize(QtCore.QSize(500, 200))
        sub_list.setMaximumSize(QtCore.QSize(500, 200))
        sub_list.setStyleSheet(css.replace("#sub_list_2", "#exm_list_2_{}".format(index)))
        verticalLayout_7 = QVBoxLayout(sub_list)
        verticalLayout_7.setObjectName(u"verticalLayout_7_{}".format(index))
        font16 = QFont()
        font16.setFamily(u"Agency FB")
        font16.setPointSize(25)
        exm_subject = QtWidgets.QLabel(sub_list)
        exm_subject.setObjectName(u"exm_subject_{}".format(index))
        exm_subject.setText(val[1])
        exm_subject.setAlignment(QtCore.Qt.AlignCenter)
        exm_subject.setFont(font16)
        verticalLayout_7.addWidget(exm_subject)

        exm_date = QtWidgets.QLabel(sub_list)
        exm_date.setObjectName(u"exm_date_{}".format(index))
        exm_date.setText(str(val[2]))
        exm_date.setAlignment(QtCore.Qt.AlignCenter)
        exm_date.setFont(font16)
        verticalLayout_7.addWidget(exm_date)

        return sub_list

    def generate_exmschedule(self, css, sizePolicy):
        for i in reversed(range(self.gridLayout_2.count())):
            widget_to_remove = self.gridLayout_2.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

        self.stud_sub_lists = []
        subs=admin_sub(1,self.user)
        i=0
        k=0
        for j in range(len(subs)):
            sub_list = self.create_exmschedule(j, css, sizePolicy,subs[j])
            self.stud_sub_lists.append(sub_list)
            self.gridLayout_2.addWidget(sub_list, i,k,1,1, Qt.AlignTop) 
            k+=1
            if(k==3):
                i+=1
                k=0


    def studsub(self):
        css = """
    #sub_list_2{
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
        self.generate_stud_sub_lists(css, sizePolicy)
        self.stackedWidget.setCurrentIndex(6)


    def prf(self):
        l=stud_profile(self.user)
        self.name_3.setText(l[0])
        self.KTUID.setText(self.user)
        self.PHNO.setText(l[1])
        self.GENDER.setText(l[2])
        self.EMAIL.setText(l[3])
        self.DOB.setText(str(l[4]))
        self.img.setImage("F:/QT/lab/src/lab/icons/"+self.user+".jpg")
        self.stackedWidget.setCurrentIndex(5)
    def un(self):
        self.stackedWidget.setCurrentIndex(8)

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
        wa_msg(self.otp,self.user)
        self.frgpass.Box_2.show()
        self.frgpass.label_9.show()        
        self.frgpass.label_10.hide()

    def studsubcss(self):
        css = """
    #sub_list_2{
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

    def create_stud_sub_list(self, index, css, sizePolicy,val):
        s=str(index+1)+" ) "+val[0]+" - "+val[1]
        sub_list = QWidget(self.Box_5)
        sub_list.setObjectName(u"sub_list_2_{}".format(index))
        sub_list.setMaximumSize(QSize(16777215, 75))
        sub_list.setStyleSheet(css.replace("#sub_list_2", "#sub_list_2_{}".format(index)))
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
        verticalLayout_7.addWidget(Sub1_2)
        return sub_list

    def generate_stud_sub_lists(self, css, sizePolicy):
        for i in reversed(range(self.verticalLayout_29.count())):
            widget_to_remove = self.verticalLayout_29.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

        self.stud_sub_lists = []
        subs=stud_sub(self.user)
        for i in range(len(subs)):
            sub_list = self.create_stud_sub_list(i, css, sizePolicy,subs[i])
            self.stud_sub_lists.append(sub_list)
            self.verticalLayout_29.addWidget(sub_list, 0, Qt.AlignTop)   




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
        subs=admin_sub(0,0)
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
        self.viewques.Up.clicked.connect(self.viewques.update)
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
        self.user=self.username_edit.text()
        passw=login_user(self.user)
        if (self.user=="admin" and passw=="admin"):
            self.Sub1.show()
            self.menu.show()
            self.q1.hide()
            self.q2.hide()
            self.submit.hide()
            self.roll.hide()
            self.sem.hide()
            self.roll_label.show()
            self.sub_2.show()
            self.sub_3.show()
            self.q2_3.hide()
            self.sub.hide()
            self.sub.setAlignment(Qt.AlignCenter)
            self.roll_label.setText("Welcome\n"+self.user)
            self.stackedWidget.setCurrentIndex(3)

        elif(passw and self.password_edit.text()==passw):
            sd=stud_profile(self.user)
            self.q2_3.show()
            self.menu.show()
            self.Sub1.show()
            self.sub.hide()
            self.q1.hide()
            self.q2.hide()
            self.sub_2.show()
            self.sub_3.show()
            self.submit.hide()
            self.roll.hide()
            self.roll_label.hide()
            self.sem.hide()
            self.name.setText(sd[0]+" : "+self.user)
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainUi()
    main_window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
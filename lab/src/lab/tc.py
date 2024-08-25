from PyQt5 import QtCore, QtGui, QtWidgets

class DynamicGridLayout(QtWidgets.QWidget):
    def __init__(self, n, parent=None):
        super(DynamicGridLayout, self).__init__(parent)
        
        # Create the main layout and ScrollArea
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1462, 149))
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        
        # Add n rows dynamically
        for i in range(n):
            self.add_row(i)

        # Set up the scroll area and main layout
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea, 0, QtCore.Qt.AlignTop)

    def add_row(self, row_number):
        # Create and configure widgets for the row
        op = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        op.setMinimumSize(QtCore.QSize(550, 30))
        op.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        op.setFont(font)
        op.setReadOnly(True)

        inp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        inp.setMinimumSize(QtCore.QSize(0, 30))
        inp.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        inp.setFont(font)
        inp.setAlignment(QtCore.Qt.AlignCenter)
        inp.setReadOnly(True)

        inp_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        inp_2.setMinimumSize(QtCore.QSize(0, 30))
        inp_2.setMaximumSize(QtCore.QSize(300, 16777215))
        inp_2.setFont(font)
        inp_2.setAlignment(QtCore.Qt.AlignCenter)
        inp_2.setReadOnly(True)

        label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        label.setMaximumSize(QtCore.QSize(25, 25))
        label.setPixmap(QtGui.QPixmap(":/icons/accept.png"))
        label.setScaledContents(True)

        exp_op = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        exp_op.setMinimumSize(QtCore.QSize(0, 30))
        exp_op.setMaximumSize(QtCore.QSize(300, 16777215))
        exp_op.setFont(font)
        exp_op.setAlignment(QtCore.Qt.AlignCenter)
        exp_op.setReadOnly(True)

        # Add widgets to the grid layout in the specified row
        self.gridLayout.addWidget(inp_2, row_number, 0)
        self.gridLayout.addWidget(inp, row_number, 1)
        self.gridLayout.addWidget(exp_op, row_number, 2)
        self.gridLayout.addWidget(op, row_number, 3)
        self.gridLayout.addWidget(label, row_number, 4)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    n = 5  # Number of rows you want to generate
    window = DynamicGridLayout(n)
    window.show()
    sys.exit(app.exec_())

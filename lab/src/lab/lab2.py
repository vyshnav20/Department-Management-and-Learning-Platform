from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl   
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create a QWebEngineView and add it to the layout
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        # Load a webpage
        self.browser.setUrl(QUrl("https://ktumca.github.io/materials"))

        # Set window title and dimensions
        self.setWindowTitle("Web Browser in PyQt")
        self.resize(800, 600)

# Set up the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

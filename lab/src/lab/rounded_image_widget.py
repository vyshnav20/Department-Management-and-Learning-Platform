import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPixmap, QPainterPath
from PyQt5.QtCore import QRectF

class RoundedImageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_path = ''
        self.image = QPixmap()

    def setImage(self, image_path):
        self.image_path = image_path
        self.image = QPixmap(image_path)
        self.update()  # Refresh the widget to repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()
        
        path = QPainterPath()
        path.addRoundedRect(QRectF(rect), 150, 150)  # Convert QRect to QRectF

        painter.setClipPath(path)
        painter.drawPixmap(rect, self.image)  # Use QRect for drawPixmap

        painter.end()
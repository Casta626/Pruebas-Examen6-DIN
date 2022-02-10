import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit
)

class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Ponemos una barra de estado
        self.statusBar()

        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)

        # Creamos los tips
        tipInput = "Escribe el texto que quieras"
        # Añadimos a la barra de estado
        self.input.setStatusTip(tipInput)
        # Y como ventana emergente
        self.input.setToolTip(tipInput)

        tipButton = "Abre una nueva ventana"
        self.button.setStatusTip(tipButton)
        self.button.setToolTip(tipButton)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def toggle_window(self, checked):
        
        if self.w.isVisible():
            self.w.hide()

        else:
            self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()


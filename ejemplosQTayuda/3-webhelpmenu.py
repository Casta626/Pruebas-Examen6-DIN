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

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtHelp import QHelpEngineCore
from PySide6.QtGui import QAction

class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Ayuda en línea:")
        # Creamos un visor web
        self.browser = QWebEngineView()
        self.browser.setUrl("https://google.es")

        layout.addWidget(self.label)
        layout.addWidget(self.browser)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Al llamarse de esta forma, el SO lo detecta. macOS agrega una barra de búsqueda.
        help_menu = self.menuBar().addMenu("&Help")
        
        help_action = QAction("&Abrir Ayuda", self)
        help_action.setStatusTip("Acción de abrir la ayuda")
        help_action.triggered.connect(self.toggle_window)

        help_menu.addAction(help_action)

        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)

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
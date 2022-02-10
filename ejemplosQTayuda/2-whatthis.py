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

        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)


        self.button2 = QPushButton("Push for Window")
        

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)
        

        # Creamos el tip
        tipButton = "Abre una nueva ventana y esta es una descripción más detallada de la acción"

        self.button2.setWhatsThis(tipButton)
        # Y se lo asignamos con el método setWhatThis
        self.button.setWhatsThis(tipButton)
        self.input.setWhatsThis("Los gormitis y los personajes de la wwe vivian en armonia")
        # La ventana aparecerá pulsando 
        # 
        # 
        # 
        ################################################ Pulsa shift+F1 por favor David :( ######################################################################
        # 
        # 
        # 
        # cuando el botón tenga el foco
        # También se puede crear una acción que ponga en modo "ayuda" o que se active con un botón. Ver documentación: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWhatsThis.html

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)
        layout.addWidget(self.button2)
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
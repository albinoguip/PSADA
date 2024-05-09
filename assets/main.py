 # coding:utf-8
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QCompleter, QMainWindow
from qfluentwidgets import ComboBox, setTheme, Theme, setThemeColor, EditableComboBox

# from widgets import *
from UIWidgets import *
from UIFunctions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        UIFunctions.uiDefinitions(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

# Importinng necessary modules and classes:
import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,QComboBox,QLineEdit,QTextEdit,QWidget,QToolBar,QStatusBar)
from PyQt5.QtGui import (QPalette,QColor,QFont)

# MainWindowApp class
class PermanonceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
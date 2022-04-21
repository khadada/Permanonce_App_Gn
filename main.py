# Importinng necessary modules and classes:
import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,QComboBox,QLineEdit,QTextEdit,QWidget,QToolBar,QStatusBar,QGridLayout,QPushButton)
from PyQt5.QtGui import (QPalette,QColor,QFont,QIcon)

# MainWindowApp class
class PermanonceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.workspace = None
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the main window and display its content
        """
        self.setGeometry(10, 10, 800, 600)
        self.setWindowTitle("برنامج الخفير فرقة تماسين")
        self.setWindowIcon(QIcon("icons/policeman.png"))
        self.display_content()
    
    def display_content(self):
        """
        Display the content of the main window
        """
        # Create vertical layout
        main_layout = QGridLayout()
        self.day_event_btn = QPushButton
        
        
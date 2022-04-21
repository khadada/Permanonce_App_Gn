# Importinng necessary modules and classes:
import sys
from turtle import color
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,QComboBox,QLineEdit,QTextEdit,QWidget,QToolBar,QStatusBar,QGridLayout,QPushButton)
from PyQt5.QtGui import (QPalette,QColor,QFont,QIcon)

# MainWindowApp class
class PermanonceApp(QMainWindow):
    PRIMARY_COLOR = "#10893e"
    INITIAL_COLOR = "#fff"
    RADIUS_BTNS = "8px"
    PADDING_BTN = "15px"
    def __init__(self):
        super().__init__()
        self.workspace = None
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the main window and display its content
        """
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("برنامج الخفير فرقة تماسين")
        self.setWindowIcon(QIcon("icons/policeman.png"))
        self.display_content()
    
    def display_content(self):
        """
        Display the content of the main window
        """
        # Create vertical layout
        main_layout = QGridLayout()
        #----------------------------------------------------------
        self.day_event_btn = QPushButton("الأحداث اليومية")
        self.day_event_btn.setStyleSheet("QPushButton"
                                         "{"
                                         "font: 75 12pt Calibri;"
                                         f"border:2px solid {PermanonceApp.PRIMARY_COLOR};"
                                         f"background-color: {PermanonceApp.INITIAL_COLOR};"
                                         f"color: {PermanonceApp.PRIMARY_COLOR};"
                                         f"padding: {PermanonceApp.PADDING_BTN};"
                                         f"border-radius: {PermanonceApp.RADIUS_BTNS};"
                                         "}"
                                         "QPushButton::hover"
                                         "{"
                                         f"background-color: {PermanonceApp.PRIMARY_COLOR};"
                                         f"color: {PermanonceApp.INITIAL_COLOR};"
                                         "}"
                                         )
        main_layout.addWidget(self.day_event_btn,0,0,1,1)

        #......................
        #----------------------------------------------------------
        self.call_log_btn = QPushButton(" المكالمات الهاتفية")
        #...................... 
        #......................
        #----------------------------------------------------------
        self.messages_btn = QPushButton("البرقيات")
        #...................... 
        #......................
        #----------------------------------------------------------
        self.birth_certificate_btn = QPushButton("طلب شهادات الميلاد")
        #...................... 
        #......................
        #----------------------------------------------------------
        self.judicial_precedent_btn = QPushButton("طلب السوابق القضائية")
        #...................... 
        #......................
        #----------------------------------------------------------
        # Create the container that hold widgets and set its layout a
        container = QWidget()
        container.setLayout(main_layout)
        # Set the container as the central widget of the main window
        self.setCentralWidget(container)
 # Run the program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gn_apps =  PermanonceApp()   
    sys.exit(app.exec_())   
        
        
        
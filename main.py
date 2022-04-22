# Importinng necessary modules and classes:
import sys
from turtle import color
import PyQt5
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,QComboBox,QLineEdit,QTextEdit,QWidget,QToolBar,QStatusBar,QGridLayout,QPushButton,QHBoxLayout)
from PyQt5.QtGui import (QPalette,QColor,QFont,QIcon,QBrush,QImage)
from PyQt5.QtCore import Qt,QSize

# MainWindowApp class
class PermanonceApp(QMainWindow):
    PRIMARY_COLOR = "#10893e"
    INITIAL_COLOR = "#fff"
    RADIUS_BTNS = "8px"
    PADDING_BTN = "50px"
    FONT = "75 14pt Calibri"
    def __init__(self):
        super().__init__()
        self.workspace = None
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the main window and display its content
        """
        #self.setGeometry(50, 50, 900, 600)
        self.setWindowTitle("برنامج الخفير فرقة تماسيـــــــن")
        self.setMinimumSize(800,600)
        self.setWindowIcon(QIcon("icons/policeman.png"))
        self.display_content()
    
    def display_content(self):
        """
        Display the content of the main window
        """
        # Create vertical layout
        main_layout = QGridLayout()
        main_layout.setSpacing(40)
        #----------------------------------------------------------
        # Header:
        header = QLabel("برنامج الخفيـر")   
        header.setStyleSheet(f"color: {PermanonceApp.PRIMARY_COLOR};font: {PermanonceApp.FONT};")
        header.setAlignment(Qt.AlignHCenter)
        main_layout.addWidget(header,0,0,1,3)
        self.day_event_btn = QPushButton("الأحداث اليومية")
        self.day_event_btn.setStyleSheet("QPushButton"
                                         "{"
                                         f"font: {PermanonceApp.FONT};"
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
        main_layout.addWidget(self.day_event_btn,1,0,1,1)

        #......................
        #----------------------------------------------------------
        self.call_log_btn = QPushButton(" المكالمات الهاتفية")
        self.call_log_btn.setStyleSheet("QPushButton"
                                         "{"
                                         f"font: {PermanonceApp.FONT};"
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
        main_layout.addWidget(self.call_log_btn,1,1,1,1)
        #...................... 
        #......................
        #----------------------------------------------------------
        self.messages_btn = QPushButton("البرقيات")
        self.messages_btn.setStyleSheet("QPushButton"
                                         "{"
                                         f"font: {PermanonceApp.FONT};"
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
        main_layout.addWidget(self.messages_btn,1,2,1,1)
        #...................... 
        #......................
        #----------------------------------------------------------
        two_column = QHBoxLayout()
        self.birth_certificate_btn = QPushButton("طلب شهادات الميلاد")
        self.birth_certificate_btn.setStyleSheet("QPushButton"
                                         "{"
                                         f"font: {PermanonceApp.FONT};"
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
        #...................... 
        #......................
        #----------------------------------------------------------
        self.judicial_precedent_btn = QPushButton("طلب السوابق القضائية")
        self.judicial_precedent_btn.setStyleSheet("QPushButton"
                                         "{"
                                         f"font: {PermanonceApp.FONT};"
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
        two_column.addWidget(self.judicial_precedent_btn)
        two_column.addWidget(self.birth_certificate_btn)
        main_layout.addLayout(two_column,2,0,1,3)
        
        
        
        #...................... 
        #......................
        #----------------------------------------------------------
        # Create the container that hold widgets and set its layout a
        container = QWidget()
        img_or = QImage("icons/policeman.png")
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(img_or))
        container.setPalette(palette)
        container.setLayout(main_layout)
        # Set the container as the central widget of the main window
        self.setCentralWidget(container)

 # Run the program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gn_apps =  PermanonceApp()   
    sys.exit(app.exec_())   
        
        
        
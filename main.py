# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from Modules import *
import sys, os, platform



# SETTING ENVIORNMENT VARIABLES AND GLOBAL VARIABLES
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
widgets = None


# PATH HELPER
# ///////////////////////////////////////////////////////////////
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                   MAIN WINDOW                                                                  ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        
        # DEFINE BASE WIDGETS
        # ///////////////////////////////////////////////////////////////

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui


        # DEFINE SPECIFIC WIDGETS
        # ///////////////////////////////////////////////////////////////

        DYNW = DYN_Widgets()
        DYNW._create_dynamic(widgets)


        # 
        # ///////////////////////////////////////////////////////////////


        self.setWindowTitle("Data Analysis Tool")
        widgets.titleRightInfo.setText("Data Analysis Tool")

        # BASE_Functions.constructor(self) 
        
        widgets.toggleButton.clicked.connect(lambda: BASE_Functions.toggleMenu(self, True)) # TOGGLE MENU        
        BASE_Functions.uiDefinitions(self)                                                  # SET UI DEFINITIONS

        widgets.btn_home.clicked.connect(self.buttonClick)     # HOME
        widgets.btn_dynamic.clicked.connect(self.buttonClick)  # DYNAMIC
        widgets.btn_static.clicked.connect(self.buttonClick)  # STATIC
        widgets.btn_dynamic_static.clicked.connect(self.buttonClick)  # DYNAMIC STATIC
        widgets.btn_network.clicked.connect(self.buttonClick)  # NETWORK
        

        self.show() 

        BASE_Functions.theme(self, resource_path('assets/albino_light_theme.qss'), True)

        widgets.stackedWidget.setCurrentWidget(widgets.home)      


        # CREATING CONNECTIONS BETWEEN WIDGETS AND FUNCTIONS
        # ///////////////////////////////////////////////////////////////
        

        con = connect()
        con.dyn_conn(widgets, self)




    # SELECT WIDGETS
    # ///////////////////////////////////////////////////////////////

    def buttonClick(self):

        # GET BUTTON CLICKED
        btn     = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            BASE_Functions.resetStyle(self, btnName)
            btn.setStyleSheet(BASE_Functions.selectMenu(btn.styleSheet()))

        # SHOW DYNAMIC PAGE
        if btnName == "btn_dynamic":
            widgets.stackedWidget.setCurrentWidget(widgets.dvp)
            BASE_Functions.resetStyle(self, btnName)
            btn.setStyleSheet(BASE_Functions.selectMenu(btn.styleSheet()))

        # SHOW STATIC PAGE
        if btnName == "btn_static":
            widgets.stackedWidget.setCurrentWidget(widgets.STATIC)
            BASE_Functions.resetStyle(self, btnName)
            btn.setStyleSheet(BASE_Functions.selectMenu(btn.styleSheet()))
        
        # SHOW DYNAMIC_STATIC PAGE
        if btnName == "btn_dynamic_static":
            widgets.stackedWidget.setCurrentWidget(widgets.DYNAMIC_STATIC)
            BASE_Functions.resetStyle(self, btnName)
            btn.setStyleSheet(BASE_Functions.selectMenu(btn.styleSheet()))

        # SHOW NETWORK PAGE
        if btnName == "btn_network":
            widgets.stackedWidget.setCurrentWidget(widgets.NETWORK)
            BASE_Functions.resetStyle(self, btnName)
            btn.setStyleSheet(BASE_Functions.selectMenu(btn.styleSheet()))



    
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        BASE_Functions.resize_grips(self)


    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS 
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:/Users/Scarlet/Desktop/Tool/assets/icons/logo.png"))
    window = MainWindow()
    sys.exit(app.exec())

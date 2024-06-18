import sys, os, platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from Modules import *
# from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%






def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)










# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ///---------------------------------------------------------- INITIALIZE GLOBAL WIDGETS -----------------------------------------------------------///
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        self.setWindowTitle("Data Analysis Tool")
        widgets.titleRightInfo.setText("Data Analysis Tool")

        UIFunctions.constructor(self) 
        
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True)) # TOGGLE MENU        
        UIFunctions.uiDefinitions(self)                                                  # SET UI DEFINITIONS

        widgets.btn_home.clicked.connect(self.buttonClick)     # HOME
        widgets.btn_dynamic.clicked.connect(self.buttonClick)  # DYNAMIC
        

        self.show() 

        UIFunctions.theme(self, resource_path('assets/albino_light_theme.qss'), True)

        widgets.stackedWidget.setCurrentWidget(widgets.home)      


        # ========================================================================================================================================================================
        # ===                                                                                                                                                                  ===
        # ===                                                                              DYNAMIC                                                                             ===
        # ===                                                                                                                                                                  ===
        # ========================================================================================================================================================================
        

        widgets.data_match_local_search_button.clicked.connect(lambda: UIFunctions.data_match_local_search_button_function(self))
        widgets.dvp_search_file_button.clicked.connect(lambda: UIFunctions.dvp_sf_button_function(self))
        widgets.dvp_read_file_button.clicked.connect(lambda: UIFunctions.dvp_read_file_button_function(self))

        widgets.vars_search.clicked.connect(lambda: UIFunctions.processed_open_button_function(self))
        widgets.instavel.clicked.connect(lambda: UIFunctions.instavel_button(self))
        widgets.estavel.clicked.connect(lambda: UIFunctions.estavel_button(self))















    def buttonClick(self):

        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW DYNAMIC PAGE
        if btnName == "btn_dynamic":
            widgets.stackedWidget.setCurrentWidget(widgets.dvp)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    
    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
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

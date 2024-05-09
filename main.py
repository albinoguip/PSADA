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
        widgets.btn_dvp.clicked.connect(self.buttonClick)      # SS DVP
        widgets.btn_dec.clicked.connect(self.buttonClick)      # DELAY COMP
        widgets.btn_dec_inca.clicked.connect(self.buttonClick) # DELAY COMP
        widgets.btn_idi.clicked.connect(self.buttonClick)      # SWEEP CURRENT
        # widgets.btn_idi_inca.clicked.connect(self.buttonClick) # SWEEP CURRENT
        widgets.btn_ddi.clicked.connect(self.buttonClick)      # SWEEP CURRENT
        widgets.btn_temp.clicked.connect(self.buttonClick)     # SWEEP CURRENT

        # widgets.btn_dvpd.clicked.connect(self.buttonClick)  # SWEEP CURRENT
        

        self.show() 

        UIFunctions.theme(self, resource_path('assets/albino_light_theme.qss'), True)

        widgets.stackedWidget.setCurrentWidget(widgets.home)      


    def buttonClick(self):

        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW DVP PAGE
        if btnName == "btn_dvp":
            widgets.stackedWidget.setCurrentWidget(widgets.dvp)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW IdIq PAGE
        if btnName == "btn_idi":
            widgets.stackedWidget.setCurrentWidget(widgets.idq)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW IdIq PAGE
        if btnName == "btn_idi_inca":
            widgets.stackedWidget.setCurrentWidget(widgets.idq_inca)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW DELAY COMP PAGE
        if btnName == "btn_dec":
            widgets.stackedWidget.setCurrentWidget(widgets.delay)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW DELAY COMP PAGE
        if btnName == "btn_dec_inca":
            widgets.stackedWidget.setCurrentWidget(widgets.delay_inca)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW IdIq PAGE
        if btnName == "btn_ddi":
            widgets.stackedWidget.setCurrentWidget(widgets.ddi)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW IdIq PAGE
        if btnName == "btn_temp":
            widgets.stackedWidget.setCurrentWidget(widgets.temp)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))




        # # SHOW IdIq PAGE
        # if btnName == "btn_dvpd":
        #     widgets.stackedWidget.setCurrentWidget(widgets.dvpd)
        #     UIFunctions.resetStyle(self, btnName)
        #     btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        



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

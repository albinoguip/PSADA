from main import *
from PySide6.QtCore    import *
from PySide6.QtGui     import *
from PySide6.QtWidgets import *

from Modules.UIWidgets.custom_grips import *
from Modules.UIWidgets.Help_Widgets import *

import shutil, json

from win32com.shell import shell, shellcon 



from PowerSystemsAnalysis import *

import os, glob, shutil

from tqdm import tqdm
import pandas as pd




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///----------------------------------------------------------------- HELP FUNCTION ----------------------------------------------------------------///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)





def help_concat(path):

    with open(path, "r") as f:
        lines, skiprows = f.readlines(), []
        for idx, line in enumerate(lines[1:]):
            try:
                int(line.split(',')[0])
            except:
                skiprows.append(idx+1)

    name = path.split('/')[-1].split('.')[0]


    # Read File

    if ('.csv' in path) or ('.CSV' in path):
        raw_data = pd.read_csv(path, skiprows=skiprows)

    elif ('.dat' in path) or ('.DAT' in path):
        raw_data = pd.read_csv(path, skiprows=skiprows)

    elif ('.xlsx' in path) or ('.XLSX' in path):
        raw_data = pd.read_excel(path, skiprows=skiprows)

    else:
        print('\n---> The file must be .csv or .dat\n')

    return raw_data






GLOBAL_STATE = False

class BASE_Functions(MainWindow):

    def __init__(self, ui):
        
        pass

        
    def actionSave_function(self):

        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        file_path  = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_dvp.pdf'

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.pdf);;All files(*.*)")
        save_path    = save_path.split('.')[0]

        shutil.copyfile(file_path, save_path + '.pdf')

        print(save_path.split('/')[:-1])

        n = ''
        for a in save_path.split('/')[:-1]:
            n += a + '/'

        self.DP.excel(n, names=[path.split('/')[-1].split('.')[0] for path in self.file_names_dvp])


    def dvp_actionZoom_In_function(self):

        factor = self.ui.pdfView_dvp.zoomFactor() * 2
        self.ui.pdfView_dvp.setZoomFactor(factor)

    
    def dvp_actionZoom_Out_function(self):

        factor = self.ui.pdfView_dvp.zoomFactor() / 2
        self.ui.pdfView_dvp.setZoomFactor(factor)

    def dvp_actionPage_down_function(self):

        nav = self.ui.pdfView_dvp.pageNavigator()
        nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    def dvp_actionPage_up_function(self):

        nav = self.ui.pdfView_dvp.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())






    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # MAXIMIZE/RESTORE
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # IMPORT THEMES FILES QSS/CSS
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # START - GUI DEFINITIONS
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: BASE_Functions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if True:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if GLOBAL_STATE:
                    BASE_Functions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: BASE_Functions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if True:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # TOGGLE MENU
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = 210
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # SELECT/DESELECT MENU

    # SELECT
    def selectMenu(getStyle):
        MENU_SELECTED_STYLESHEET = """
                border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
                background-color: rgb(40, 44, 52);
                """
        
        select = getStyle + MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        MENU_SELECTED_STYLESHEET = """
                border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
                background-color: rgb(40, 44, 52);
                """
        
        deselect = getStyle.replace(MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(BASE_Functions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(BASE_Functions.deselectMenu(w.styleSheet()))
from PySide6.QtCore       import *
from PySide6.QtGui        import *
from PySide6.QtWidgets    import *
from PySide6.QtCharts     import *
from PySide6.QtPdfWidgets import *
from PySide6.QtPdf        import *

from Modules.Help_Widgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

# from Backend import *

import pandas as pd

import os, sys







def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)









class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))

        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        


        self._basic_window()
        self._create_left_menu()
        self._create_logo()
        self._create_toggle_box()
        self._create_buttons()
        

        self.leftMenuBg_vert_layout.addWidget(self.leftMenuFrame)
        self.appLayout.addWidget(self.leftMenuBg)


        # self.teste2 = QLabel(self.bgApp)
        # self.teste2.setStyleSheet(u"background-color: rgb(0, 37, 43)")
        # self.appLayout.addWidget(self.teste2)


        self._create_content_box()
        self._create_up_bar()
        self._create_page_container()
        self._create_home()

        self._create_dvp()
        

        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.resto()


        self.pdf = None



        # self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)

        self.appLayout.addWidget(self.contentBox)

        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)



    def update_plot(self):

        self.ydata = [0, 1, 2, 3, 4]
        self.xdata = [0, 1, 2, 3, 4]
        self.sc.axes.cla()
        self.sc.axes.plot(self.xdata, self.ydata, 'r')

        self.sc.draw()

    def _basic_window(self):

        self.font0 = QFont()
        self.font0.setFamily(u"Segoe UI")
        self.font0.setPointSize(10)
        self.font0.setBold(False)
        self.font0.setItalic(False)
        self.styleSheet.setFont(self.font0)
        
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)

        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)

        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)

    def _create_left_menu(self):

        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)

        self.leftMenuBg_vert_layout = QVBoxLayout(self.leftMenuBg)
        self.leftMenuBg_vert_layout.setSpacing(0)
        self.leftMenuBg_vert_layout.setObjectName(u"leftMenuBg_vert_layout")
        self.leftMenuBg_vert_layout.setContentsMargins(0, 0, 0, 0)

    def _create_logo(self):

        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        # self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        # self.topLogoInfo.setFrameShadow(QFrame.Raised)

        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        # self.topLogo.setFrameShape(QFrame.NoFrame)
        # self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        # self.titleLeftApp.setStyleSheet(u"background-color: rgb(100, 180, 150)")
        # self.verticalLayout_3.addWidget(self.teste3)

        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)



        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.leftMenuBg_vert_layout.addWidget(self.topLogoInfo)

    def _create_toggle_box(self):
        
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")

        self.toggleLabel= QLabel(self.toggleBox)
        # self.toggleLabel.setStyleSheet(u"background-color: rgb(150, 255, 150)")


        self.sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(self.sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(self.font0)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(./images/MENU.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.verticalLayout_4.addWidget(self.toggleLabel)

        self.verticalMenuLayout.addWidget(self.toggleBox)

    def _create_buttons(self):

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        self.sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(self.sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(self.font0)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(./images/HOME.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        ### 1) DVP 

        self.btn_dynamic = QPushButton(self.topMenu)
        self.btn_dynamic.setObjectName(u"btn_dynamic")
        self.sizePolicy.setHeightForWidth(self.btn_dynamic.sizePolicy().hasHeightForWidth())
        self.btn_dynamic.setSizePolicy(self.sizePolicy)
        self.btn_dynamic.setMinimumSize(QSize(0, 45))
        self.btn_dynamic.setFont(self.font0)
        self.btn_dynamic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dynamic.setLayoutDirection(Qt.LeftToRight)
        self.btn_dynamic.setStyleSheet(u"background-image: url(./images/1.png); color: black;")
        self.verticalLayout_8.addWidget(self.btn_dynamic)
     

        

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

    def _create_botton_menu(self):

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        self.sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(self.sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(self.font0)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(./assets/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)

    def _create_content_box(self):

        # CONTENT BOX (RIGHT)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # CONTENT BOTTON

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

    def _create_up_bar(self):

        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(self.font0)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/icon_restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

    def _create_page_container(self):

        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

    def _create_home(self):

        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(./assets/logo_expands.png);\n"
                                 "background-position: center;\n"
                                 "background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)



### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





    def _create_dvp(self):

        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(120)
        font1.setBold(True)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)

        self.dvp = QWidget()
        self.dvp.setObjectName(u"dvp")
        self.dvp.setStyleSheet(u"b")

        self.mainLayout_dvp = QHBoxLayout(self.dvp)
        self.mainLayout_dvp.setSpacing(10)
        self.mainLayout_dvp.setObjectName(u"mainLayout_dvp")
        self.mainLayout_dvp.setContentsMargins(10, 10, 10, 10)

        # === ESQUERDA

        self.infos_dvp = QFrame(self.dvp)
        self.infos_dvp.setObjectName(u"row_1")
        self.infos_dvp.setFrameShape(QFrame.StyledPanel)
        self.infos_dvp.setFrameShadow(QFrame.Raised)
        self.infos_dvp.setMinimumWidth(800)

        self.verticalLayout_dvp = QVBoxLayout(self.infos_dvp)
        self.verticalLayout_dvp.setSpacing(10)
        self.verticalLayout_dvp.setObjectName(u"verticalLayout_dvp")
        self.verticalLayout_dvp.setContentsMargins(10, 10, 10, 10)

        # ROW 1

        self.row_1_dvp = QFrame(self.infos_dvp)
        self.row_1_dvp.setObjectName(u"row_1_dvp")
        self.row_1_dvp.setFrameShape(QFrame.StyledPanel)
        self.row_1_dvp.setFrameShadow(QFrame.Raised)
        self.row_1_dvp.setMaximumHeight(150)

        self.LG_row_1_dvp = QGridLayout(self.row_1_dvp)
        self.LG_row_1_dvp.setSpacing(5)
        self.LG_row_1_dvp.setObjectName(u"LG_row_1_dvp")
        self.LG_row_1_dvp.setContentsMargins(0, 0, 1, 1)




        self.data_match_local_search_button = QPushButton(self.row_1_dvp)
        self.data_match_local_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.data_match_local_search_button.setText("Search")
        self.LG_row_1_dvp.addWidget(self.data_match_local_search_button, 0, 0, 1, 2)

        self.data_match_qline_files = QLineEdit(self.row_1_dvp)
        self.data_match_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_1_dvp.addWidget(self.data_match_qline_files, 0, 2, 1, 8)






        self.dvp_search_file_button = QPushButton(self.row_1_dvp)
        self.dvp_search_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.dvp_search_file_button.setText("Select")
        self.LG_row_1_dvp.addWidget(self.dvp_search_file_button, 1, 0, 1, 2)

        self.dvp_qline_files = QLineEdit(self.row_1_dvp)
        self.dvp_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_1_dvp.addWidget(self.dvp_qline_files, 1, 2, 1, 8)

        self.dvp_read_file_button = QPushButton(self.row_1_dvp)
        self.dvp_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.dvp_read_file_button.setText("Process")
        self.LG_row_1_dvp.addWidget(self.dvp_read_file_button, 0, 10, 2, 2)


        self.verticalLayout_dvp.addWidget(self.row_1_dvp)





        self.row_2_dvp = QFrame(self.infos_dvp)
        self.row_2_dvp.setObjectName(u"row_3_dvp")
        self.row_2_dvp.setFrameShape(QFrame.StyledPanel)
        self.row_2_dvp.setFrameShadow(QFrame.Raised)

        self.LG_row_2_dvp = QGridLayout(self.row_2_dvp)
        self.LG_row_2_dvp.setSpacing(5)
        self.LG_row_2_dvp.setObjectName(u"LG_row_3_dvp")
        self.LG_row_2_dvp.setContentsMargins(0, 0, 1, 1)


        self.vars_search = QPushButton(self.row_2_dvp)
        self.vars_search.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.vars_search.setText("Processed")
        self.LG_row_2_dvp.addWidget(self.vars_search, 2, 0, 1, 2)

        self.vars_qline = QLineEdit(self.row_2_dvp)
        self.vars_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_2_dvp.addWidget(self.vars_qline, 2, 2, 1, 10)




        self.instavel = QPushButton(self.row_2_dvp)
        self.instavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.instavel.setText("Instável")
        self.LG_row_2_dvp.addWidget(self.instavel, 3, 0, 1, 6)

        self.estavel = QPushButton(self.row_2_dvp)
        self.estavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.estavel.setText("Estável")
        self.LG_row_2_dvp.addWidget(self.estavel, 3, 6, 1, 6)




        self.verticalLayout_dvp.addWidget(self.row_2_dvp)

        
        # self.mainLayout_dvp.addWidget(self.pdf_dvp)



        # ROW 3

        self.row_3_dvp = QFrame(self.infos_dvp)
        self.row_3_dvp.setObjectName(u"row_3_dvp")
        self.row_3_dvp.setFrameShape(QFrame.StyledPanel)
        self.row_3_dvp.setFrameShadow(QFrame.Raised)

        self.LG_row_3_dvp = QGridLayout(self.row_3_dvp)
        self.LG_row_3_dvp.setSpacing(5)
        self.LG_row_3_dvp.setObjectName(u"LG_row_3_dvp")
        self.LG_row_3_dvp.setContentsMargins(0, 0, 1, 1)






        
        self.dvp_concatenate = QPushButton(self.row_3_dvp)
        self.dvp_concatenate.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.dvp_concatenate.setText("Concatenate")
        self.LG_row_3_dvp.addWidget(self.dvp_concatenate, 0, 0, 1, 2)

        self.dvp_select_data = QComboBox(self.row_3_dvp)
        # self.dvp_select_data.addItems(plots_list.keys())
        self.dvp_select_data.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_3_dvp.addWidget(self.dvp_select_data, 0, 2, 1, 3)


        self.dvp_select_plot = QComboBox(self.row_3_dvp)
        # self.dvp_select_plot.addItems(plots_list.keys())
        self.dvp_select_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_3_dvp.addWidget(self.dvp_select_plot, 1, 0, 1, 2)

        self.speed_select = QComboBox(self.row_3_dvp)
        # self.speed_select.addItems(['None', '+', '-'])
        self.speed_select.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_3_dvp.addWidget(self.speed_select, 1, 2, 1, 1)

        self.dvp_see_plot = QPushButton(self.row_3_dvp)
        self.dvp_see_plot.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.dvp_see_plot.setText("Plot")
        self.LG_row_3_dvp.addWidget(self.dvp_see_plot, 1, 3, 1, 2)

        # ===================================================================================

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        self.toolbar = NavigationToolbar2QT(self.sc)

        self.LG_row_3_dvp.addWidget(self.toolbar, 2, 0, 1, 5)
        self.LG_row_3_dvp.addWidget(self.sc     , 3, 0, 3, 5)

        # ===================================================================================
        self.verticalLayout_dvp.addWidget(self.row_3_dvp)

        # ROW 4

        self.row_4_dvp = QFrame(self.infos_dvp)
        self.row_4_dvp.setObjectName(u"row_3_dvp")
        self.row_4_dvp.setFrameShape(QFrame.StyledPanel)
        self.row_4_dvp.setFrameShadow(QFrame.Raised)
        self.row_4_dvp.setMaximumHeight(100)

        self.LG_row_4_dvp = QGridLayout(self.row_4_dvp)
        self.LG_row_4_dvp.setSpacing(5)
        self.LG_row_4_dvp.setObjectName(u"LG_row_3_dvp")
        self.LG_row_4_dvp.setContentsMargins(0, 0, 1, 1)


        self.dvp_combo_variable = ExtendedComboBox(self.row_4_dvp)
        self.dvp_combo_variable.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_4_dvp.addWidget(self.dvp_combo_variable, 0, 0, 1, 2)

        self.dvp_combo_sinal = QComboBox(self.row_4_dvp)
        self.dvp_combo_sinal.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_4_dvp.addWidget(self.dvp_combo_sinal, 0, 2, 1, 2)


        self.dvp_label_value = QLineEdit(self.row_4_dvp)
        self.dvp_label_value.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        self.LG_row_4_dvp.addWidget(self.dvp_label_value, 0, 4, 1, 2)

        self.dvp_button_apply_filter = QPushButton(self.row_4_dvp)
        self.dvp_button_apply_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.dvp_button_apply_filter.setText("Apply Filter")
        self.LG_row_4_dvp.addWidget(self.dvp_button_apply_filter, 0, 6, 1, 2)
 



        self.verticalLayout_dvp.addWidget(self.row_4_dvp)

        self.mainLayout_dvp.addWidget(self.infos_dvp)

        # === DIREITA

        self.pdf_dvp = QFrame(self.dvp)
        self.pdf_dvp.setObjectName(u"row_1")
        # self.pdf_dvp.setMinimumSize(QSize(600, 110))
        self.pdf_dvp.setFrameShape(QFrame.StyledPanel)
        self.pdf_dvp.setFrameShadow(QFrame.Raised)

        self.verticalLayout_pdf_dvp = QVBoxLayout(self.pdf_dvp)
        self.verticalLayout_pdf_dvp.setSpacing(10)
        self.verticalLayout_pdf_dvp.setObjectName(u"verticalLayout_pdf_dvp")
        self.verticalLayout_pdf_dvp.setContentsMargins(10, 10, 10, 10)

        # # ROW 2

        # self.row_2_dvp = QFrame(self.pdf_dvp)
        # self.row_2_dvp.setObjectName(u"row_2_dvp")
        # # self.row_2_dvp.setMinimumSize(QSize(500, 110))
        # self.row_2_dvp.setFrameShape(QFrame.StyledPanel)
        # self.row_2_dvp.setFrameShadow(QFrame.Raised)
        # # self.row_2_dvp.setMaximumHeight(100)

        # self.LG_row_2_dvp = QGridLayout(self.row_2_dvp)
        # self.LG_row_2_dvp.setSpacing(5)
        # self.LG_row_2_dvp.setObjectName(u"LG_row_2_dvp")
        # self.LG_row_2_dvp.setContentsMargins(0, 0, 1, 1)


        # # 00
        # self.dvp_infos00 = QLabel(self.row_2_dvp)
        # self.dvp_infos00.setObjectName(u"labelVersion_3")
        # self.dvp_infos00.setStyleSheet(u"color: rgb(10, 10, 10);")
        # self.dvp_infos00.setLineWidth(1)
        # self.dvp_infos00.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.LG_row_2_dvp.addWidget(self.dvp_infos00, 0, 0, 1, 1)
        # self.dvp_infos00_l = QLineEdit(self.row_1_dvp)
        # self.dvp_infos00_l.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.LG_row_2_dvp.addWidget(self.dvp_infos00_l, 0, 1, 1, 3)

        # # 01
        # self.dvp_infos01 = QLabel(self.row_2_dvp)
        # self.dvp_infos01.setObjectName(u"labelVersion_3")
        # self.dvp_infos01.setStyleSheet(u"color: rgb(10, 10, 10);")
        # self.dvp_infos01.setLineWidth(1)
        # self.dvp_infos01.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.LG_row_2_dvp.addWidget(self.dvp_infos01, 0, 4, 1, 1)
        # self.dvp_infos01_l = QLineEdit(self.row_1_dvp)
        # self.dvp_infos01_l.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.LG_row_2_dvp.addWidget(self.dvp_infos01_l, 0, 5, 1, 3)


        # # 10
        # self.dvp_infos10 = QLabel(self.row_2_dvp)
        # self.dvp_infos10.setObjectName(u"labelVersion_3")
        # self.dvp_infos10.setStyleSheet(u"color: rgb(10, 10, 10);")
        # self.dvp_infos10.setLineWidth(1)
        # self.dvp_infos10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.LG_row_2_dvp.addWidget(self.dvp_infos10, 1, 0, 1, 1)
        # self.dvp_infos10_l = QLineEdit(self.row_1_dvp)
        # self.dvp_infos10_l.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.LG_row_2_dvp.addWidget(self.dvp_infos10_l, 1, 1, 1, 3)

        # # 11
        # self.dvp_infos11 = QLabel(self.row_2_dvp)
        # self.dvp_infos11.setObjectName(u"labelVersion_3")
        # self.dvp_infos11.setStyleSheet(u"color: rgb(10, 10, 10);")
        # self.dvp_infos11.setLineWidth(1)
        # self.dvp_infos11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.LG_row_2_dvp.addWidget(self.dvp_infos11, 1, 4, 1, 1)
        # self.dvp_infos11_l = QLineEdit(self.row_1_dvp)
        # self.dvp_infos11_l.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.LG_row_2_dvp.addWidget(self.dvp_infos11_l, 1, 5, 1, 3)

        # # 20
        # self.dvp_infos20 = QLabel(self.row_2_dvp)
        # self.dvp_infos20.setObjectName(u"labelVersion_3")
        # self.dvp_infos20.setStyleSheet(u"color: rgb(10, 10, 10);")
        # self.dvp_infos20.setLineWidth(1)
        # self.dvp_infos20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.LG_row_2_dvp.addWidget(self.dvp_infos20, 2, 0, 1, 1)
        # self.dvp_infos20_l = QLineEdit(self.row_1_dvp)
        # self.dvp_infos20_l.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.LG_row_2_dvp.addWidget(self.dvp_infos20_l, 2, 1, 1, 3)

        # # 21
        # self.dvp_infos21 = QLabel(self.row_2_dvp)
        # self.dvp_infos21.setObjectName(u"labelVersion_3")
        # self.dvp_infos21.setStyleSheet(u"color: rgb(10, 10, 10);")
        # self.dvp_infos21.setLineWidth(1)
        # self.dvp_infos21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.LG_row_2_dvp.addWidget(self.dvp_infos21, 2, 4, 1, 1)
        # self.dvp_infos21_l = QLineEdit(self.row_1_dvp)
        # self.dvp_infos21_l.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.LG_row_2_dvp.addWidget(self.dvp_infos21_l, 2, 5, 1, 3)


        # # 3-
        # self.dvp_infos30 = QLabel(self.row_2_dvp)
        # self.dvp_infos30.setObjectName(u"labelVersion_3")
        # self.dvp_infos30.setStyleSheet(u"color: rgb(10, 10, 10);")
        # self.dvp_infos30.setLineWidth(1)
        # self.dvp_infos30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        # self.LG_row_2_dvp.addWidget(self.dvp_infos30, 3, 0, 1, 1)
        # self.dvp_infos30_l = QLineEdit(self.row_1_dvp)
        # self.dvp_infos30_l.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.LG_row_2_dvp.addWidget(self.dvp_infos30_l, 4, 0, 10, 8)



        # self.verticalLayout_pdf_dvp.addWidget(self.row_2_dvp)

















        self.d_row_1_dvp = QFrame(self.pdf_dvp)
        self.d_row_1_dvp.setObjectName(u"d_row_1_dvp")
        self.d_row_1_dvp.setFrameShape(QFrame.StyledPanel)
        self.d_row_1_dvp.setFrameShadow(QFrame.Raised)
        self.d_row_1_dvp.setMaximumHeight(600)
        # self.d_row_1_dvp.setMaximumSize(QSize(600, 400))

        self.d_LG_row_1_dvp = QGridLayout(self.d_row_1_dvp)
        self.d_LG_row_1_dvp.setSpacing(0)
        self.d_LG_row_1_dvp.setObjectName(u"d_LG_row_1_dvp")
        self.d_LG_row_1_dvp.setContentsMargins(0, 0, 1, 1)

        ## ============================


        self.pdfView_dvp = QPdfView(self.pdf_dvp)
        self.pdfView_dvp.setObjectName(u"pdfView_dvp")

        self.m_document = QPdfDocument(self.pdf_dvp)

        self.pdfView_dvp.setDocument(self.m_document)


        ## ============================



        self.mainToolBar = QToolBar(self.d_row_1_dvp)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setFloatable(False)


        # ACTIONS


        self.run_dvp = QPushButton(self.d_row_1_dvp)
        self.run_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        self.run_dvp.setText("Run")

        self.actionZoom_In_dvp = QPushButton(self.d_row_1_dvp)
        self.actionZoom_In_dvp.setText('In')
        self.actionZoom_In_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        self.actionZoom_Out = QPushButton(self.d_row_1_dvp)
        self.actionZoom_Out.setText('Out')
        self.actionZoom_Out.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        self.m_zoomSelector = ZoomSelector(self.d_row_1_dvp)
        self.m_zoomSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # self.m_zoomSelector.setMaximumWidth(150)
        self.m_zoomSelector.zoom_mode_changed.connect(self.pdfView_dvp.setZoomMode)
        self.m_zoomSelector.zoom_factor_changed.connect(self.pdfView_dvp.setZoomFactor)
        self.m_zoomSelector.reset()
        self.pdfView_dvp.zoomFactorChanged.connect(self.m_zoomSelector.set_zoom_factor)

        self.actionPage_down_dvp = QPushButton(self.d_row_1_dvp)
        self.actionPage_down_dvp.setText('-')
        self.actionPage_down_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        self.actionPage_up_dvp = QPushButton(self.d_row_1_dvp)
        self.actionPage_up_dvp.setText('+')
        self.actionPage_up_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        self.m_pageSelector = QSpinBox(self.d_row_1_dvp)
        self.m_pageSelector.valueChanged.connect(self.page_selected)
        self.m_pageSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        nav = self.pdfView_dvp.pageNavigator()
        nav.currentPageChanged.connect(self.m_pageSelector.setValue)
        # nav.backAvailableChanged.connect(self.actionBack.setEnabled)
        # nav.forwardAvailableChanged.connect(self.actionForward.setEnabled)

        self.actionSave = QPushButton(self.d_row_1_dvp)
        self.actionSave.setText('Save')
        self.actionSave.setStyleSheet(u"background-color: rgb(91, 95, 199)")





        self.mainToolBar.addWidget(self.run_dvp)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addWidget(self.actionZoom_In_dvp)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addWidget(self.m_zoomSelector)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addWidget(self.actionZoom_Out)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addWidget(self.actionPage_down_dvp)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addWidget(self.m_pageSelector)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addWidget(self.actionPage_up_dvp)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addWidget(self.actionSave)




        ## =============


        self.d_LG_row_1_dvp.addWidget(self.mainToolBar, 0, 0, 1, 1)
        self.d_LG_row_1_dvp.addWidget(self.pdfView_dvp, 1, 0, 1, 1)

        self.verticalLayout_pdf_dvp.addWidget(self.d_row_1_dvp)
        self.mainLayout_dvp.addWidget(self.pdf_dvp)






        

        # ADD ALL

        self.stackedWidget.addWidget(self.dvp)



    def resto(self):

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        self.sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(self.sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(self.font0)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(./assets/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        self.sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(self.sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(self.font0)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(./assets/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        self.sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(self.sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(self.font0)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(./assets/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content) ### ==============================================================


        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data Analysis Tool", None))

        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Data Analysis Tool", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Unicamp", None))

        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_dynamic.setText(QCoreApplication.translate("MainWindow", u"Dynamic", None))




        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)


    
        # self.data_match_local.setText(QCoreApplication.translate("MainWindow", u"Data Match:", None))
        # self.dvp_label_local.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        # self.dvp_label_ptc.setText(QCoreApplication.translate("MainWindow", u"PTC:", None))

        # self.dvp_infos00.setText(QCoreApplication.translate("MainWindow", u"Cell:", None))
        # self.dvp_infos01.setText(QCoreApplication.translate("MainWindow", u"Engineer:", None))
        # self.dvp_infos10.setText(QCoreApplication.translate("MainWindow", u"Software:", None))
        # self.dvp_infos11.setText(QCoreApplication.translate("MainWindow", u"Motor:", None))
        # self.dvp_infos20.setText(QCoreApplication.translate("MainWindow", u"PIM:", None))
        # self.dvp_infos21.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        # self.dvp_infos30.setText(QCoreApplication.translate("MainWindow", u"Comments:", None))


        # self.delay_infos00.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        # self.delay_infos01.setText(QCoreApplication.translate("MainWindow", u"Torque:", None))
        # self.delay_infos10.setText(QCoreApplication.translate("MainWindow", u"Id Cmd:", None))
        # self.delay_infos11.setText(QCoreApplication.translate("MainWindow", u"Iq Cmd:", None))
        # self.delay_infos20.setText(QCoreApplication.translate("MainWindow", u"Imag1:", None))
        # self.delay_infos21.setText(QCoreApplication.translate("MainWindow", u"Imag2:", None))


        # self.delay_inca_infos00.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        # self.delay_inca_infos01.setText(QCoreApplication.translate("MainWindow", u"Torque:", None))
        # self.delay_inca_infos10.setText(QCoreApplication.translate("MainWindow", u"Id FB:", None))
        # self.delay_inca_infos11.setText(QCoreApplication.translate("MainWindow", u"Iq FB:", None))
        # self.delay_inca_infos20.setText(QCoreApplication.translate("MainWindow", u"Id Filt:", None))
        # self.delay_inca_infos21.setText(QCoreApplication.translate("MainWindow", u"Iq Filt:", None))
        # self.delay_inca_infos30.setText(QCoreApplication.translate("MainWindow", u"Imag1:", None))
        # self.delay_inca_infos31.setText(QCoreApplication.translate("MainWindow", u"Imag2:", None))


        # self.idq_infos00.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        # self.idq_infos01.setText(QCoreApplication.translate("MainWindow", u"Torque:", None))
        # self.idq_infos10.setText(QCoreApplication.translate("MainWindow", u"Id Cmd:", None))
        # self.idq_infos11.setText(QCoreApplication.translate("MainWindow", u"Iq Cmd:", None))
        # self.idq_infos20.setText(QCoreApplication.translate("MainWindow", u"Id FB:", None))
        # self.idq_infos21.setText(QCoreApplication.translate("MainWindow", u"Iq FB:", None))
        # self.idq_infos30.setText(QCoreApplication.translate("MainWindow", u"Ud FB:", None))
        # self.idq_infos31.setText(QCoreApplication.translate("MainWindow", u"Uq FB:", None))
        # self.idq_infos40.setText(QCoreApplication.translate("MainWindow", u"ModIndex:", None))
        # self.idq_infos41.setText(QCoreApplication.translate("MainWindow", u"Vdc:", None))


        


        # self.ddi_infos00.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        # self.ddi_infos01.setText(QCoreApplication.translate("MainWindow", u"Torque:", None))
        # self.ddi_infos10.setText(QCoreApplication.translate("MainWindow", u"Id Cmd:", None))
        # self.ddi_infos11.setText(QCoreApplication.translate("MainWindow", u"Iq Cmd:", None))
        # self.ddi_infos20.setText(QCoreApplication.translate("MainWindow", u"Id FB:", None))
        # self.ddi_infos21.setText(QCoreApplication.translate("MainWindow", u"Iq FB:", None))
        # self.ddi_infos30.setText(QCoreApplication.translate("MainWindow", u"Ud FB:", None))
        # self.ddi_infos31.setText(QCoreApplication.translate("MainWindow", u"Uq FB:", None))
        # self.ddi_infos40.setText(QCoreApplication.translate("MainWindow", u"ModIndex:", None))
        # self.ddi_infos41.setText(QCoreApplication.translate("MainWindow", u"Vdc:", None))


        # self.dvpd_infos00.setText(QCoreApplication.translate("MainWindow", u"Speed:", None))
        # self.dvpd_infos01.setText(QCoreApplication.translate("MainWindow", u"Torque:", None))
        # self.dvpd_infos10.setText(QCoreApplication.translate("MainWindow", u"Id Cmd:", None))
        # self.dvpd_infos11.setText(QCoreApplication.translate("MainWindow", u"Iq Cmd:", None))
        # self.dvpd_infos20.setText(QCoreApplication.translate("MainWindow", u"Id FB:", None))
        # self.dvpd_infos21.setText(QCoreApplication.translate("MainWindow", u"Iq FB:", None))
        # self.dvpd_infos30.setText(QCoreApplication.translate("MainWindow", u"Ud FB:", None))
        # self.dvpd_infos31.setText(QCoreApplication.translate("MainWindow", u"Uq FB:", None))
        # self.dvpd_infos40.setText(QCoreApplication.translate("MainWindow", u"ModIndex:", None))
        # self.dvpd_infos41.setText(QCoreApplication.translate("MainWindow", u"Vdc:", None))


        # self.temp_infos00.setText(QCoreApplication.translate("MainWindow", u"Volt Breakpoints:", None))
        # self.temp_infos01.setText(QCoreApplication.translate("MainWindow", u"Corner Speeds:", None))
        # self.temp_infos10.setText(QCoreApplication.translate("MainWindow", u"Max Volt:", None))
        # self.temp_infos11.setText(QCoreApplication.translate("MainWindow", u"Back EMF:", None))
        # self.temp_infos20.setText(QCoreApplication.translate("MainWindow", u"Peak Torque:", None))
        # self.temp_infos21.setText(QCoreApplication.translate("MainWindow", u"Continuous Torque Target:", None))
        # self.temp_infos30.setText(QCoreApplication.translate("MainWindow", u"Corner Speed (Max Volt):", None))
        # self.temp_infos31.setText(QCoreApplication.translate("MainWindow", u"RPM Step:", None))
        # self.temp_infos40.setText(QCoreApplication.translate("MainWindow", u"RPM Begin", None))
        # self.temp_infos41.setText(QCoreApplication.translate("MainWindow", u"RPM End:", None))
        # self.temp_infos50.setText(QCoreApplication.translate("MainWindow", u"Torque Breakpoints:", None))

        # self.ddi_infos00.setText(QCoreApplication.translate("MainWindow", u"00:", None))
        # self.ddi_infos01.setText(QCoreApplication.translate("MainWindow", u"01:", None))
        # self.ddi_infos02.setText(QCoreApplication.translate("MainWindow", u"02:", None))
        
        # self.ddi_infos10.setText(QCoreApplication.translate("MainWindow", u"10:", None))
        # self.ddi_infos11.setText(QCoreApplication.translate("MainWindow", u"11:", None))
        # self.ddi_infos12.setText(QCoreApplication.translate("MainWindow", u"12:", None))
        # self.ddi_infos13.setText(QCoreApplication.translate("MainWindow", u"13:", None))

        # self.ddi_infos20.setText(QCoreApplication.translate("MainWindow", u"20:", None))
        # self.ddi_infos21.setText(QCoreApplication.translate("MainWindow", u"21:", None))
        # self.ddi_infos22.setText(QCoreApplication.translate("MainWindow", u"22:", None))
        # self.ddi_infos23.setText(QCoreApplication.translate("MainWindow", u"23:", None))

        # self.ddi_infos_actual.setText(QCoreApplication.translate("MainWindow", u"Back-Emf Type:", None))
        # self.ddi_infos_target.setText(QCoreApplication.translate("MainWindow", u"Back-Emf Target:", None))
        


    @Slot(QUrl)
    def open(self, doc_location):
        if doc_location.isLocalFile():

            print(doc_location.toLocalFile())
            self.m_document.load(doc_location.toLocalFile())
            document_title = self.m_document.metaData(QPdfDocument.MetaDataField.Title)
            self.setWindowTitle(document_title if document_title else "PDF Viewer")
            self.page_selected(0)
            self.m_pageSelector.setMaximum(self.m_document.pageCount() - 1)
        else:
            message = f"{doc_location} is not a valid local file"
            print(message, file=sys.stderr)
            QMessageBox.critical(self, "Failed to open", message)

    @Slot(QModelIndex)
    def bookmark_selected(self, index):
        if not index.isValid():
            return
        page = index.data(int(QPdfBookmarkModel.Role.Page))
        zoom_level = index.data(int(QPdfBookmarkModel.Role.Level))
        self.pdf.pageNavigator().jump(page, QPoint(), zoom_level)

    @Slot(int)
    def page_selected(self, page):
        nav = self.pdf.pageNavigator()
        nav.jump(page, QPoint(), nav.currentZoom())

    # DELAY COMP

    # @Slot(QModelIndex)
    # def bookmark_selected_delay(self, index):
    #     if not index.isValid():
    #         return
    #     page = index.data(int(QPdfBookmarkModel.Role.Page))
    #     zoom_level = index.data(int(QPdfBookmarkModel.Role.Level))
    #     self.pdfView_delay.pageNavigator().jump(page, QPoint(), zoom_level)

    # @Slot(int)
    # def page_selected_delay(self, page):
    #     nav = self.pdfView_delay.pageNavigator()
    #     nav.jump(page, QPoint(), nav.currentZoom())

    # @Slot()
    # def on_actionOpen_triggered(self):
    #     if not self.m_fileDialog:
    #         directory = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
    #         self.m_fileDialog = QFileDialog(self, "Choose a PDF", directory)
    #         self.m_fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
    #         self.m_fileDialog.setMimeTypeFilters(["application/pdf"])
    #     if self.m_fileDialog.exec() == QDialog.Accepted:
    #         to_open = self.m_fileDialog.selectedUrls()[0]
    #         if to_open.isValid():
    #             self.open(to_open)

    # @Slot()
    # def on_actionQuit_triggered(self):
    #     self.close()

    # @Slot()
    # def on_actionAbout_triggered(self):
    #     QMessageBox.about(self, "About PdfViewer",
    #                       "An example using QPdfDocument")

    # @Slot()
    # def on_actionAbout_Qt_triggered(self):
    #     QMessageBox.aboutQt(self)

    @Slot()
    def on_actionZoom_In_triggered(self):
        factor = self.pdfView.zoomFactor() * 2
        self.pdfView.setZoomFactor(factor)

    # @Slot()
    # def on_actionZoom_Out_triggered(self):
    #     factor = self.pdfView.zoomFactor() / 2
    #     self.pdfView.setZoomFactor(factor)

    # @Slot()
    # def on_actionPrevious_Page_triggered(self):
    #     nav = self.pdfView.pageNavigator()
    #     nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    # @Slot()
    # def on_actionNext_Page_triggered(self):
    #     nav = self.pdfView.pageNavigator()
    #     nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())

    # @Slot()
    # def on_actionContinuous_triggered(self):
    #     cont_checked = self.actionContinuous.isChecked()
    #     mode = QPdfView.PageMode.MultiPage if cont_checked else QPdfView.PageMode.SinglePage
    #     self.pdfView.setPageMode(mode)

    # @Slot()
    # def on_actionBack_triggered(self):
    #     self.pdfView.pageNavigator().back()

    # @Slot()
    # def on_actionForward_triggered(self):
    #     self.pdfView.pageNavigator().forward()
    


        

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from resources_rc import *

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")

        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                        "\n"
                                        "ALBINO'S THEME\n"
                                        "\n"
                                        "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
                                        "\n"
                                        "QWidget{\n"
                                        "	color: rgb(0, 0, 0);\n"
                                        "	font: 10pt \"Segoe UI\";\n"
                                        "}\n"
                                        "\n"
                                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                        "Tooltip */\n"
                                        "QToolTip {\n"
                                        "	color: #ffffff;\n"
                                        "	background-color: rgba(33, 37, 43, 180);\n"
                                        "	border: 1px solid rgb(44, 49, 58);\n"
                                        "	background-image: none;\n"
                                        "	background-position: left center;\n"
                                        "    background-repeat: no-repeat;\n"
                                        "	border: none;\n"
                                        "	border-left: 2px solid rgb(255, 121, 198);\n"
                                        "	text-align: left;\n"
                                        "	padding-left: 8px;\n"
                                        "	margin: 0px;\n"
                                        "}\n"
                                        "\n"
                                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                        "Bg App */\n"
                                        "#bgApp {	\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border: 1px solid rgb(44, 49, 58);\n"
                                        "}\n"
                                        "\n"
                                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
                                        "Left Menu */\n"
                                        "#leftMenuBg {	\n"
                                        "	background-color: rgb(36, 55, 130);\n"
                                        "}\n"
                                        "#topLogo {\n"
                                        "	background-color: rgb(36, 55, 130);\n"
                                        "	background-image: url(images/images/logo.png);\n"
                                        "	background-position: centered;\n"
                                        "	background-repeat: no-repeat;\n"
                                        "}\n"
                                        "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; color: rgb(255, 255, 255); }\n"
                                        "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(255, 255, 255); }\n"
                                        "\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"   background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"

"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"

"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"

"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
                                        "/* Toggle Button */\n"
                                        "#toggleButton {\n"
                                        "	background-position: left center;\n"
                                        "   background-repeat: no-repeat;\n"
                                        "	border: none;\n"
                                        "	border-left: 20px solid transparent;\n"
                                        "	background-color: rgb(36, 55, 130);\n"
                                        "	text-align: left;\n"
                                        "	padding-left: 44px;\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "#toggleButton:hover {\n"
                                        "	background-color: rgb(40, 44, 52);\n"
                                        "}\n"
                                        "#toggleButton:pressed {\n"
                                        "	background-color: rgb("
                                                                "189, 147, 249);\n"
                                        "}\n"
                                        "\n"
# "/* Title Menu */\n"
# "#titleRightInfo { padding-left: 10px; }\n"
# "\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Extra Tab */\n"
# "#extraLeftBox {	\n"
# "	background-color: rgb(44, 49, 58);\n"
# "}\n"
# "#extraTopBg{	\n"
# "	background-color: rgb(189, 147, 249)\n"
# "}\n"
# "\n"
# "/* Icon */\n"
# "#extraIcon {\n"
# "	background-position: center;\n"
# "	background-repeat: no-repeat;\n"
# "	background-image: url(:/icons/images/icons/icon_settings.png);\n"
# "}\n"
# "\n"
# "/* Label */\n"
# "#extraLabel { color: rgb(255, 255, 255); }\n"
# "\n"
# "/* Btn Close */\n"
# "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
# "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
# "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
# "\n"
# "/* Extra Content */\n"
# "#extraContent{\n"
# "	border"
#                         "-top: 3px solid rgb(40, 44, 52);\n"
# "}\n"
# "\n"
# "/* Extra Top Menus */\n"
# "#extraTopMenu .QPushButton {\n"
# "background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 22px solid transparent;\n"
# "	background-color:transparent;\n"
# "	text-align: left;\n"
# "	padding-left: 44px;\n"
# "}\n"
# "#extraTopMenu .QPushButton:hover {\n"
# "	background-color: rgb(40, 44, 52);\n"
# "}\n"
# "#extraTopMenu .QPushButton:pressed {	\n"
# "	background-color: rgb(189, 147, 249);\n"
# "	color: rgb(255, 255, 255);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Content App */\n"
# "#contentTopBg{	\n"
# "	background-color: rgb(33, 37, 43);\n"
# "}\n"
# "#contentBottom{\n"
# "	border-top: 3px solid rgb(44, 49, 58);\n"
# "}\n"
# "\n"
# "/* Top Buttons */\n"
# "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
# "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
#                         "le: solid; border-radius: 4px; }\n"
# "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
# "\n"
# "/* Theme Settings */\n"
# "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
# "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
# "\n"
# "/* Bottom Bar */\n"
# "#bottomBar { background-color: rgb(44, 49, 58); }\n"
# "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
# "\n"
# "/* CONTENT SETTINGS */\n"
# "/* MENUS */\n"
# "#contentSettings .QPushButton {	\n"
# "	background-position: left center;\n"
# "    background-repeat: no-repeat;\n"
# "	border: none;\n"
# "	border-left: 22px solid transparent;\n"
# "	background-color:transparent;\n"
# "	text-align: left;\n"
# "	padding-left: 44px;\n"
# "}\n"
# "#contentSettings .QPushButton:hover {\n"
# "	background-color: rgb(40, 44, 52);\n"
# "}\n"
# "#contentSettings .QPushButton:pressed {	\n"
# "	background-color: rgb(189, 147, 249);\n"
# "	color: rgb"
#                         "(255, 255, 255);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "QTableWidget */\n"
# "QTableWidget {	\n"
# "	background-color: transparent;\n"
# "	padding: 10px;\n"
# "	border-radius: 5px;\n"
# "	gridline-color: rgb(44, 49, 58);\n"
# "	border-bottom: 1px solid rgb(44, 49, 60);\n"
# "}\n"
# "QTableWidget::item{\n"
# "	border-color: rgb(44, 49, 60);\n"
# "	padding-left: 5px;\n"
# "	padding-right: 5px;\n"
# "	gridline-color: rgb(44, 49, 60);\n"
# "}\n"
# "QTableWidget::item:selected{\n"
# "	background-color: rgb(189, 147, 249);\n"
# "}\n"
# "QHeaderView::section{\n"
# "	background-color: rgb(33, 37, 43);\n"
# "	max-width: 30px;\n"
# "	border: 1px solid rgb(44, 49, 58);\n"
# "	border-style: none;\n"
# "    border-bottom: 1px solid rgb(44, 49, 60);\n"
# "    border-right: 1px solid rgb(44, 49, 60);\n"
# "}\n"
# "QTableWidget::horizontalHeader {	\n"
# "	background-color: rgb(33, 37, 43);\n"
# "}\n"
# "QHeaderView::section:horizontal\n"
# "{\n"
# "    border: 1px solid rgb(33, 37, 43);\n"
# "	background-co"
#                         "lor: rgb(33, 37, 43);\n"
# "	padding: 3px;\n"
# "	border-top-left-radius: 7px;\n"
# "    border-top-right-radius: 7px;\n"
# "}\n"
# "QHeaderView::section:vertical\n"
# "{\n"
# "    border: 1px solid rgb(44, 49, 60);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "LineEdit */\n"
# "QLineEdit {\n"
# "	background-color: rgb(33, 37, 43);\n"
# "	border-radius: 5px;\n"
# "	border: 2px solid rgb(33, 37, 43);\n"
# "	padding-left: 10px;\n"
# "	selection-color: rgb(255, 255, 255);\n"
# "	selection-background-color: rgb(255, 121, 198);\n"
# "}\n"
# "QLineEdit:hover {\n"
# "	border: 2px solid rgb(64, 71, 88);\n"
# "}\n"
# "QLineEdit:focus {\n"
# "	border: 2px solid rgb(91, 101, 124);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "PlainTextEdit */\n"
# "QPlainTextEdit {\n"
# "	background-color: rgb(27, 29, 35);\n"
# "	border-radius: 5px;\n"
# "	padding: 10px;\n"
# "	selection-color: rgb(255, 255, 255);\n"
# "	selection-background-c"
#                         "olor: rgb(255, 121, 198);\n"
# "}\n"
# "QPlainTextEdit  QScrollBar:vertical {\n"
# "    width: 8px;\n"
# " }\n"
# "QPlainTextEdit  QScrollBar:horizontal {\n"
# "    height: 8px;\n"
# " }\n"
# "QPlainTextEdit:hover {\n"
# "	border: 2px solid rgb(64, 71, 88);\n"
# "}\n"
# "QPlainTextEdit:focus {\n"
# "	border: 2px solid rgb(91, 101, 124);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "ScrollBars */\n"
# "QScrollBar:horizontal {\n"
# "    border: none;\n"
# "    background: rgb(52, 59, 72);\n"
# "    height: 8px;\n"
# "    margin: 0px 21px 0 21px;\n"
# "	border-radius: 0px;\n"
# "}\n"
# "QScrollBar::handle:horizontal {\n"
# "    background: rgb(189, 147, 249);\n"
# "    min-width: 25px;\n"
# "	border-radius: 4px\n"
# "}\n"
# "QScrollBar::add-line:horizontal {\n"
# "    border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "    width: 20px;\n"
# "	border-top-right-radius: 4px;\n"
# "    border-bottom-right-radius: 4px;\n"
# "    subcontrol-position: right;\n"
# "    subcontrol-origin: margin;\n"
# "}\n"
# ""
#                         "QScrollBar::sub-line:horizontal {\n"
# "    border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "    width: 20px;\n"
# "	border-top-left-radius: 4px;\n"
# "    border-bottom-left-radius: 4px;\n"
# "    subcontrol-position: left;\n"
# "    subcontrol-origin: margin;\n"
# "}\n"
# "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
# "{\n"
# "     background: none;\n"
# "}\n"
# "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
# "{\n"
# "     background: none;\n"
# "}\n"
# " QScrollBar:vertical {\n"
# "	border: none;\n"
# "    background: rgb(52, 59, 72);\n"
# "    width: 8px;\n"
# "    margin: 21px 0 21px 0;\n"
# "	border-radius: 0px;\n"
# " }\n"
# " QScrollBar::handle:vertical {	\n"
# "	background: rgb(189, 147, 249);\n"
# "    min-height: 25px;\n"
# "	border-radius: 4px\n"
# " }\n"
# " QScrollBar::add-line:vertical {\n"
# "     border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "     height: 20px;\n"
# "	border-bottom-left-radius: 4px;\n"
# "    border-bottom-right-radius: 4px;\n"
# "     subcontrol-position: bottom;\n"
# "     su"
#                         "bcontrol-origin: margin;\n"
# " }\n"
# " QScrollBar::sub-line:vertical {\n"
# "	border: none;\n"
# "    background: rgb(55, 63, 77);\n"
# "     height: 20px;\n"
# "	border-top-left-radius: 4px;\n"
# "    border-top-right-radius: 4px;\n"
# "     subcontrol-position: top;\n"
# "     subcontrol-origin: margin;\n"
# " }\n"
# " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
# "     background: none;\n"
# " }\n"
# "\n"
# " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
# "     background: none;\n"
# " }\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "CheckBox */\n"
# "QCheckBox::indicator {\n"
# "    border: 3px solid rgb(52, 59, 72);\n"
# "	width: 15px;\n"
# "	height: 15px;\n"
# "	border-radius: 10px;\n"
# "    background: rgb(44, 49, 60);\n"
# "}\n"
# "QCheckBox::indicator:hover {\n"
# "    border: 3px solid rgb(58, 66, 81);\n"
# "}\n"
# "QCheckBox::indicator:checked {\n"
# "    background: 3px solid rgb(52, 59, 72);\n"
# "	border: 3px solid rgb(52, 59, 72);	\n"
# "	back"
#                         "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "RadioButton */\n"
# "QRadioButton::indicator {\n"
# "    border: 3px solid rgb(52, 59, 72);\n"
# "	width: 15px;\n"
# "	height: 15px;\n"
# "	border-radius: 10px;\n"
# "    background: rgb(44, 49, 60);\n"
# "}\n"
# "QRadioButton::indicator:hover {\n"
# "    border: 3px solid rgb(58, 66, 81);\n"
# "}\n"
# "QRadioButton::indicator:checked {\n"
# "    background: 3px solid rgb(94, 106, 130);\n"
# "	border: 3px solid rgb(52, 59, 72);	\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "ComboBox */\n"
# "QComboBox{\n"
# "	background-color: rgb(27, 29, 35);\n"
# "	border-radius: 5px;\n"
# "	border: 2px solid rgb(33, 37, 43);\n"
# "	padding: 5px;\n"
# "	padding-left: 10px;\n"
# "}\n"
# "QComboBox:hover{\n"
# "	border: 2px solid rgb(64, 71, 88);\n"
# "}\n"
# "QComboBox::drop-down {\n"
# "	subcontrol-origin: padding;\n"
# "	subco"
#                         "ntrol-position: top right;\n"
# "	width: 25px; \n"
# "	border-left-width: 3px;\n"
# "	border-left-color: rgba(39, 44, 54, 150);\n"
# "	border-left-style: solid;\n"
# "	border-top-right-radius: 3px;\n"
# "	border-bottom-right-radius: 3px;	\n"
# "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
# "	background-position: center;\n"
# "	background-repeat: no-reperat;\n"
# " }\n"
# "QComboBox QAbstractItemView {\n"
# "	color: rgb(255, 121, 198);	\n"
# "	background-color: rgb(33, 37, 43);\n"
# "	padding: 10px;\n"
# "	selection-background-color: rgb(39, 44, 54);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Sliders */\n"
# "QSlider::groove:horizontal {\n"
# "    border-radius: 5px;\n"
# "    height: 10px;\n"
# "	margin: 0px;\n"
# "	background-color: rgb(52, 59, 72);\n"
# "}\n"
# "QSlider::groove:horizontal:hover {\n"
# "	background-color: rgb(55, 62, 76);\n"
# "}\n"
# "QSlider::handle:horizontal {\n"
# "    background-color: rgb(189, 147, 249);\n"
# "    border: none;\n"
# "    h"
#                         "eight: 10px;\n"
# "    width: 10px;\n"
# "    margin: 0px;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "QSlider::handle:horizontal:hover {\n"
# "    background-color: rgb(195, 155, 255);\n"
# "}\n"
# "QSlider::handle:horizontal:pressed {\n"
# "    background-color: rgb(255, 121, 198);\n"
# "}\n"
# "\n"
# "QSlider::groove:vertical {\n"
# "    border-radius: 5px;\n"
# "    width: 10px;\n"
# "    margin: 0px;\n"
# "	background-color: rgb(52, 59, 72);\n"
# "}\n"
# "QSlider::groove:vertical:hover {\n"
# "	background-color: rgb(55, 62, 76);\n"
# "}\n"
# "QSlider::handle:vertical {\n"
# "    background-color: rgb(189, 147, 249);\n"
# "	border: none;\n"
# "    height: 10px;\n"
# "    width: 10px;\n"
# "    margin: 0px;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "QSlider::handle:vertical:hover {\n"
# "    background-color: rgb(195, 155, 255);\n"
# "}\n"
# "QSlider::handle:vertical:pressed {\n"
# "    background-color: rgb(255, 121, 198);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "CommandLinkButton */\n"
# "QCommandLi"
#                         "nkButton {	\n"
# "	color: rgb(255, 121, 198);\n"
# "	border-radius: 5px;\n"
# "	padding: 5px;\n"
# "	color: rgb(255, 170, 255);\n"
# "}\n"
# "QCommandLinkButton:hover {	\n"
# "	color: rgb(255, 170, 255);\n"
# "	background-color: rgb(44, 49, 60);\n"
# "}\n"
# "QCommandLinkButton:pressed {	\n"
# "	color: rgb(189, 147, 249);\n"
# "	background-color: rgb(52, 58, 71);\n"
# "}\n"
# "\n"
# "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
# "Button */\n"
# "#pagesContainer QPushButton {\n"
# "	border: 2px solid rgb(52, 59, 72);\n"
# "	border-radius: 5px;	\n"
# "	background-color: rgb(52, 59, 72);\n"
# "}\n"
# "#pagesContainer QPushButton:hover {\n"
# "	background-color: rgb(57, 65, 80);\n"
# "	border: 2px solid rgb(61, 70, 86);\n"
# "}\n"
# "#pagesContainer QPushButton:pressed {	\n"
# "	background-color: rgb(35, 40, 49);\n"
# "	border: 2px solid rgb(43, 50, 61);\n"
# "}\n"
# "\n"
"")

        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)

        self._preparation()
        self._create_vertical_menu(font)
        sizePolicy = self._add_toggle_menu(font)
        self._add_left_menu(sizePolicy, font)
        self._create_content_box()
        self._add_top_menu(sizePolicy, font)
        self._add_window_buttons()
        self._botton_content_page_container()
        self._home()


        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.verticalLayout_6.addWidget(self.content)

        self.verticalLayout_2.addWidget(self.contentBottom)

        self.appLayout.addWidget(self.contentBox)


        # self.appMargins.addWidget(self.bgApp)

        # MainWindow.setCentralWidget(self.styleSheet)

        # self.retranslateUi(MainWindow)




        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)


    def _preparation(self):

        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)


        self.bgApp = QFrame(self.styleSheet) #
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)


        self.appLayout = QHBoxLayout(self.bgApp) #
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)


        self.leftMenuBg = QFrame(self.bgApp) #
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)


        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)

        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))

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

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg) 
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)

    def _create_vertical_menu(self, font):

        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
  

    def _add_toggle_menu(self, font):

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
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.verticalMenuLayout.addWidget(self.toggleBox)

        return sizePolicy

    
    def _add_left_menu(self, sizePolicy, font):

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)


        self.verticalLayout_8 = QVBoxLayout(self.topMenu) #
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.btn_home = QPushButton(self.topMenu)  # 
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_dvp = QPushButton(self.topMenu)
        self.btn_dvp.setObjectName(u"btn_dvp")
        sizePolicy.setHeightForWidth(self.btn_dvp.sizePolicy().hasHeightForWidth())
        self.btn_dvp.setSizePolicy(sizePolicy)
        self.btn_dvp.setMinimumSize(QSize(0, 45))
        self.btn_dvp.setFont(font)
        self.btn_dvp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dvp.setLayoutDirection(Qt.LeftToRight)
        self.btn_dvp.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_dvp)

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

    def _create_content_box(self):

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)


    def _add_top_menu(self, sizePolicy, font):

        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)


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
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)


    def _add_window_buttons(self):

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
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)


    def _botton_content_page_container(self):

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


    def _home(self):

        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(images/images/logo_expands.png);\n"
                                 "background-position: center;\n"
                                 "background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Data Analysis Tool", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Stellantis", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))

        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_dvp.setText(QCoreApplication.translate("MainWindow", u"DVP", None))
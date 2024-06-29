from PySide6.QtCore       import *
from PySide6.QtGui        import *
from PySide6.QtWidgets    import *
from PySide6.QtCharts     import *
from PySide6.QtPdfWidgets import *
from PySide6.QtPdf        import *

from Modules.UIWidgets.Help_Widgets import *

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









class DYN_Widgets(object):

    def __init__(self):


        pass

    
    def _create_dynamic(self, widgets):

        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(120)
        font1.setBold(True)
        font1.setItalic(False)
        widgets.styleSheet.setFont(font1)

        widgets.dvp = QWidget()
        widgets.dvp.setObjectName(u"dvp")
        widgets.dvp.setStyleSheet(u"b")

        widgets.mainLayout_dvp = QHBoxLayout(widgets.dvp)
        widgets.mainLayout_dvp.setSpacing(10)
        widgets.mainLayout_dvp.setObjectName(u"mainLayout_dvp")
        widgets.mainLayout_dvp.setContentsMargins(10, 10, 10, 10)

        # === ESQUERDA

        widgets.infos_dvp = QFrame(widgets.dvp)
        widgets.infos_dvp.setObjectName(u"row_1")
        widgets.infos_dvp.setFrameShape(QFrame.StyledPanel)
        widgets.infos_dvp.setFrameShadow(QFrame.Raised)
        widgets.infos_dvp.setMinimumWidth(800)

        widgets.verticalLayout_dvp = QVBoxLayout(widgets.infos_dvp)
        widgets.verticalLayout_dvp.setSpacing(10)
        widgets.verticalLayout_dvp.setObjectName(u"verticalLayout_dvp")
        widgets.verticalLayout_dvp.setContentsMargins(10, 10, 10, 10)

        # ROW 1

        widgets.row_1_dvp = QFrame(widgets.infos_dvp)
        widgets.row_1_dvp.setObjectName(u"row_1_dvp")
        widgets.row_1_dvp.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_dvp.setFrameShadow(QFrame.Raised)
        widgets.row_1_dvp.setMaximumHeight(110)

        widgets.LG_row_1_dvp = QGridLayout(widgets.row_1_dvp)
        widgets.LG_row_1_dvp.setSpacing(5)
        widgets.LG_row_1_dvp.setObjectName(u"LG_row_1_dvp")
        widgets.LG_row_1_dvp.setContentsMargins(0, 0, 1, 1)




        # FIRST ROW

        widgets.dynamic_local_search_button = QPushButton(widgets.row_1_dvp)
        widgets.dynamic_local_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_local_search_button.setText("Search")
        widgets.LG_row_1_dvp.addWidget(widgets.dynamic_local_search_button, 0, 0, 1, 2)

        widgets.dynamic_qline_files = QLineEdit(widgets.row_1_dvp)
        widgets.dynamic_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_dvp.addWidget(widgets.dynamic_qline_files, 0, 2, 1, 8)



        widgets.dynamic_search_file_button = QPushButton(widgets.row_1_dvp)
        widgets.dynamic_search_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_search_file_button.setText("Select")
        widgets.LG_row_1_dvp.addWidget(widgets.dynamic_search_file_button, 1, 0, 1, 2)

        widgets.dynamic_qline_files_out = QLineEdit(widgets.row_1_dvp)
        widgets.dynamic_qline_files_out.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_dvp.addWidget(widgets.dynamic_qline_files_out, 1, 2, 1, 8)

        widgets.dynamic_read_file_button = QPushButton(widgets.row_1_dvp)
        widgets.dynamic_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_read_file_button.setText("Process")
        widgets.LG_row_1_dvp.addWidget(widgets.dynamic_read_file_button, 0, 10, 2, 2)

        widgets.verticalLayout_dvp.addWidget(widgets.row_1_dvp)


        # SECOND ROW


        widgets.row_2_dvp = QFrame(widgets.infos_dvp)
        widgets.row_2_dvp.setObjectName(u"row_3_dvp")
        widgets.row_2_dvp.setFrameShape(QFrame.StyledPanel)
        widgets.row_2_dvp.setFrameShadow(QFrame.Raised)
        widgets.row_2_dvp.setMaximumHeight(110)

        widgets.LG_row_2_dvp = QGridLayout(widgets.row_2_dvp)
        widgets.LG_row_2_dvp.setSpacing(5)
        widgets.LG_row_2_dvp.setObjectName(u"LG_row_3_dvp")
        widgets.LG_row_2_dvp.setContentsMargins(0, 0, 1, 1)


        widgets.dynamic_vars_search = QPushButton(widgets.row_2_dvp)
        widgets.dynamic_vars_search.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_vars_search.setText("Processed")
        widgets.LG_row_2_dvp.addWidget(widgets.dynamic_vars_search, 2, 0, 1, 2)

        widgets.dynamic_vars_qline = QLineEdit(widgets.row_2_dvp)
        widgets.dynamic_vars_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_dvp.addWidget(widgets.dynamic_vars_qline, 2, 2, 1, 10)




        widgets.dynamic_instavel = QPushButton(widgets.row_2_dvp)
        widgets.dynamic_instavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_instavel.setText("Instável")
        widgets.LG_row_2_dvp.addWidget(widgets.dynamic_instavel, 3, 0, 1, 6)

        widgets.dynamic_estavel = QPushButton(widgets.row_2_dvp)
        widgets.dynamic_estavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_estavel.setText("Estável")
        widgets.LG_row_2_dvp.addWidget(widgets.dynamic_estavel, 3, 6, 1, 6)


        widgets.dynamic_per_cont = QPushButton(widgets.row_2_dvp)
        widgets.dynamic_per_cont.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_per_cont.setText("Por Contingência")
        widgets.LG_row_2_dvp.addWidget(widgets.dynamic_per_cont, 4, 0, 1, 6)

        widgets.dynamic_per_group = QPushButton(widgets.row_2_dvp)
        widgets.dynamic_per_group.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_per_group.setText("Por Grupo")
        widgets.LG_row_2_dvp.addWidget(widgets.dynamic_per_group, 4, 6, 1, 6)




        widgets.verticalLayout_dvp.addWidget(widgets.row_2_dvp)

        
        # widgets.mainLayout_dvp.addWidget(widgets.pdf_dvp)



        # ROW 3

        widgets.row_3_dvp = QFrame(widgets.infos_dvp)
        widgets.row_3_dvp.setObjectName(u"row_3_dvp")
        widgets.row_3_dvp.setFrameShape(QFrame.StyledPanel)
        widgets.row_3_dvp.setFrameShadow(QFrame.Raised)
        widgets.row_3_dvp.setMinimumHeight(300)

        widgets.LG_row_3_dvp = QGridLayout(widgets.row_3_dvp)
        widgets.LG_row_3_dvp.setSpacing(5)
        widgets.LG_row_3_dvp.setObjectName(u"LG_row_3_dvp")
        widgets.LG_row_3_dvp.setContentsMargins(0, 0, 1, 1)







        widgets.dynamic_x = QComboBox(widgets.row_3_dvp)
        widgets.dynamic_x.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dynamic_x, 0, 0, 1, 3)

        widgets.dynamic_y = QComboBox(widgets.row_3_dvp)
        widgets.dynamic_y.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dynamic_y, 0, 3, 1, 3)


        widgets.dynamic_c = QComboBox(widgets.row_3_dvp)
        widgets.dynamic_c.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dynamic_c, 0, 6, 1, 3)



        widgets.dynamic_plot = QComboBox(widgets.row_3_dvp)
        widgets.dynamic_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dynamic_plot, 1, 0, 1, 3)

        widgets.dynamic_stats = QComboBox(widgets.row_3_dvp)
        widgets.dynamic_stats.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dynamic_stats, 1, 3, 1, 3)


        # widgets.dynamic_c = QComboBox(widgets.row_3_dvp)
        # widgets.dynamic_c.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_3_dvp.addWidget(widgets.dynamic_c, 0, 6, 1, 3)




        widgets.dynamic_plot_button = QPushButton(widgets.row_3_dvp)
        widgets.dynamic_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dynamic_plot_button.setText("Plot")
        widgets.LG_row_3_dvp.addWidget(widgets.dynamic_plot_button, 0, 9, 2, 3)






        widgets.dvp_combo_variable = ExtendedComboBox(widgets.row_3_dvp)
        widgets.dvp_combo_variable.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dvp_combo_variable, 2, 0, 1, 3)

        widgets.dvp_combo_sinal = QComboBox(widgets.row_3_dvp)
        widgets.dvp_combo_sinal.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dvp_combo_sinal, 2, 3, 1, 3)


        widgets.dvp_label_value = QLineEdit(widgets.row_3_dvp)
        widgets.dvp_label_value.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_3_dvp.addWidget(widgets.dvp_label_value, 2, 6, 1, 3)

        widgets.dvp_button_apply_filter = QPushButton(widgets.row_3_dvp)
        widgets.dvp_button_apply_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.dvp_button_apply_filter.setText("Apply Filter")
        widgets.LG_row_3_dvp.addWidget(widgets.dvp_button_apply_filter, 2, 9, 1, 3)



        # ===================================================================================

        widgets.DYNAMIC_sc = MplCanvas(self, width=12, height=12, dpi=100)
        widgets.DYNAMIC_sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        widgets.toolbar = NavigationToolbar2QT(widgets.DYNAMIC_sc)

        widgets.LG_row_3_dvp.addWidget(widgets.toolbar   , 3, 0,  1, 12)
        widgets.LG_row_3_dvp.addWidget(widgets.DYNAMIC_sc, 4, 0, 12, 12)

        # ===================================================================================
        widgets.verticalLayout_dvp.addWidget(widgets.row_3_dvp)


        widgets.mainLayout_dvp.addWidget(widgets.infos_dvp)

        # === DIREITA

        widgets.pdf_dvp = QFrame(widgets.dvp)
        widgets.pdf_dvp.setObjectName(u"row_1")
        # widgets.pdf_dvp.setMinimumSize(QSize(600, 110))
        widgets.pdf_dvp.setFrameShape(QFrame.StyledPanel)
        widgets.pdf_dvp.setFrameShadow(QFrame.Raised)

        widgets.verticalLayout_pdf_dvp = QVBoxLayout(widgets.pdf_dvp)
        widgets.verticalLayout_pdf_dvp.setSpacing(10)
        widgets.verticalLayout_pdf_dvp.setObjectName(u"verticalLayout_pdf_dvp")
        widgets.verticalLayout_pdf_dvp.setContentsMargins(10, 10, 10, 10)

      


        widgets.d_row_1_dvp = QFrame(widgets.pdf_dvp)
        widgets.d_row_1_dvp.setObjectName(u"d_row_1_dvp")
        widgets.d_row_1_dvp.setFrameShape(QFrame.StyledPanel)
        widgets.d_row_1_dvp.setFrameShadow(QFrame.Raised)
        widgets.d_row_1_dvp.setMaximumHeight(600)
        # widgets.d_row_1_dvp.setMaximumSize(QSize(600, 400))

        widgets.d_LG_row_1_dvp = QGridLayout(widgets.d_row_1_dvp)
        widgets.d_LG_row_1_dvp.setSpacing(0)
        widgets.d_LG_row_1_dvp.setObjectName(u"d_LG_row_1_dvp")
        widgets.d_LG_row_1_dvp.setContentsMargins(0, 0, 1, 1)

        ## ============================


        widgets.pdfView_dvp = QPdfView(widgets.pdf_dvp)
        widgets.pdfView_dvp.setObjectName(u"pdfView_dvp")

        widgets.m_document = QPdfDocument(widgets.pdf_dvp)

        widgets.pdfView_dvp.setDocument(widgets.m_document)


        ## ============================



        widgets.mainToolBar = QToolBar(widgets.d_row_1_dvp)
        widgets.mainToolBar.setObjectName(u"mainToolBar")
        widgets.mainToolBar.setMovable(False)
        widgets.mainToolBar.setFloatable(False)


        # ACTIONS


        widgets.run_dvp = QPushButton(widgets.d_row_1_dvp)
        widgets.run_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.run_dvp.setText("Run")

        widgets.actionZoom_In_dvp = QPushButton(widgets.d_row_1_dvp)
        widgets.actionZoom_In_dvp.setText('In')
        widgets.actionZoom_In_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionZoom_Out = QPushButton(widgets.d_row_1_dvp)
        widgets.actionZoom_Out.setText('Out')
        widgets.actionZoom_Out.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_zoomSelector = ZoomSelector(widgets.d_row_1_dvp)
        widgets.m_zoomSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.m_zoomSelector.setMaximumWidth(150)
        widgets.m_zoomSelector.zoom_mode_changed.connect(widgets.pdfView_dvp.setZoomMode)
        widgets.m_zoomSelector.zoom_factor_changed.connect(widgets.pdfView_dvp.setZoomFactor)
        widgets.m_zoomSelector.reset()
        widgets.pdfView_dvp.zoomFactorChanged.connect(widgets.m_zoomSelector.set_zoom_factor)

        widgets.actionPage_down_dvp = QPushButton(widgets.d_row_1_dvp)
        widgets.actionPage_down_dvp.setText('-')
        widgets.actionPage_down_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionPage_up_dvp = QPushButton(widgets.d_row_1_dvp)
        widgets.actionPage_up_dvp.setText('+')
        widgets.actionPage_up_dvp.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_pageSelector = QSpinBox(widgets.d_row_1_dvp)
        widgets.m_pageSelector.valueChanged.connect(widgets.page_selected)
        widgets.m_pageSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        nav = widgets.pdfView_dvp.pageNavigator()
        nav.currentPageChanged.connect(widgets.m_pageSelector.setValue)
        # nav.backAvailableChanged.connect(widgets.actionBack.setEnabled)
        # nav.forwardAvailableChanged.connect(widgets.actionForward.setEnabled)

        widgets.actionSave = QPushButton(widgets.d_row_1_dvp)
        widgets.actionSave.setText('Save')
        widgets.actionSave.setStyleSheet(u"background-color: rgb(91, 95, 199)")





        widgets.mainToolBar.addWidget(widgets.run_dvp)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_In_dvp)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_zoomSelector)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_Out)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_down_dvp)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_pageSelector)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_up_dvp)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionSave)




        ## =============


        widgets.d_LG_row_1_dvp.addWidget(widgets.mainToolBar, 0, 0, 1, 1)
        widgets.d_LG_row_1_dvp.addWidget(widgets.pdfView_dvp, 1, 0, 1, 1)

        widgets.verticalLayout_pdf_dvp.addWidget(widgets.d_row_1_dvp)
        widgets.mainLayout_dvp.addWidget(widgets.pdf_dvp)
       

        # ADD ALL

        widgets.stackedWidget.addWidget(widgets.dvp)






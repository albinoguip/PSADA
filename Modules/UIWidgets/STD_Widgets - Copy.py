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









class STD_Widgets(object):

    def __init__(self):


        pass

    
    def _create_static_dynamic(self, widgets):

        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(120)
        font1.setBold(True)
        font1.setItalic(False)
        widgets.styleSheet.setFont(font1)

        widgets.STADYN = QWidget()
        widgets.STADYN.setObjectName(u"STADYN")
        widgets.STADYN.setStyleSheet(u"b")

        widgets.mainLayout_STADYN = QHBoxLayout(widgets.STADYN)
        widgets.mainLayout_STADYN.setSpacing(10)
        widgets.mainLayout_STADYN.setObjectName(u"mainLayout_STADYN")
        widgets.mainLayout_STADYN.setContentsMargins(10, 10, 10, 10)

        # === ESQUERDA

        widgets.infos_STADYN = QFrame(widgets.STADYN)
        widgets.infos_STADYN.setObjectName(u"row_1")
        widgets.infos_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.infos_STADYN.setFrameShadow(QFrame.Raised)
        widgets.infos_STADYN.setMinimumWidth(800)

        widgets.verticalLayout_STADYN = QVBoxLayout(widgets.infos_STADYN)
        widgets.verticalLayout_STADYN.setSpacing(10)
        widgets.verticalLayout_STADYN.setObjectName(u"verticalLayout_STADYN")
        widgets.verticalLayout_STADYN.setContentsMargins(10, 10, 10, 10)

        # ROW 1

        widgets.row_1_STADYN = QFrame(widgets.infos_STADYN)
        widgets.row_1_STADYN.setObjectName(u"row_1_STADYN")
        widgets.row_1_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_STADYN.setFrameShadow(QFrame.Raised)
        widgets.row_1_STADYN.setMaximumHeight(110)
        widgets.row_1_STADYN.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        

        widgets.LG_row_1_STADYN = QGridLayout(widgets.row_1_STADYN)
        widgets.LG_row_1_STADYN.setSpacing(5)
        widgets.LG_row_1_STADYN.setObjectName(u"LG_row_1_STADYN")
        widgets.LG_row_1_STADYN.setContentsMargins(0, 0, 1, 1)



        # FIRST ROW

        widgets.STADYN_search_button = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_search_button.setText("Search")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_search_button, 0, 0, 1, 2)

        widgets.STADYN_qline_files = QLineEdit(widgets.row_1_STADYN)
        widgets.STADYN_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_qline_files, 0, 2, 1, 8)

        widgets.STADYN_read_file_button = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_read_file_button.setText("Process")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_read_file_button, 0, 10, 1, 2)

        # SECOND ROW



        widgets.STADYN_vars_search = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_vars_search.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_vars_search.setText("Processed")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_vars_search, 1, 0, 1, 2)

        widgets.STADYN_vars_qline = QLineEdit(widgets.row_1_STADYN)
        widgets.STADYN_vars_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_vars_qline, 1, 2, 1, 8)

        widgets.STADYN_read_vars_button = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_read_vars_button.setText("Open")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_read_vars_button, 1, 10, 1, 2)


        # SPECIAL BUTTONS

        widgets.STADYN_instavel = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_instavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_instavel.setText("Instável")
        widgets.STADYN_instavel.setMinimumWidth(20)
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_instavel, 0, 13, 1, 1)        

        widgets.STADYN_estavel = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_estavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_estavel.setText("Estável")
        widgets.STADYN_estavel.setMinimumWidth(130)
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_estavel, 0, 14, 1, 1)

        widgets.STADYN_per_cont = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_per_cont.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_per_cont.setText("Por Contingência")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_per_cont, 1, 13, 1, 1)

        widgets.STADYN_per_group = QPushButton(widgets.row_1_STADYN)
        widgets.STADYN_per_group.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_per_group.setText("Por Grupo")
        widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_per_group, 1, 14, 1, 1)


        widgets.verticalLayout_STADYN.addWidget(widgets.row_1_STADYN)


        # ------------------------------------------------------------------------------------------


        widgets.row_2_STADYN = QFrame(widgets.infos_STADYN)
        widgets.row_2_STADYN.setObjectName(u"row_2_STADYN")
        widgets.row_2_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.row_2_STADYN.setFrameShadow(QFrame.Raised)
        widgets.row_2_STADYN.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_2_STADYN.setMaximumHeight(130)

        widgets.LG_row_2_STADYN = QGridLayout(widgets.row_2_STADYN)
        widgets.LG_row_2_STADYN.setSpacing(5)
        widgets.LG_row_2_STADYN.setObjectName(u"LG_row_2_STADYN")
        widgets.LG_row_2_STADYN.setContentsMargins(0, 0, 1, 1)


        # THIRD ROW


        widgets.STADYN_x = QComboBox(widgets.row_2_STADYN)
        widgets.STADYN_x.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_x, 0, 0, 1, 3)

        widgets.STADYN_y = QComboBox(widgets.row_2_STADYN)
        widgets.STADYN_y.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_y, 0, 3, 1, 3)

        widgets.STADYN_c = QComboBox(widgets.row_2_STADYN)
        widgets.STADYN_c.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_c, 0, 6, 1, 3)

        # FOURTH ROW

        widgets.STADYN_plot = QComboBox(widgets.row_2_STADYN)
        widgets.STADYN_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_plot, 1, 0, 1, 3)

        widgets.STADYN_round = QComboBox(widgets.row_2_STADYN)
        widgets.STADYN_round.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_round, 1, 3, 1, 3)


        widgets.STADYN_stats = QComboBox(widgets.row_2_STADYN)
        widgets.STADYN_stats.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_stats, 1, 6, 1, 3)

        # PLOT BUTTON

        widgets.STADYN_plot_button = QPushButton(widgets.row_2_STADYN)
        widgets.STADYN_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_plot_button.setText("Plot")
        widgets.STADYN_plot_button.setMinimumHeight(70)
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_plot_button, 0, 9, 2, 4)

        # FIFTH ROW

        widgets.STADYN_combo_variable = ExtendedComboBox(widgets.row_2_STADYN)
        widgets.STADYN_combo_variable.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_combo_variable, 2, 0, 1, 3)

        widgets.STADYN_combo_sinal = QComboBox(widgets.row_2_STADYN)
        widgets.STADYN_combo_sinal.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_combo_sinal, 2, 3, 1, 3)

        widgets.STADYN_label_value = QLineEdit(widgets.row_2_STADYN)
        widgets.STADYN_label_value.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_label_value, 2, 6, 1, 3)

        widgets.STADYN_button_apply_filter = QPushButton(widgets.row_2_STADYN)
        widgets.STADYN_button_apply_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_button_apply_filter.setText("Apply Filter")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_button_apply_filter, 2, 9, 1, 2)

        widgets.STADYN_button_remove_filter = QPushButton(widgets.row_2_STADYN)
        widgets.STADYN_button_remove_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_button_remove_filter.setText("Remove Filter")
        widgets.LG_row_2_STADYN.addWidget(widgets.STADYN_button_remove_filter, 2, 11, 1, 2)


        widgets.verticalLayout_STADYN.addWidget(widgets.row_2_STADYN)


        # ------------------------------------------------------------------------------------------


        widgets.row_3_STADYN = QFrame(widgets.infos_STADYN)
        widgets.row_3_STADYN.setObjectName(u"row_3_STADYN")
        widgets.row_3_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.row_3_STADYN.setFrameShadow(QFrame.Raised)
        # widgets.row_3_STADYN.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_3_STADYN.setMinimumHeight(500)

        widgets.LG_row_3_STADYN = QGridLayout(widgets.row_3_STADYN)
        widgets.LG_row_3_STADYN.setSpacing(5)
        widgets.LG_row_3_STADYN.setObjectName(u"LG_row_3_STADYN")
        widgets.LG_row_3_STADYN.setContentsMargins(0, 0, 1, 1)



        widgets.STADYN_sc = MplCanvas(self, width=12, height=12, dpi=100)        
        widgets.STADYN_sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        widgets.toolbar = NavigationToolbar2QT(widgets.STADYN_sc)

        widgets.LG_row_3_STADYN.addWidget(widgets.toolbar   , 0, 0,  1, 10)
        widgets.LG_row_3_STADYN.addWidget(widgets.STADYN_sc, 1, 0, 10, 10)



        widgets.verticalLayout_STADYN.addWidget(widgets.row_3_STADYN)


        # ------------------------------------------------------------------------------------------


        widgets.row_4_STADYN = QFrame(widgets.infos_STADYN)
        widgets.row_4_STADYN.setObjectName(u"row_4_STADYN")
        widgets.row_4_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_STADYN.setFrameShadow(QFrame.Raised)
        widgets.row_4_STADYN.setMaximumHeight(130)

        widgets.LG_row_4_STADYN = QGridLayout(widgets.row_4_STADYN)
        widgets.LG_row_4_STADYN.setSpacing(5)
        widgets.LG_row_4_STADYN.setObjectName(u"LG_row_4_STADYN")
        widgets.LG_row_4_STADYN.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_1_STADYN = QFrame(widgets.row_4_STADYN)
        widgets.row_4_1_STADYN.setObjectName(u"row_4_1_STADYN")
        widgets.row_4_1_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_1_STADYN.setFrameShadow(QFrame.Raised)
        widgets.row_4_1_STADYN.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_1_STADYN = QGridLayout(widgets.row_4_1_STADYN)
        widgets.LG_row_4_1_STADYN.setSpacing(5)
        widgets.LG_row_4_1_STADYN.setObjectName(u"LG_row_4_1_STADYN")
        widgets.LG_row_4_1_STADYN.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_2_STADYN = QFrame(widgets.row_4_STADYN)
        widgets.row_4_2_STADYN.setObjectName(u"row_4_2_STADYN")
        widgets.row_4_2_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_2_STADYN.setFrameShadow(QFrame.Raised)
        widgets.row_4_2_STADYN.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_2_STADYN = QGridLayout(widgets.row_4_2_STADYN)
        widgets.LG_row_4_2_STADYN.setSpacing(5)
        widgets.LG_row_4_2_STADYN.setObjectName(u"LG_row_4_2_STADYN")
        widgets.LG_row_4_2_STADYN.setContentsMargins(0, 0, 1, 1)



        widgets.LG_row_4_STADYN.addWidget(widgets.row_4_1_STADYN, 0, 0, 1, 1)
        widgets.LG_row_4_STADYN.addWidget(widgets.row_4_2_STADYN, 0, 1, 1, 1)


        # SIXTH ROW


        widgets.STADYN_add_section = QLineEdit(widgets.row_4_1_STADYN)
        widgets.STADYN_add_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_1_STADYN.addWidget(widgets.STADYN_add_section, 0, 0, 1, 3)

        widgets.STADYN_add_section_button = QPushButton(widgets.row_4_1_STADYN)
        widgets.STADYN_add_section_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_add_section_button.setText("Add Section")
        widgets.LG_row_4_1_STADYN.addWidget(widgets.STADYN_add_section_button, 0, 3, 1, 3)

        widgets.STADYN_add_plot = QLineEdit(widgets.row_4_1_STADYN)
        widgets.STADYN_add_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_1_STADYN.addWidget(widgets.STADYN_add_plot, 1, 0, 1, 3)

        widgets.STADYN_add_plot_button = QPushButton(widgets.row_4_1_STADYN)
        widgets.STADYN_add_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_add_plot_button.setText("Add Page")
        widgets.LG_row_4_1_STADYN.addWidget(widgets.STADYN_add_plot_button, 1, 3, 1, 3)


        # SEVENTH ROW


        widgets.STADYN_select_section = QComboBox(widgets.row_4_2_STADYN)
        widgets.STADYN_select_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_2_STADYN.addWidget(widgets.STADYN_select_section, 0, 0, 1, 4)

        widgets.STADYN_select_plot = QComboBox(widgets.row_4_2_STADYN)
        widgets.STADYN_select_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_2_STADYN.addWidget(widgets.STADYN_select_plot, 0, 4, 1, 4)

        widgets.STADYN_add_to_json_button = QPushButton(widgets.row_4_2_STADYN)
        widgets.STADYN_add_to_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_add_to_json_button.setText("Add Plot to Page")
        widgets.LG_row_4_2_STADYN.addWidget(widgets.STADYN_add_to_json_button, 1, 0, 1, 8)

        widgets.verticalLayout_STADYN.addWidget(widgets.row_4_STADYN)


        widgets.mainLayout_STADYN.addWidget(widgets.infos_STADYN)




        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ///                                                                                                                                                ///
        # ///                                                                     DIREITA                                                                    ///
        # ///                                                                                                                                                ///
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



        widgets.pdf_STADYN = QFrame(widgets.STADYN)
        widgets.pdf_STADYN.setObjectName(u"row_1")
        widgets.pdf_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.pdf_STADYN.setFrameShadow(QFrame.Raised)

        widgets.verticalLayout_pdf_STADYN = QVBoxLayout(widgets.pdf_STADYN)
        widgets.verticalLayout_pdf_STADYN.setSpacing(10)
        widgets.verticalLayout_pdf_STADYN.setObjectName(u"verticalLayout_pdf_STADYN")
        widgets.verticalLayout_pdf_STADYN.setContentsMargins(10, 10, 10, 10)





        widgets.row_5_STADYN = QFrame(widgets.pdf_STADYN)
        widgets.row_5_STADYN.setObjectName(u"row_5_STADYN")
        widgets.row_5_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.row_5_STADYN.setFrameShadow(QFrame.Raised)
        # widgets.row_5_STADYN.setMaximumHeight(110)
        widgets.row_5_STADYN.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        

        widgets.LG_row_5_STADYN = QGridLayout(widgets.row_5_STADYN)
        widgets.LG_row_5_STADYN.setSpacing(5)
        widgets.LG_row_5_STADYN.setObjectName(u"LG_row_5_STADYN")
        widgets.LG_row_5_STADYN.setContentsMargins(0, 0, 1, 1)



        # FIRST ROW

        widgets.STADYN_search_button = QPushButton(widgets.row_5_STADYN)
        widgets.STADYN_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_search_button.setText("Search")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_search_button, 0, 0, 1, 2)

        widgets.STADYN_qline_files = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_files, 0, 2, 1, 8)

        widgets.STADYN_read_file_button = QPushButton(widgets.row_5_STADYN)
        widgets.STADYN_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STADYN_read_file_button.setText("Process")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_read_file_button, 0, 10, 1, 2)

        # SECOND ROW

        widgets.STADYN_label_00 = QLabel(widgets.row_5_STADYN)
        widgets.STADYN_label_00.setText("Processed")
        widgets.STADYN_label_00.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_label_00, 1, 0, 1, 6)

        widgets.STADYN_qline_00 = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_00.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_00, 2, 0, 1, 6)


        widgets.STADYN_label_01 = QLabel(widgets.row_5_STADYN)
        widgets.STADYN_label_01.setText("Processed")
        widgets.STADYN_label_01.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_label_01, 1, 6, 1, 6)

        widgets.STADYN_qline_01 = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_01.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_01, 2, 6, 1, 6)


        # THIRD ROW

        widgets.STADYN_label_10 = QLabel(widgets.row_5_STADYN)
        widgets.STADYN_label_10.setText("Processed")
        widgets.STADYN_label_10.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_label_10, 3, 0, 1, 6)

        widgets.STADYN_qline_10 = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_10.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_10, 4, 0, 1, 6)


        widgets.STADYN_label_11 = QLabel(widgets.row_5_STADYN)
        widgets.STADYN_label_11.setText("Processed")
        widgets.STADYN_label_11.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_label_11, 3, 6, 1, 6)

        widgets.STADYN_qline_11 = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_11.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_11, 4, 6, 1, 6)

        # THIRD ROW

        widgets.STADYN_label_20 = QLabel(widgets.row_5_STADYN)
        widgets.STADYN_label_20.setText("Processed")
        widgets.STADYN_label_20.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_label_20, 5, 0, 1, 6)

        widgets.STADYN_qline_20 = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_20.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_20, 6, 0, 1, 6)


        widgets.STADYN_label_21 = QLabel(widgets.row_5_STADYN)
        widgets.STADYN_label_21.setText("Processed")
        widgets.STADYN_label_21.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_label_21, 5, 6, 1, 6)

        widgets.STADYN_qline_21 = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_21.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_21, 6, 6, 1, 6)


        # THIRD ROW

        widgets.STADYN_label_30 = QLabel(widgets.row_5_STADYN)
        widgets.STADYN_label_30.setText("Processed")
        widgets.STADYN_label_30.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_label_30, 7, 0, 1, 12)

        widgets.STADYN_qline_30 = QLineEdit(widgets.row_5_STADYN)
        widgets.STADYN_qline_30.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_STADYN.addWidget(widgets.STADYN_qline_30, 8, 0, 1, 12)





        # widgets.STADYN_read_vars_button = QPushButton(widgets.row_1_STADYN)
        # widgets.STADYN_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STADYN_read_vars_button.setText("Open")
        # widgets.LG_row_1_STADYN.addWidget(widgets.STADYN_read_vars_button, 1, 10, 1, 2)



        widgets.verticalLayout_pdf_STADYN.addWidget(widgets.row_5_STADYN)





        

      


        widgets.d_row_1_STADYN = QFrame(widgets.pdf_STADYN)
        widgets.d_row_1_STADYN.setObjectName(u"d_row_1_STADYN")
        widgets.d_row_1_STADYN.setFrameShape(QFrame.StyledPanel)
        widgets.d_row_1_STADYN.setFrameShadow(QFrame.Raised)
        widgets.d_row_1_STADYN.setMaximumHeight(600)
        # widgets.d_row_1_STADYN.setMaximumSize(QSize(600, 400))

        widgets.d_LG_row_1_STADYN = QGridLayout(widgets.d_row_1_STADYN)
        widgets.d_LG_row_1_STADYN.setSpacing(0)
        widgets.d_LG_row_1_STADYN.setObjectName(u"d_LG_row_1_STADYN")
        widgets.d_LG_row_1_STADYN.setContentsMargins(0, 0, 1, 1)

        ## ============================


        widgets.pdfView_STADYN = QPdfView(widgets.pdf_STADYN)
        widgets.pdfView_STADYN.setObjectName(u"pdfView_STADYN")

        widgets.m_document = QPdfDocument(widgets.pdf_STADYN)

        widgets.pdfView_STADYN.setDocument(widgets.m_document)


        ## ============================



        widgets.mainToolBar = QToolBar(widgets.d_row_1_STADYN)
        widgets.mainToolBar.setObjectName(u"mainToolBar")
        widgets.mainToolBar.setMovable(False)
        widgets.mainToolBar.setFloatable(False)


        # ACTIONS


        widgets.run_STADYN = QPushButton(widgets.d_row_1_STADYN)
        widgets.run_STADYN.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.run_STADYN.setText("Run")

        widgets.actionZoom_In_STADYN = QPushButton(widgets.d_row_1_STADYN)
        widgets.actionZoom_In_STADYN.setText('In')
        widgets.actionZoom_In_STADYN.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionZoom_Out = QPushButton(widgets.d_row_1_STADYN)
        widgets.actionZoom_Out.setText('Out')
        widgets.actionZoom_Out.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_zoomSelector = ZoomSelector(widgets.d_row_1_STADYN)
        widgets.m_zoomSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.m_zoomSelector.setMaximumWidth(150)
        widgets.m_zoomSelector.zoom_mode_changed.connect(widgets.pdfView_STADYN.setZoomMode)
        widgets.m_zoomSelector.zoom_factor_changed.connect(widgets.pdfView_STADYN.setZoomFactor)
        widgets.m_zoomSelector.reset()
        widgets.pdfView_STADYN.zoomFactorChanged.connect(widgets.m_zoomSelector.set_zoom_factor)

        widgets.actionPage_down_STADYN = QPushButton(widgets.d_row_1_STADYN)
        widgets.actionPage_down_STADYN.setText('-')
        widgets.actionPage_down_STADYN.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionPage_up_STADYN = QPushButton(widgets.d_row_1_STADYN)
        widgets.actionPage_up_STADYN.setText('+')
        widgets.actionPage_up_STADYN.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_pageSelector = QSpinBox(widgets.d_row_1_STADYN)
        widgets.m_pageSelector.valueChanged.connect(widgets.page_selected)
        widgets.m_pageSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        nav = widgets.pdfView_STADYN.pageNavigator()
        nav.currentPageChanged.connect(widgets.m_pageSelector.setValue)
        # nav.backAvailableChanged.connect(widgets.actionBack.setEnabled)
        # nav.forwardAvailableChanged.connect(widgets.actionForward.setEnabled)

        widgets.actionSave = QPushButton(widgets.d_row_1_STADYN)
        widgets.actionSave.setText('Save')
        widgets.actionSave.setStyleSheet(u"background-color: rgb(91, 95, 199)")





        widgets.mainToolBar.addWidget(widgets.run_STADYN)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_In_STADYN)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_zoomSelector)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_Out)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_down_STADYN)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_pageSelector)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_up_STADYN)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionSave)




        ## =============


        widgets.d_LG_row_1_STADYN.addWidget(widgets.mainToolBar, 0, 0, 1, 1)
        widgets.d_LG_row_1_STADYN.addWidget(widgets.pdfView_STADYN, 1, 0, 1, 1)

        widgets.verticalLayout_pdf_STADYN.addWidget(widgets.d_row_1_STADYN)
        widgets.mainLayout_STADYN.addWidget(widgets.pdf_STADYN)
       

        # ADD ALL

        widgets.stackedWidget.addWidget(widgets.STADYN)






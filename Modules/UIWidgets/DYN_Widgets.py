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

        widgets.DYNAMIC = QWidget()
        widgets.DYNAMIC.setObjectName(u"DYNAMIC")
        widgets.DYNAMIC.setStyleSheet(u"b")

        widgets.mainLayout_DYNAMIC = QHBoxLayout(widgets.DYNAMIC)
        widgets.mainLayout_DYNAMIC.setSpacing(10)
        widgets.mainLayout_DYNAMIC.setObjectName(u"mainLayout_DYNAMIC")
        widgets.mainLayout_DYNAMIC.setContentsMargins(10, 10, 10, 10)

        # === ESQUERDA

        widgets.infos_DYNAMIC = QFrame(widgets.DYNAMIC)
        widgets.infos_DYNAMIC.setObjectName(u"row_1")
        widgets.infos_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.infos_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.infos_DYNAMIC.setMinimumWidth(800)

        widgets.verticalLayout_DYNAMIC = QVBoxLayout(widgets.infos_DYNAMIC)
        widgets.verticalLayout_DYNAMIC.setSpacing(10)
        widgets.verticalLayout_DYNAMIC.setObjectName(u"verticalLayout_DYNAMIC")
        widgets.verticalLayout_DYNAMIC.setContentsMargins(10, 10, 10, 10)

        # ROW 1

        widgets.row_1_DYNAMIC = QFrame(widgets.infos_DYNAMIC)
        widgets.row_1_DYNAMIC.setObjectName(u"row_1_DYNAMIC")
        widgets.row_1_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.row_1_DYNAMIC.setMaximumHeight(110)
        

        widgets.LG_row_1_DYNAMIC = QGridLayout(widgets.row_1_DYNAMIC)
        widgets.LG_row_1_DYNAMIC.setSpacing(5)
        widgets.LG_row_1_DYNAMIC.setObjectName(u"LG_row_1_DYNAMIC")
        widgets.LG_row_1_DYNAMIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_1_1_DYNAMIC = QFrame(widgets.row_1_DYNAMIC)
        widgets.row_1_1_DYNAMIC.setObjectName(u"row_1_1_DYNAMIC")
        widgets.row_1_1_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_1_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.row_1_1_DYNAMIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_1_1_DYNAMIC = QGridLayout(widgets.row_1_1_DYNAMIC)
        widgets.LG_row_1_1_DYNAMIC.setSpacing(5)
        widgets.LG_row_1_1_DYNAMIC.setObjectName(u"LG_row_1_1_DYNAMIC")
        widgets.LG_row_1_1_DYNAMIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_1_2_DYNAMIC = QFrame(widgets.row_1_DYNAMIC)
        widgets.row_1_2_DYNAMIC.setObjectName(u"row_1_2_DYNAMIC")
        widgets.row_1_2_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_2_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.row_1_2_DYNAMIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_1_2_DYNAMIC = QGridLayout(widgets.row_1_2_DYNAMIC)
        widgets.LG_row_1_2_DYNAMIC.setSpacing(5)
        widgets.LG_row_1_2_DYNAMIC.setObjectName(u"LG_row_1_2_DYNAMIC")
        widgets.LG_row_1_2_DYNAMIC.setContentsMargins(0, 0, 1, 1)



        widgets.LG_row_1_DYNAMIC.addWidget(widgets.row_1_1_DYNAMIC, 0, 0, 1, 3)
        widgets.LG_row_1_DYNAMIC.addWidget(widgets.row_1_2_DYNAMIC, 0, 3, 1, 1)



        # FIRST ROW

        widgets.DYNAMIC_search_button = QPushButton(widgets.row_1_1_DYNAMIC)
        widgets.DYNAMIC_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_search_button.setText("Search")
        widgets.LG_row_1_1_DYNAMIC.addWidget(widgets.DYNAMIC_search_button, 0, 0, 1, 2)

        widgets.DYNAMIC_qline_files = QLineEdit(widgets.row_1_1_DYNAMIC)
        widgets.DYNAMIC_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_1_DYNAMIC.addWidget(widgets.DYNAMIC_qline_files, 0, 2, 1, 8)

        widgets.DYNAMIC_read_file_button = QPushButton(widgets.row_1_1_DYNAMIC)
        widgets.DYNAMIC_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_read_file_button.setText("Process")
        widgets.LG_row_1_1_DYNAMIC.addWidget(widgets.DYNAMIC_read_file_button, 0, 10, 1, 2)

        # SECOND ROW

        widgets.DYNAMIC_vars_search = QPushButton(widgets.row_1_1_DYNAMIC)
        widgets.DYNAMIC_vars_search.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_vars_search.setText("Processed")
        widgets.LG_row_1_1_DYNAMIC.addWidget(widgets.DYNAMIC_vars_search, 1, 0, 1, 2)

        widgets.DYNAMIC_vars_qline = QLineEdit(widgets.row_1_1_DYNAMIC)
        widgets.DYNAMIC_vars_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_1_DYNAMIC.addWidget(widgets.DYNAMIC_vars_qline, 1, 2, 1, 8)

        widgets.DYNAMIC_read_vars_button = QPushButton(widgets.row_1_1_DYNAMIC)
        widgets.DYNAMIC_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_read_vars_button.setText("Open")
        widgets.LG_row_1_1_DYNAMIC.addWidget(widgets.DYNAMIC_read_vars_button, 1, 10, 1, 2)


        # SPECIAL BUTTONS

        widgets.DYNAMIC_instavel = QPushButton(widgets.row_1_2_DYNAMIC)
        widgets.DYNAMIC_instavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_instavel.setText("Unstable")
        widgets.DYNAMIC_instavel.setMinimumWidth(20)
        widgets.LG_row_1_2_DYNAMIC.addWidget(widgets.DYNAMIC_instavel, 0, 13, 1, 1)        

        widgets.DYNAMIC_estavel = QPushButton(widgets.row_1_2_DYNAMIC)
        widgets.DYNAMIC_estavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_estavel.setText("Stable")
        widgets.DYNAMIC_estavel.setMinimumWidth(130)
        widgets.LG_row_1_2_DYNAMIC.addWidget(widgets.DYNAMIC_estavel, 0, 14, 1, 1)

        widgets.DYNAMIC_per_cont = QPushButton(widgets.row_1_2_DYNAMIC)
        widgets.DYNAMIC_per_cont.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_per_cont.setText("By Contingency")
        widgets.LG_row_1_2_DYNAMIC.addWidget(widgets.DYNAMIC_per_cont, 1, 13, 1, 1)

        widgets.DYNAMIC_per_group = QPushButton(widgets.row_1_2_DYNAMIC)
        widgets.DYNAMIC_per_group.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_per_group.setText("By Group")
        widgets.LG_row_1_2_DYNAMIC.addWidget(widgets.DYNAMIC_per_group, 1, 14, 1, 1)


        widgets.verticalLayout_DYNAMIC.addWidget(widgets.row_1_DYNAMIC)


        # ------------------------------------------------------------------------------------------


        widgets.row_2_DYNAMIC = QFrame(widgets.infos_DYNAMIC)
        widgets.row_2_DYNAMIC.setObjectName(u"row_2_DYNAMIC")
        widgets.row_2_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_2_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.row_2_DYNAMIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_2_DYNAMIC.setMaximumHeight(130)

        widgets.LG_row_2_DYNAMIC = QGridLayout(widgets.row_2_DYNAMIC)
        widgets.LG_row_2_DYNAMIC.setSpacing(5)
        widgets.LG_row_2_DYNAMIC.setObjectName(u"LG_row_2_DYNAMIC")
        widgets.LG_row_2_DYNAMIC.setContentsMargins(0, 0, 1, 1)


        # THIRD ROW

        widgets.DYNAMIC_plot_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_plot_label.setText("Plot")
        widgets.DYNAMIC_plot_label.setMaximumWidth(40)
        widgets.DYNAMIC_plot_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_plot_label, 0, 0, 1, 1)
        widgets.DYNAMIC_plot = QComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_plot, 0, 1, 1, 2)


        widgets.DYNAMIC_x_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_x_label.setText("X")
        widgets.DYNAMIC_x_label.setMaximumWidth(40)
        widgets.DYNAMIC_x_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_x_label, 0, 3, 1, 1)
        widgets.DYNAMIC_x = QComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_x.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_x, 0, 4, 1, 2)


        widgets.DYNAMIC_y_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_y_label.setText("Y")
        widgets.DYNAMIC_y_label.setMaximumWidth(40)
        widgets.DYNAMIC_y_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_y_label, 0, 6, 1, 1)
        widgets.DYNAMIC_y = QComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_y.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_y, 0, 7, 1, 2)

        

        # FOURTH ROW

        widgets.DYNAMIC_c_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_c_label.setText("Color")
        widgets.DYNAMIC_c_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_c_label, 1, 0, 1, 1)
        widgets.DYNAMIC_c = QComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_c.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_c, 1, 1, 1, 2)        


        widgets.DYNAMIC_round_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_round_label.setText("Round")
        widgets.DYNAMIC_round_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_round_label, 1, 3, 1, 1)
        widgets.DYNAMIC_round = QComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_round.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_round, 1, 4, 1, 2)


        widgets.DYNAMIC_stats_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_stats_label.setText("Functions")
        widgets.DYNAMIC_stats_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_stats_label, 1, 6, 1, 1)
        widgets.DYNAMIC_stats = QComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_stats.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_stats, 1, 7, 1, 2)

        # PLOT BUTTON

        widgets.DYNAMIC_plot_button = QPushButton(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_plot_button.setText("Plot")
        widgets.DYNAMIC_plot_button.setMinimumHeight(70)
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_plot_button, 0, 9, 2, 4)

        # FIFTH ROW

        widgets.DYNAMIC_variable_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_variable_label.setText("Col")
        widgets.DYNAMIC_variable_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_variable_label, 2, 0, 1, 1)
        widgets.DYNAMIC_combo_variable = ExtendedComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_combo_variable.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_combo_variable, 2, 1, 1, 2)


        widgets.DYNAMIC_signal_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_signal_label.setText("Oper")
        widgets.DYNAMIC_signal_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_signal_label, 2, 3, 1, 1)
        widgets.DYNAMIC_combo_sinal = QComboBox(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_combo_sinal.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_combo_sinal, 2, 4, 1, 2)


        widgets.DYNAMIC_value_label = QLabel(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_value_label.setText("Value")
        widgets.DYNAMIC_value_label.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_value_label, 2, 6, 1, 1)
        widgets.DYNAMIC_label_value = QLineEdit(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_label_value.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_label_value, 2, 7, 1, 2)




        widgets.DYNAMIC_button_apply_filter = QPushButton(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_button_apply_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_button_apply_filter.setText("Apply Filter")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_button_apply_filter, 2, 9, 1, 2)

        widgets.DYNAMIC_button_remove_filter = QPushButton(widgets.row_2_DYNAMIC)
        widgets.DYNAMIC_button_remove_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_button_remove_filter.setText("Remove Filter")
        widgets.LG_row_2_DYNAMIC.addWidget(widgets.DYNAMIC_button_remove_filter, 2, 11, 1, 2)


        widgets.verticalLayout_DYNAMIC.addWidget(widgets.row_2_DYNAMIC)


        # ------------------------------------------------------------------------------------------


        widgets.row_3_DYNAMIC = QFrame(widgets.infos_DYNAMIC)
        widgets.row_3_DYNAMIC.setObjectName(u"row_3_DYNAMIC")
        widgets.row_3_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_3_DYNAMIC.setFrameShadow(QFrame.Raised)
        # widgets.row_3_DYNAMIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_3_DYNAMIC.setMinimumHeight(500)

        widgets.LG_row_3_DYNAMIC = QGridLayout(widgets.row_3_DYNAMIC)
        widgets.LG_row_3_DYNAMIC.setSpacing(5)
        widgets.LG_row_3_DYNAMIC.setObjectName(u"LG_row_3_DYNAMIC")
        widgets.LG_row_3_DYNAMIC.setContentsMargins(0, 0, 1, 1)



        widgets.DYNAMIC_sc = MplCanvas(self, width=12, height=12, dpi=100)        
        widgets.DYNAMIC_sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        widgets.toolbar = NavigationToolbar2QT(widgets.DYNAMIC_sc)

        widgets.LG_row_3_DYNAMIC.addWidget(widgets.toolbar   , 0, 0,  1, 10)
        widgets.LG_row_3_DYNAMIC.addWidget(widgets.DYNAMIC_sc, 1, 0, 10, 10)



        widgets.verticalLayout_DYNAMIC.addWidget(widgets.row_3_DYNAMIC)


        # ------------------------------------------------------------------------------------------


        widgets.row_4_DYNAMIC = QFrame(widgets.infos_DYNAMIC)
        widgets.row_4_DYNAMIC.setObjectName(u"row_4_DYNAMIC")
        widgets.row_4_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.row_4_DYNAMIC.setMaximumHeight(130)

        widgets.LG_row_4_DYNAMIC = QGridLayout(widgets.row_4_DYNAMIC)
        widgets.LG_row_4_DYNAMIC.setSpacing(5)
        widgets.LG_row_4_DYNAMIC.setObjectName(u"LG_row_4_DYNAMIC")
        widgets.LG_row_4_DYNAMIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_1_DYNAMIC = QFrame(widgets.row_4_DYNAMIC)
        widgets.row_4_1_DYNAMIC.setObjectName(u"row_4_1_DYNAMIC")
        widgets.row_4_1_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_1_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.row_4_1_DYNAMIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_1_DYNAMIC = QGridLayout(widgets.row_4_1_DYNAMIC)
        widgets.LG_row_4_1_DYNAMIC.setSpacing(5)
        widgets.LG_row_4_1_DYNAMIC.setObjectName(u"LG_row_4_1_DYNAMIC")
        widgets.LG_row_4_1_DYNAMIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_2_DYNAMIC = QFrame(widgets.row_4_DYNAMIC)
        widgets.row_4_2_DYNAMIC.setObjectName(u"row_4_2_DYNAMIC")
        widgets.row_4_2_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_2_DYNAMIC.setFrameShadow(QFrame.Raised)
        widgets.row_4_2_DYNAMIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_2_DYNAMIC = QGridLayout(widgets.row_4_2_DYNAMIC)
        widgets.LG_row_4_2_DYNAMIC.setSpacing(5)
        widgets.LG_row_4_2_DYNAMIC.setObjectName(u"LG_row_4_2_DYNAMIC")
        widgets.LG_row_4_2_DYNAMIC.setContentsMargins(0, 0, 1, 1)



        widgets.LG_row_4_DYNAMIC.addWidget(widgets.row_4_1_DYNAMIC, 0, 0, 1, 1)
        widgets.LG_row_4_DYNAMIC.addWidget(widgets.row_4_2_DYNAMIC, 0, 1, 1, 1)


        # SIXTH ROW


        widgets.DYNAMIC_add_section = QLineEdit(widgets.row_4_1_DYNAMIC)
        widgets.DYNAMIC_add_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_1_DYNAMIC.addWidget(widgets.DYNAMIC_add_section, 0, 0, 1, 4)

        widgets.DYNAMIC_add_section_button = QPushButton(widgets.row_4_1_DYNAMIC)
        widgets.DYNAMIC_add_section_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_add_section_button.setText("Add Section")
        widgets.LG_row_4_1_DYNAMIC.addWidget(widgets.DYNAMIC_add_section_button, 0, 4, 1, 4)

        widgets.DYNAMIC_sections_ava = QComboBox(widgets.row_4_1_DYNAMIC)
        widgets.DYNAMIC_sections_ava.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_1_DYNAMIC.addWidget(widgets.DYNAMIC_sections_ava, 1, 0, 1, 2)

        widgets.DYNAMIC_add_plot = QLineEdit(widgets.row_4_1_DYNAMIC)
        widgets.DYNAMIC_add_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_1_DYNAMIC.addWidget(widgets.DYNAMIC_add_plot, 1, 2, 1, 2)

        widgets.DYNAMIC_add_plot_button = QPushButton(widgets.row_4_1_DYNAMIC)
        widgets.DYNAMIC_add_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_add_plot_button.setText("Add Page")
        widgets.LG_row_4_1_DYNAMIC.addWidget(widgets.DYNAMIC_add_plot_button, 1, 4, 1, 4)


        # SEVENTH ROW


        widgets.DYNAMIC_select_section = QComboBox(widgets.row_4_2_DYNAMIC)
        widgets.DYNAMIC_select_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_2_DYNAMIC.addWidget(widgets.DYNAMIC_select_section, 0, 0, 1, 4)

        widgets.DYNAMIC_select_plot = QComboBox(widgets.row_4_2_DYNAMIC)
        widgets.DYNAMIC_select_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_2_DYNAMIC.addWidget(widgets.DYNAMIC_select_plot, 0, 4, 1, 4)

        widgets.DYNAMIC_add_to_json_button = QPushButton(widgets.row_4_2_DYNAMIC)
        widgets.DYNAMIC_add_to_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_add_to_json_button.setText("Add Plot to Page")
        widgets.LG_row_4_2_DYNAMIC.addWidget(widgets.DYNAMIC_add_to_json_button, 1, 0, 1, 4)

        widgets.DYNAMIC_page_to_plot_button = QPushButton(widgets.row_4_2_DYNAMIC)
        widgets.DYNAMIC_page_to_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_page_to_plot_button.setText("Plot Page")
        widgets.LG_row_4_2_DYNAMIC.addWidget(widgets.DYNAMIC_page_to_plot_button, 1, 4, 1, 4)

        widgets.DYNAMIC_save_json_button = QPushButton(widgets.row_4_2_DYNAMIC)
        widgets.DYNAMIC_save_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_save_json_button.setText("Save")
        widgets.DYNAMIC_save_json_button.setMinimumHeight(80)
        widgets.LG_row_4_2_DYNAMIC.addWidget(widgets.DYNAMIC_save_json_button, 0, 8, 2, 1)


        widgets.verticalLayout_DYNAMIC.addWidget(widgets.row_4_DYNAMIC)


        widgets.mainLayout_DYNAMIC.addWidget(widgets.infos_DYNAMIC)




        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ///                                                                                                                                                ///
        # ///                                                                     DIREITA                                                                    ///
        # ///                                                                                                                                                ///
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



        widgets.pdf_DYNAMIC = QFrame(widgets.DYNAMIC)
        widgets.pdf_DYNAMIC.setObjectName(u"row_1")
        widgets.pdf_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.pdf_DYNAMIC.setFrameShadow(QFrame.Raised)

        widgets.verticalLayout_pdf_DYNAMIC = QVBoxLayout(widgets.pdf_DYNAMIC)
        widgets.verticalLayout_pdf_DYNAMIC.setSpacing(10)
        widgets.verticalLayout_pdf_DYNAMIC.setObjectName(u"verticalLayout_pdf_DYNAMIC")
        widgets.verticalLayout_pdf_DYNAMIC.setContentsMargins(10, 10, 10, 10)





        widgets.row_5_DYNAMIC = QFrame(widgets.pdf_DYNAMIC)
        widgets.row_5_DYNAMIC.setObjectName(u"row_5_DYNAMIC")
        widgets.row_5_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_5_DYNAMIC.setFrameShadow(QFrame.Raised)
        # widgets.row_5_DYNAMIC.setMaximumHeight(110)
        widgets.row_5_DYNAMIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        

        widgets.LG_row_5_DYNAMIC = QGridLayout(widgets.row_5_DYNAMIC)
        widgets.LG_row_5_DYNAMIC.setSpacing(5)
        widgets.LG_row_5_DYNAMIC.setObjectName(u"LG_row_5_DYNAMIC")
        widgets.LG_row_5_DYNAMIC.setContentsMargins(0, 0, 1, 1)



        # FIRST ROW

        widgets.DYNAMIC_search_json_button = QPushButton(widgets.row_5_DYNAMIC)
        widgets.DYNAMIC_search_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_search_json_button.setText("Search")
        widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_search_json_button, 0, 0, 1, 2)

        widgets.DYNAMIC_qline_json_files = QLineEdit(widgets.row_5_DYNAMIC)
        widgets.DYNAMIC_qline_json_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_json_files, 0, 2, 1, 8)

        widgets.DYNAMIC_read_json_button = QPushButton(widgets.row_5_DYNAMIC)
        widgets.DYNAMIC_read_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.DYNAMIC_read_json_button.setText("Open")
        widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_read_json_button, 0, 10, 1, 2)

        # # SECOND ROW

        # widgets.DYNAMIC_label_00 = QLabel(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_label_00.setText("File")
        # widgets.DYNAMIC_label_00.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_label_00, 1, 0, 1, 6)

        # widgets.DYNAMIC_qline_00 = QLineEdit(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_qline_00.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_00, 2, 0, 1, 6)


        # widgets.DYNAMIC_label_01 = QLabel(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_label_01.setText("Version")
        # widgets.DYNAMIC_label_01.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_label_01, 1, 6, 1, 6)

        # widgets.DYNAMIC_qline_01 = QLineEdit(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_qline_01.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_01, 2, 6, 1, 6)


        # # THIRD ROW

        # widgets.DYNAMIC_label_10 = QLabel(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_label_10.setText("Responsible")
        # widgets.DYNAMIC_label_10.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_label_10, 3, 0, 1, 6)

        # widgets.DYNAMIC_qline_10 = QLineEdit(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_qline_10.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_10, 4, 0, 1, 6)


        # widgets.DYNAMIC_label_11 = QLabel(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_label_11.setText("Date")
        # widgets.DYNAMIC_label_11.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_label_11, 3, 6, 1, 6)

        # widgets.DYNAMIC_qline_11 = QLineEdit(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_qline_11.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_11, 4, 6, 1, 6)

        # # THIRD ROW

        # widgets.DYNAMIC_label_20 = QLabel(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_label_20.setText("")
        # widgets.DYNAMIC_label_20.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_label_20, 5, 0, 1, 6)

        # widgets.DYNAMIC_qline_20 = QLineEdit(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_qline_20.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_20, 6, 0, 1, 6)


        # widgets.DYNAMIC_label_21 = QLabel(widgets.row_5_DYNAMIC) 
        # widgets.DYNAMIC_label_21.setText("")
        # widgets.DYNAMIC_label_21.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_label_21, 5, 6, 1, 6)

        # widgets.DYNAMIC_qline_21 = QLineEdit(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_qline_21.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_21, 6, 6, 1, 6)


        # # THIRD ROW

        # widgets.DYNAMIC_label_30 = QLabel(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_label_30.setText("Comment")
        # widgets.DYNAMIC_label_30.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_label_30, 7, 0, 1, 12)

        # widgets.DYNAMIC_qline_30 = QLineEdit(widgets.row_5_DYNAMIC)
        # widgets.DYNAMIC_qline_30.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_DYNAMIC.addWidget(widgets.DYNAMIC_qline_30, 8, 0, 1, 12)





        # widgets.DYNAMIC_read_vars_button = QPushButton(widgets.row_1_DYNAMIC)
        # widgets.DYNAMIC_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.DYNAMIC_read_vars_button.setText("Open")
        # widgets.LG_row_1_DYNAMIC.addWidget(widgets.DYNAMIC_read_vars_button, 1, 10, 1, 2)



        widgets.verticalLayout_pdf_DYNAMIC.addWidget(widgets.row_5_DYNAMIC)





        

      


        widgets.d_row_1_DYNAMIC = QFrame(widgets.pdf_DYNAMIC)
        widgets.d_row_1_DYNAMIC.setObjectName(u"d_row_1_DYNAMIC")
        widgets.d_row_1_DYNAMIC.setFrameShape(QFrame.StyledPanel)
        widgets.d_row_1_DYNAMIC.setFrameShadow(QFrame.Raised)
        # widgets.d_row_1_DYNAMIC.setMaximumHeight(600)
        # widgets.d_row_1_DYNAMIC.setMaximumSize(QSize(600, 400))

        widgets.d_LG_row_1_DYNAMIC = QGridLayout(widgets.d_row_1_DYNAMIC)
        widgets.d_LG_row_1_DYNAMIC.setSpacing(0)
        widgets.d_LG_row_1_DYNAMIC.setObjectName(u"d_LG_row_1_DYNAMIC")
        widgets.d_LG_row_1_DYNAMIC.setContentsMargins(0, 0, 1, 1)

        ## ============================


        widgets.pdfView_DYNAMIC = QPdfView(widgets.pdf_DYNAMIC)
        widgets.pdfView_DYNAMIC.setObjectName(u"pdfView_DYNAMIC")

        widgets.DYNAMIC_document = QPdfDocument(widgets.pdf_DYNAMIC)

        widgets.pdfView_DYNAMIC.setDocument(widgets.DYNAMIC_document)


        ## ============================



        widgets.mainToolBar = QToolBar(widgets.d_row_1_DYNAMIC)
        widgets.mainToolBar.setObjectName(u"mainToolBar")
        widgets.mainToolBar.setMovable(False)
        widgets.mainToolBar.setFloatable(False)


        # ACTIONS


        widgets.run_DYNAMIC = QPushButton(widgets.d_row_1_DYNAMIC)
        widgets.run_DYNAMIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.run_DYNAMIC.setText("Run")

        widgets.actionZoom_In_DYNAMIC = QPushButton(widgets.d_row_1_DYNAMIC)
        widgets.actionZoom_In_DYNAMIC.setText('In')
        widgets.actionZoom_In_DYNAMIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionZoom_Out_DYNAMIC = QPushButton(widgets.d_row_1_DYNAMIC)
        widgets.actionZoom_Out_DYNAMIC.setText('Out')
        widgets.actionZoom_Out_DYNAMIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_zoomSelector_DYNAMIC = ZoomSelector(widgets.d_row_1_DYNAMIC)
        widgets.m_zoomSelector_DYNAMIC.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.m_zoomSelector_DYNAMIC.zoom_mode_changed.connect(widgets.pdfView_DYNAMIC.setZoomMode)
        widgets.m_zoomSelector_DYNAMIC.zoom_factor_changed.connect(widgets.pdfView_DYNAMIC.setZoomFactor)
        widgets.m_zoomSelector_DYNAMIC.reset()
        widgets.pdfView_DYNAMIC.zoomFactorChanged.connect(widgets.m_zoomSelector_DYNAMIC.set_zoom_factor)

        widgets.actionPage_down_DYNAMIC = QPushButton(widgets.d_row_1_DYNAMIC)
        widgets.actionPage_down_DYNAMIC.setText('-')
        widgets.actionPage_down_DYNAMIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionPage_up_DYNAMIC = QPushButton(widgets.d_row_1_DYNAMIC)
        widgets.actionPage_up_DYNAMIC.setText('+')
        widgets.actionPage_up_DYNAMIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_pageSelector_DYNAMIC = QSpinBox(widgets.d_row_1_DYNAMIC)
        widgets.m_pageSelector_DYNAMIC.valueChanged.connect(widgets.page_selected)
        widgets.m_pageSelector_DYNAMIC.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        nav = widgets.pdfView_DYNAMIC.pageNavigator()
        nav.currentPageChanged.connect(widgets.m_pageSelector_DYNAMIC.setValue)

    
        widgets.actionSave_DYNAMIC = QPushButton(widgets.d_row_1_DYNAMIC)
        widgets.actionSave_DYNAMIC.setText('Save')
        widgets.actionSave_DYNAMIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")





        widgets.mainToolBar.addWidget(widgets.run_DYNAMIC)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_In_DYNAMIC)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_zoomSelector_DYNAMIC)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_Out_DYNAMIC)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_down_DYNAMIC)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_pageSelector_DYNAMIC)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_up_DYNAMIC)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionSave_DYNAMIC)




        ## =============


        widgets.d_LG_row_1_DYNAMIC.addWidget(widgets.mainToolBar, 0, 0, 1, 1)
        widgets.d_LG_row_1_DYNAMIC.addWidget(widgets.pdfView_DYNAMIC, 1, 0, 1, 1)

        widgets.verticalLayout_pdf_DYNAMIC.addWidget(widgets.d_row_1_DYNAMIC)
        widgets.mainLayout_DYNAMIC.addWidget(widgets.pdf_DYNAMIC)
       

        # ADD ALL

        widgets.stackedWidget.addWidget(widgets.DYNAMIC)






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









class NET_Widgets(object):

    def __init__(self):


        pass

    
    def _create_network(self, widgets):

        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(120)
        font1.setBold(True)
        font1.setItalic(False)
        widgets.styleSheet.setFont(font1)

        widgets.NETWORK = QWidget()
        widgets.NETWORK.setObjectName(u"NETWORK")
        widgets.NETWORK.setStyleSheet(u"b")

        widgets.mainLayout_NETWORK = QHBoxLayout(widgets.NETWORK)
        widgets.mainLayout_NETWORK.setSpacing(10)
        widgets.mainLayout_NETWORK.setObjectName(u"mainLayout_NETWORK")
        widgets.mainLayout_NETWORK.setContentsMargins(10, 10, 10, 10)

        # === ESQUERDA

        widgets.infos_NETWORK = QFrame(widgets.NETWORK)
        widgets.infos_NETWORK.setObjectName(u"row_1")
        widgets.infos_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.infos_NETWORK.setFrameShadow(QFrame.Raised)
        widgets.infos_NETWORK.setMinimumWidth(800)

        widgets.verticalLayout_NETWORK = QVBoxLayout(widgets.infos_NETWORK)
        widgets.verticalLayout_NETWORK.setSpacing(10)
        widgets.verticalLayout_NETWORK.setObjectName(u"verticalLayout_NETWORK")
        widgets.verticalLayout_NETWORK.setContentsMargins(10, 10, 10, 10)

        # ROW 1

        widgets.row_1_NETWORK = QFrame(widgets.infos_NETWORK)
        widgets.row_1_NETWORK.setObjectName(u"row_1_NETWORK")
        widgets.row_1_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_NETWORK.setFrameShadow(QFrame.Raised)
        widgets.row_1_NETWORK.setMaximumHeight(110)
        widgets.row_1_NETWORK.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        

        widgets.LG_row_1_NETWORK = QGridLayout(widgets.row_1_NETWORK)
        widgets.LG_row_1_NETWORK.setSpacing(5)
        widgets.LG_row_1_NETWORK.setObjectName(u"LG_row_1_NETWORK")
        widgets.LG_row_1_NETWORK.setContentsMargins(0, 0, 1, 1)



        # FIRST ROW

        widgets.NETWORK_search_button = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_search_button.setText("Search")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_search_button, 0, 0, 1, 2)

        widgets.NETWORK_qline_files = QLineEdit(widgets.row_1_NETWORK)
        widgets.NETWORK_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_qline_files, 0, 2, 1, 8)

        widgets.NETWORK_read_file_button = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_read_file_button.setText("Process")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_read_file_button, 0, 10, 1, 2)

        # SECOND ROW



        widgets.NETWORK_vars_search = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_vars_search.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_vars_search.setText("Processed")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_vars_search, 1, 0, 1, 2)

        widgets.NETWORK_vars_qline = QLineEdit(widgets.row_1_NETWORK)
        widgets.NETWORK_vars_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_vars_qline, 1, 2, 1, 8)

        widgets.NETWORK_read_vars_button = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_read_vars_button.setText("Open")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_read_vars_button, 1, 10, 1, 2)


        # SPECIAL BUTTONS

        widgets.NETWORK_instavel = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_instavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_instavel.setText("Instável")
        widgets.NETWORK_instavel.setMinimumWidth(20)
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_instavel, 0, 13, 1, 1)        

        widgets.NETWORK_estavel = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_estavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_estavel.setText("Estável")
        widgets.NETWORK_estavel.setMinimumWidth(130)
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_estavel, 0, 14, 1, 1)

        widgets.NETWORK_per_cont = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_per_cont.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_per_cont.setText("Por Contingência")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_per_cont, 1, 13, 1, 1)

        widgets.NETWORK_per_group = QPushButton(widgets.row_1_NETWORK)
        widgets.NETWORK_per_group.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_per_group.setText("Por Grupo")
        widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_per_group, 1, 14, 1, 1)


        widgets.verticalLayout_NETWORK.addWidget(widgets.row_1_NETWORK)


        # ------------------------------------------------------------------------------------------


        widgets.row_2_NETWORK = QFrame(widgets.infos_NETWORK)
        widgets.row_2_NETWORK.setObjectName(u"row_2_NETWORK")
        widgets.row_2_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.row_2_NETWORK.setFrameShadow(QFrame.Raised)
        widgets.row_2_NETWORK.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_2_NETWORK.setMaximumHeight(130)

        widgets.LG_row_2_NETWORK = QGridLayout(widgets.row_2_NETWORK)
        widgets.LG_row_2_NETWORK.setSpacing(5)
        widgets.LG_row_2_NETWORK.setObjectName(u"LG_row_2_NETWORK")
        widgets.LG_row_2_NETWORK.setContentsMargins(0, 0, 1, 1)


        # THIRD ROW


        widgets.NETWORK_x = QComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_x.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_x, 0, 0, 1, 3)

        widgets.NETWORK_y = QComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_y.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_y, 0, 3, 1, 3)

        widgets.NETWORK_c = QComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_c.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_c, 0, 6, 1, 3)

        # FOURTH ROW

        widgets.NETWORK_plot = QComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_plot, 1, 0, 1, 3)

        widgets.NETWORK_round = QComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_round.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_round, 1, 3, 1, 3)


        widgets.NETWORK_stats = QComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_stats.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_stats, 1, 6, 1, 3)

        # PLOT BUTTON

        widgets.NETWORK_plot_button = QPushButton(widgets.row_2_NETWORK)
        widgets.NETWORK_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_plot_button.setText("Plot")
        widgets.NETWORK_plot_button.setMinimumHeight(70)
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_plot_button, 0, 9, 2, 4)

        # FIFTH ROW

        widgets.NETWORK_combo_variable = ExtendedComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_combo_variable.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_combo_variable, 2, 0, 1, 3)

        widgets.NETWORK_combo_sinal = QComboBox(widgets.row_2_NETWORK)
        widgets.NETWORK_combo_sinal.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_combo_sinal, 2, 3, 1, 3)

        widgets.NETWORK_label_value = QLineEdit(widgets.row_2_NETWORK)
        widgets.NETWORK_label_value.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_label_value, 2, 6, 1, 3)

        widgets.NETWORK_button_apply_filter = QPushButton(widgets.row_2_NETWORK)
        widgets.NETWORK_button_apply_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_button_apply_filter.setText("Apply Filter")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_button_apply_filter, 2, 9, 1, 2)

        widgets.NETWORK_button_remove_filter = QPushButton(widgets.row_2_NETWORK)
        widgets.NETWORK_button_remove_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_button_remove_filter.setText("Remove Filter")
        widgets.LG_row_2_NETWORK.addWidget(widgets.NETWORK_button_remove_filter, 2, 11, 1, 2)


        widgets.verticalLayout_NETWORK.addWidget(widgets.row_2_NETWORK)


        # ------------------------------------------------------------------------------------------


        widgets.row_3_NETWORK = QFrame(widgets.infos_NETWORK)
        widgets.row_3_NETWORK.setObjectName(u"row_3_NETWORK")
        widgets.row_3_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.row_3_NETWORK.setFrameShadow(QFrame.Raised)
        # widgets.row_3_NETWORK.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_3_NETWORK.setMinimumHeight(500)

        widgets.LG_row_3_NETWORK = QGridLayout(widgets.row_3_NETWORK)
        widgets.LG_row_3_NETWORK.setSpacing(5)
        widgets.LG_row_3_NETWORK.setObjectName(u"LG_row_3_NETWORK")
        widgets.LG_row_3_NETWORK.setContentsMargins(0, 0, 1, 1)



        widgets.NETWORK_sc = MplCanvas(self, width=12, height=12, dpi=100)        
        widgets.NETWORK_sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        widgets.toolbar = NavigationToolbar2QT(widgets.NETWORK_sc)

        widgets.LG_row_3_NETWORK.addWidget(widgets.toolbar   , 0, 0,  1, 10)
        widgets.LG_row_3_NETWORK.addWidget(widgets.NETWORK_sc, 1, 0, 10, 10)



        widgets.verticalLayout_NETWORK.addWidget(widgets.row_3_NETWORK)


        # ------------------------------------------------------------------------------------------


        widgets.row_4_NETWORK = QFrame(widgets.infos_NETWORK)
        widgets.row_4_NETWORK.setObjectName(u"row_4_NETWORK")
        widgets.row_4_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_NETWORK.setFrameShadow(QFrame.Raised)
        widgets.row_4_NETWORK.setMaximumHeight(130)

        widgets.LG_row_4_NETWORK = QGridLayout(widgets.row_4_NETWORK)
        widgets.LG_row_4_NETWORK.setSpacing(5)
        widgets.LG_row_4_NETWORK.setObjectName(u"LG_row_4_NETWORK")
        widgets.LG_row_4_NETWORK.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_1_NETWORK = QFrame(widgets.row_4_NETWORK)
        widgets.row_4_1_NETWORK.setObjectName(u"row_4_1_NETWORK")
        widgets.row_4_1_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_1_NETWORK.setFrameShadow(QFrame.Raised)
        widgets.row_4_1_NETWORK.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_1_NETWORK = QGridLayout(widgets.row_4_1_NETWORK)
        widgets.LG_row_4_1_NETWORK.setSpacing(5)
        widgets.LG_row_4_1_NETWORK.setObjectName(u"LG_row_4_1_NETWORK")
        widgets.LG_row_4_1_NETWORK.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_2_NETWORK = QFrame(widgets.row_4_NETWORK)
        widgets.row_4_2_NETWORK.setObjectName(u"row_4_2_NETWORK")
        widgets.row_4_2_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_2_NETWORK.setFrameShadow(QFrame.Raised)
        widgets.row_4_2_NETWORK.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_2_NETWORK = QGridLayout(widgets.row_4_2_NETWORK)
        widgets.LG_row_4_2_NETWORK.setSpacing(5)
        widgets.LG_row_4_2_NETWORK.setObjectName(u"LG_row_4_2_NETWORK")
        widgets.LG_row_4_2_NETWORK.setContentsMargins(0, 0, 1, 1)



        widgets.LG_row_4_NETWORK.addWidget(widgets.row_4_1_NETWORK, 0, 0, 1, 1)
        widgets.LG_row_4_NETWORK.addWidget(widgets.row_4_2_NETWORK, 0, 1, 1, 1)


        # SIXTH ROW


        widgets.NETWORK_add_section = QLineEdit(widgets.row_4_1_NETWORK)
        widgets.NETWORK_add_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_1_NETWORK.addWidget(widgets.NETWORK_add_section, 0, 0, 1, 3)

        widgets.NETWORK_add_section_button = QPushButton(widgets.row_4_1_NETWORK)
        widgets.NETWORK_add_section_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_add_section_button.setText("Add Section")
        widgets.LG_row_4_1_NETWORK.addWidget(widgets.NETWORK_add_section_button, 0, 3, 1, 3)

        widgets.NETWORK_add_plot = QLineEdit(widgets.row_4_1_NETWORK)
        widgets.NETWORK_add_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_1_NETWORK.addWidget(widgets.NETWORK_add_plot, 1, 0, 1, 3)

        widgets.NETWORK_add_plot_button = QPushButton(widgets.row_4_1_NETWORK)
        widgets.NETWORK_add_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_add_plot_button.setText("Add Page")
        widgets.LG_row_4_1_NETWORK.addWidget(widgets.NETWORK_add_plot_button, 1, 3, 1, 3)


        # SEVENTH ROW


        widgets.NETWORK_select_section = QComboBox(widgets.row_4_2_NETWORK)
        widgets.NETWORK_select_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_2_NETWORK.addWidget(widgets.NETWORK_select_section, 0, 0, 1, 4)

        widgets.NETWORK_select_plot = QComboBox(widgets.row_4_2_NETWORK)
        widgets.NETWORK_select_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_4_2_NETWORK.addWidget(widgets.NETWORK_select_plot, 0, 4, 1, 4)

        widgets.NETWORK_add_to_json_button = QPushButton(widgets.row_4_2_NETWORK)
        widgets.NETWORK_add_to_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_add_to_json_button.setText("Add Plot to Page")
        widgets.LG_row_4_2_NETWORK.addWidget(widgets.NETWORK_add_to_json_button, 1, 0, 1, 8)

        widgets.verticalLayout_NETWORK.addWidget(widgets.row_4_NETWORK)


        widgets.mainLayout_NETWORK.addWidget(widgets.infos_NETWORK)




        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ///                                                                                                                                                ///
        # ///                                                                     DIREITA                                                                    ///
        # ///                                                                                                                                                ///
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



        widgets.pdf_NETWORK = QFrame(widgets.NETWORK)
        widgets.pdf_NETWORK.setObjectName(u"row_1")
        widgets.pdf_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.pdf_NETWORK.setFrameShadow(QFrame.Raised)

        widgets.verticalLayout_pdf_NETWORK = QVBoxLayout(widgets.pdf_NETWORK)
        widgets.verticalLayout_pdf_NETWORK.setSpacing(10)
        widgets.verticalLayout_pdf_NETWORK.setObjectName(u"verticalLayout_pdf_NETWORK")
        widgets.verticalLayout_pdf_NETWORK.setContentsMargins(10, 10, 10, 10)





        widgets.row_5_NETWORK = QFrame(widgets.pdf_NETWORK)
        widgets.row_5_NETWORK.setObjectName(u"row_5_NETWORK")
        widgets.row_5_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.row_5_NETWORK.setFrameShadow(QFrame.Raised)
        # widgets.row_5_NETWORK.setMaximumHeight(110)
        widgets.row_5_NETWORK.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        

        widgets.LG_row_5_NETWORK = QGridLayout(widgets.row_5_NETWORK)
        widgets.LG_row_5_NETWORK.setSpacing(5)
        widgets.LG_row_5_NETWORK.setObjectName(u"LG_row_5_NETWORK")
        widgets.LG_row_5_NETWORK.setContentsMargins(0, 0, 1, 1)



        # FIRST ROW

        widgets.NETWORK_search_button = QPushButton(widgets.row_5_NETWORK)
        widgets.NETWORK_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_search_button.setText("Search")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_search_button, 0, 0, 1, 2)

        widgets.NETWORK_qline_files = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_files, 0, 2, 1, 8)

        widgets.NETWORK_read_file_button = QPushButton(widgets.row_5_NETWORK)
        widgets.NETWORK_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.NETWORK_read_file_button.setText("Process")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_read_file_button, 0, 10, 1, 2)

        # SECOND ROW

        widgets.NETWORK_label_00 = QLabel(widgets.row_5_NETWORK)
        widgets.NETWORK_label_00.setText("Processed")
        widgets.NETWORK_label_00.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_label_00, 1, 0, 1, 6)

        widgets.NETWORK_qline_00 = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_00.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_00, 2, 0, 1, 6)


        widgets.NETWORK_label_01 = QLabel(widgets.row_5_NETWORK)
        widgets.NETWORK_label_01.setText("Processed")
        widgets.NETWORK_label_01.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_label_01, 1, 6, 1, 6)

        widgets.NETWORK_qline_01 = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_01.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_01, 2, 6, 1, 6)


        # THIRD ROW

        widgets.NETWORK_label_10 = QLabel(widgets.row_5_NETWORK)
        widgets.NETWORK_label_10.setText("Processed")
        widgets.NETWORK_label_10.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_label_10, 3, 0, 1, 6)

        widgets.NETWORK_qline_10 = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_10.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_10, 4, 0, 1, 6)


        widgets.NETWORK_label_11 = QLabel(widgets.row_5_NETWORK)
        widgets.NETWORK_label_11.setText("Processed")
        widgets.NETWORK_label_11.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_label_11, 3, 6, 1, 6)

        widgets.NETWORK_qline_11 = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_11.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_11, 4, 6, 1, 6)

        # THIRD ROW

        widgets.NETWORK_label_20 = QLabel(widgets.row_5_NETWORK)
        widgets.NETWORK_label_20.setText("Processed")
        widgets.NETWORK_label_20.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_label_20, 5, 0, 1, 6)

        widgets.NETWORK_qline_20 = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_20.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_20, 6, 0, 1, 6)


        widgets.NETWORK_label_21 = QLabel(widgets.row_5_NETWORK)
        widgets.NETWORK_label_21.setText("Processed")
        widgets.NETWORK_label_21.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_label_21, 5, 6, 1, 6)

        widgets.NETWORK_qline_21 = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_21.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_21, 6, 6, 1, 6)


        # THIRD ROW

        widgets.NETWORK_label_30 = QLabel(widgets.row_5_NETWORK)
        widgets.NETWORK_label_30.setText("Processed")
        widgets.NETWORK_label_30.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_label_30, 7, 0, 1, 12)

        widgets.NETWORK_qline_30 = QLineEdit(widgets.row_5_NETWORK)
        widgets.NETWORK_qline_30.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_5_NETWORK.addWidget(widgets.NETWORK_qline_30, 8, 0, 1, 12)





        # widgets.NETWORK_read_vars_button = QPushButton(widgets.row_1_NETWORK)
        # widgets.NETWORK_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.NETWORK_read_vars_button.setText("Open")
        # widgets.LG_row_1_NETWORK.addWidget(widgets.NETWORK_read_vars_button, 1, 10, 1, 2)



        widgets.verticalLayout_pdf_NETWORK.addWidget(widgets.row_5_NETWORK)





        

      


        widgets.d_row_1_NETWORK = QFrame(widgets.pdf_NETWORK)
        widgets.d_row_1_NETWORK.setObjectName(u"d_row_1_NETWORK")
        widgets.d_row_1_NETWORK.setFrameShape(QFrame.StyledPanel)
        widgets.d_row_1_NETWORK.setFrameShadow(QFrame.Raised)
        widgets.d_row_1_NETWORK.setMaximumHeight(600)
        # widgets.d_row_1_NETWORK.setMaximumSize(QSize(600, 400))

        widgets.d_LG_row_1_NETWORK = QGridLayout(widgets.d_row_1_NETWORK)
        widgets.d_LG_row_1_NETWORK.setSpacing(0)
        widgets.d_LG_row_1_NETWORK.setObjectName(u"d_LG_row_1_NETWORK")
        widgets.d_LG_row_1_NETWORK.setContentsMargins(0, 0, 1, 1)

        ## ============================


        widgets.pdfView_NETWORK = QPdfView(widgets.pdf_NETWORK)
        widgets.pdfView_NETWORK.setObjectName(u"pdfView_NETWORK")

        widgets.m_document = QPdfDocument(widgets.pdf_NETWORK)

        widgets.pdfView_NETWORK.setDocument(widgets.m_document)


        ## ============================



        widgets.mainToolBar = QToolBar(widgets.d_row_1_NETWORK)
        widgets.mainToolBar.setObjectName(u"mainToolBar")
        widgets.mainToolBar.setMovable(False)
        widgets.mainToolBar.setFloatable(False)


        # ACTIONS


        widgets.run_NETWORK = QPushButton(widgets.d_row_1_NETWORK)
        widgets.run_NETWORK.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.run_NETWORK.setText("Run")

        widgets.actionZoom_In_NETWORK = QPushButton(widgets.d_row_1_NETWORK)
        widgets.actionZoom_In_NETWORK.setText('In')
        widgets.actionZoom_In_NETWORK.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionZoom_Out = QPushButton(widgets.d_row_1_NETWORK)
        widgets.actionZoom_Out.setText('Out')
        widgets.actionZoom_Out.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_zoomSelector = ZoomSelector(widgets.d_row_1_NETWORK)
        widgets.m_zoomSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.m_zoomSelector.setMaximumWidth(150)
        widgets.m_zoomSelector.zoom_mode_changed.connect(widgets.pdfView_NETWORK.setZoomMode)
        widgets.m_zoomSelector.zoom_factor_changed.connect(widgets.pdfView_NETWORK.setZoomFactor)
        widgets.m_zoomSelector.reset()
        widgets.pdfView_NETWORK.zoomFactorChanged.connect(widgets.m_zoomSelector.set_zoom_factor)

        widgets.actionPage_down_NETWORK = QPushButton(widgets.d_row_1_NETWORK)
        widgets.actionPage_down_NETWORK.setText('-')
        widgets.actionPage_down_NETWORK.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.actionPage_up_NETWORK = QPushButton(widgets.d_row_1_NETWORK)
        widgets.actionPage_up_NETWORK.setText('+')
        widgets.actionPage_up_NETWORK.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        widgets.m_pageSelector = QSpinBox(widgets.d_row_1_NETWORK)
        widgets.m_pageSelector.valueChanged.connect(widgets.page_selected)
        widgets.m_pageSelector.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        nav = widgets.pdfView_NETWORK.pageNavigator()
        nav.currentPageChanged.connect(widgets.m_pageSelector.setValue)
        # nav.backAvailableChanged.connect(widgets.actionBack.setEnabled)
        # nav.forwardAvailableChanged.connect(widgets.actionForward.setEnabled)

        widgets.actionSave = QPushButton(widgets.d_row_1_NETWORK)
        widgets.actionSave.setText('Save')
        widgets.actionSave.setStyleSheet(u"background-color: rgb(91, 95, 199)")





        widgets.mainToolBar.addWidget(widgets.run_NETWORK)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_In_NETWORK)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_zoomSelector)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionZoom_Out)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_down_NETWORK)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.m_pageSelector)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionPage_up_NETWORK)
        widgets.mainToolBar.addSeparator()
        widgets.mainToolBar.addWidget(widgets.actionSave)




        ## =============


        widgets.d_LG_row_1_NETWORK.addWidget(widgets.mainToolBar, 0, 0, 1, 1)
        widgets.d_LG_row_1_NETWORK.addWidget(widgets.pdfView_NETWORK, 1, 0, 1, 1)

        widgets.verticalLayout_pdf_NETWORK.addWidget(widgets.d_row_1_NETWORK)
        widgets.mainLayout_NETWORK.addWidget(widgets.pdf_NETWORK)
       

        # ADD ALL

        widgets.stackedWidget.addWidget(widgets.NETWORK)






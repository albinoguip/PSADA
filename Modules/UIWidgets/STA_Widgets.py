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









class STA_Widgets(object):

    def __init__(self):

        pass

    
    def _create_static(self, widgets):

        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(120)
        font1.setBold(True)
        font1.setItalic(False)
        widgets.styleSheet.setFont(font1)

        widgets.STATIC = QWidget()
        widgets.STATIC.setObjectName(u"STATIC")
        widgets.STATIC.setStyleSheet(u"b")

        widgets.mainLayout_STATIC = QHBoxLayout(widgets.STATIC)
        widgets.mainLayout_STATIC.setSpacing(10)
        widgets.mainLayout_STATIC.setObjectName(u"mainLayout_STATIC")
        widgets.mainLayout_STATIC.setContentsMargins(10, 10, 10, 10)

        # === ESQUERDA

        widgets.infos_STATIC = QFrame(widgets.STATIC)
        widgets.infos_STATIC.setObjectName(u"row_1")
        widgets.infos_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.infos_STATIC.setFrameShadow(QFrame.Raised)
        widgets.infos_STATIC.setMinimumWidth(800)

        widgets.verticalLayout_STATIC = QVBoxLayout(widgets.infos_STATIC)
        widgets.verticalLayout_STATIC.setSpacing(10)
        widgets.verticalLayout_STATIC.setObjectName(u"verticalLayout_STATIC")
        widgets.verticalLayout_STATIC.setContentsMargins(10, 10, 10, 10)



        # Testando janela de opções para geração e processamento dos arquivos

        widgets.row_0_STATIC = QFrame(widgets.infos_STATIC)
        widgets.row_0_STATIC.setObjectName(u"row_0_STATIC")
        widgets.row_0_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_0_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_0_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_0_STATIC.setMaximumHeight(200)

        widgets.LG_row_0_STATIC = QGridLayout(widgets.row_0_STATIC)
        widgets.LG_row_0_STATIC.setSpacing(5)
        widgets.LG_row_0_STATIC.setObjectName(u"LG_row_0_STATIC")
        widgets.LG_row_0_STATIC.setContentsMargins(0, 0, 1, 1)

        # widgets.row_0_1_STATIC = QFrame(widgets.row_0_STATIC)
        # widgets.row_0_1_STATIC.setObjectName(u"row_0_1_STATIC")
        # widgets.row_0_1_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_0_1_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_0_1_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        # widgets.LG_row_0_1_STATIC = QGridLayout(widgets.row_0_1_STATIC)
        # widgets.LG_row_0_1_STATIC.setSpacing(5)
        # widgets.LG_row_0_1_STATIC.setObjectName(u"LG_row_1_1_STATIC")
        # widgets.LG_row_0_1_STATIC.setContentsMargins(0, 0, 1, 1)

        # widgets.LG_row_0_STATIC.addWidget(widgets.row_0_1_STATIC, 0, 0, 1, 3)

        #Norma
        widgets.STATIC_norm_label = QLabel("Norm:")
        widgets.STATIC_norm_label.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_norm_combobox = QComboBox()
        widgets.STATIC_norm_combobox.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.STATIC_norm_combobox.addItems(["None", "1", "2", "3"])  # Exemplo de normas
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_norm_label, 0, 0, 1, 2)
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_norm_combobox, 0, 2, 1, 4)

        # OneCase (ComboBox)
        widgets.STATIC_onecase_label = QLabel("OneCase:")
        widgets.STATIC_onecase_label.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_onecase_combobox = QComboBox()
        widgets.STATIC_onecase_combobox.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.STATIC_onecase_combobox.addItems(["1", "2"])
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onecase_label, 1, 0, 1, 2)
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onecase_combobox, 1, 2, 1, 4)

        #OnlyPWF_datagen
        widgets.STATIC_onlypwf = QCheckBox('Only PWF Datagen')
        widgets.STATIC_onlypwf.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onlypwf, 2, 0, 1, 2)

        #Extract from CSV
        widgets.STATIC_extract_from_csv = QCheckBox('Extract from CSV')
        widgets.STATIC_extract_from_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_extract_from_csv, 2, 2, 1, 1)


        #Bus Data
        widgets.STATIC_bus_data = QCheckBox('Bus Data')
        widgets.STATIC_bus_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_bus_data, 2, 3, 1, 1)


        #Linhas data
        widgets.STATIC_line_data = QCheckBox('Linha Data')
        widgets.STATIC_line_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_line_data, 2, 4, 1, 1)

        #HVDCData
        widgets.STATIC_hvdc_data = QCheckBox('HVDC Data')
        widgets.STATIC_hvdc_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_hvdc_data, 2, 5, 1, 1)

        #ReservaData
        widgets.STATIC_reserva_data = QCheckBox('Reserva Data')
        widgets.STATIC_reserva_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_reserva_data, 3, 0, 1, 1)

        #IntercambiosData
        widgets.STATIC_intercambio_data = QCheckBox('Intercambios Data')
        widgets.STATIC_intercambio_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_intercambio_data, 3, 1, 1, 1)

        #ComputeDPI
        widgets.STATIC_compute_dpi = QCheckBox('Compute DPI')
        widgets.STATIC_compute_dpi.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_compute_dpi, 3, 2, 1, 1)

        #linhascsv
        widgets.STATIC_linhas_csv = QCheckBox('Linhas CSV')
        widgets.STATIC_linhas_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_linhas_csv, 3, 3, 1, 1)

        #reservacsv
        widgets.STATIC_reserva_csv = QCheckBox('Reserva CSV')
        widgets.STATIC_reserva_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_reserva_csv, 3, 4, 1, 1)

        #HVDCcsv
        widgets.STATIC_hvdc_csv = QCheckBox('HVDC CSV')
        widgets.STATIC_hvdc_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_hvdc_csv, 3, 5, 1, 1)

        widgets.verticalLayout_STATIC.addWidget(widgets.row_0_STATIC)

        # ROW 1

        widgets.row_1_STATIC = QFrame(widgets.infos_STATIC)
        widgets.row_1_STATIC.setObjectName(u"row_1_STATIC")
        widgets.row_1_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_1_STATIC.setMaximumHeight(110)
        

        widgets.LG_row_1_STATIC = QGridLayout(widgets.row_1_STATIC)
        widgets.LG_row_1_STATIC.setSpacing(5)
        widgets.LG_row_1_STATIC.setObjectName(u"LG_row_1_STATIC")
        widgets.LG_row_1_STATIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_1_1_STATIC = QFrame(widgets.row_1_STATIC)
        widgets.row_1_1_STATIC.setObjectName(u"row_1_1_STATIC")
        widgets.row_1_1_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_1_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_1_1_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_1_1_STATIC = QGridLayout(widgets.row_1_1_STATIC)
        widgets.LG_row_1_1_STATIC.setSpacing(5)
        widgets.LG_row_1_1_STATIC.setObjectName(u"LG_row_1_1_STATIC")
        widgets.LG_row_1_1_STATIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_1_2_STATIC = QFrame(widgets.row_1_STATIC)
        widgets.row_1_2_STATIC.setObjectName(u"row_1_2_STATIC")
        widgets.row_1_2_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_1_2_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_1_2_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_1_2_STATIC = QGridLayout(widgets.row_1_2_STATIC)
        widgets.LG_row_1_2_STATIC.setSpacing(5)
        widgets.LG_row_1_2_STATIC.setObjectName(u"LG_row_1_2_STATIC")
        widgets.LG_row_1_2_STATIC.setContentsMargins(0, 0, 1, 1)



        widgets.LG_row_1_STATIC.addWidget(widgets.row_1_1_STATIC, 0, 0, 1, 3)
        widgets.LG_row_1_STATIC.addWidget(widgets.row_1_2_STATIC, 0, 3, 1, 1)



        # FIRST ROW

        widgets.STATIC_search_button = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_search_button.setText("Search")
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_search_button, 0, 0, 1, 2)

        widgets.STATIC_qline_files = QLineEdit(widgets.row_1_1_STATIC)
        widgets.STATIC_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_qline_files, 0, 2, 1, 8)

        widgets.STATIC_genscript_button = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_genscript_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_genscript_button.setText("Generate Script")
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_genscript_button, 0, 10, 1, 1)

        widgets.STATIC_read_file_button = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_read_file_button.setText("Process")
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_read_file_button, 0, 11, 1, 1)
        

        # SECOND ROW

        widgets.STATIC_vars_search = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_vars_search.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_vars_search.setText("Processed")
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_vars_search, 1, 0, 1, 2)

        widgets.STATIC_vars_qline = QLineEdit(widgets.row_1_1_STATIC)
        widgets.STATIC_vars_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_vars_qline, 1, 2, 1, 8)

        widgets.STATIC_read_vars_button = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_read_vars_button.setText("Open")
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_read_vars_button, 1, 10, 1, 2)


        # SPECIAL BUTTONS

        # widgets.STATIC_instavel = QPushButton(widgets.row_1_2_STATIC)
        # widgets.STATIC_instavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_instavel.setText("Instável")
        # widgets.STATIC_instavel.setMinimumWidth(20)
        # widgets.LG_row_1_2_STATIC.addWidget(widgets.STATIC_instavel, 0, 13, 1, 1)        

        # widgets.STATIC_estavel = QPushButton(widgets.row_1_2_STATIC)
        # widgets.STATIC_estavel.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_estavel.setText("Estável")
        # widgets.STATIC_estavel.setMinimumWidth(130)
        # widgets.LG_row_1_2_STATIC.addWidget(widgets.STATIC_estavel, 0, 14, 1, 1)

        # widgets.STATIC_per_cont = QPushButton(widgets.row_1_2_STATIC)
        # widgets.STATIC_per_cont.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_per_cont.setText("Por Contingência")
        # widgets.LG_row_1_2_STATIC.addWidget(widgets.STATIC_per_cont, 1, 13, 1, 1)

        # widgets.STATIC_per_group = QPushButton(widgets.row_1_2_STATIC)
        # widgets.STATIC_per_group.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_per_group.setText("Por Grupo")
        # widgets.LG_row_1_2_STATIC.addWidget(widgets.STATIC_per_group, 1, 14, 1, 1)

        #botão "Inseguro" p/ filtragem dos pontos de operação
        widgets.STATIC_inseguro = QPushButton(widgets.row_1_2_STATIC)
        widgets.STATIC_inseguro.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_inseguro.setText("Inseguro")
        widgets.STATIC_inseguro.setMinimumHeight(73)
        widgets.LG_row_1_2_STATIC.addWidget(widgets.STATIC_inseguro, 0, 0, 1, 1)


        widgets.verticalLayout_STATIC.addWidget(widgets.row_1_STATIC)


        # ------------------------------------------------------------------------------------------


        widgets.row_2_STATIC = QFrame(widgets.infos_STATIC)
        widgets.row_2_STATIC.setObjectName(u"row_2_STATIC")
        widgets.row_2_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_2_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_2_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_2_STATIC.setMaximumHeight(120)

        widgets.LG_row_2_STATIC = QGridLayout(widgets.row_2_STATIC)
        widgets.LG_row_2_STATIC.setSpacing(5)
        widgets.LG_row_2_STATIC.setObjectName(u"LG_row_2_STATIC")
        widgets.LG_row_2_STATIC.setContentsMargins(0, 0, 1, 1)

        widgets.row_2_1_STATIC = QFrame(widgets.row_2_STATIC)
        widgets.row_2_1_STATIC.setObjectName(u"row_2_1_STATIC")
        widgets.row_2_1_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_2_1_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_2_1_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_2_1_STATIC = QGridLayout(widgets.row_2_1_STATIC)
        widgets.LG_row_2_1_STATIC.setSpacing(5)
        widgets.LG_row_2_1_STATIC.setObjectName(u"LG_row_2_1_STATIC")
        widgets.LG_row_2_1_STATIC.setContentsMargins(0, 0, 1, 1)

        widgets.row_2_2_STATIC = QFrame(widgets.row_2_STATIC)
        widgets.row_2_2_STATIC.setObjectName(u"row_2_2_STATIC")
        widgets.row_2_2_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_2_2_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_2_2_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_2_2_STATIC = QGridLayout(widgets.row_2_2_STATIC)
        widgets.LG_row_2_2_STATIC.setSpacing(5)
        widgets.LG_row_2_2_STATIC.setObjectName(u"LG_row_2_2_STATIC")
        widgets.LG_row_2_2_STATIC.setContentsMargins(0, 0, 1, 1)

        widgets.LG_row_2_STATIC.addWidget(widgets.row_2_1_STATIC, 0, 0, 1, 1)
        widgets.LG_row_2_STATIC.addWidget(widgets.row_2_2_STATIC, 1, 0, 1, 1)



        # THIRD ROW


        widgets.STATIC_x = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_x.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_x.setMinimumHeight(50)
        widgets.LG_row_2_1_STATIC.addWidget(widgets.STATIC_x, 0, 0, 1, 3)

        widgets.STATIC_y = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_y.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_y.setMinimumHeight(50)
        widgets.LG_row_2_1_STATIC.addWidget(widgets.STATIC_y, 0, 3, 1, 3)

        widgets.STATIC_c = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_c.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_c.setMinimumHeight(50)
        widgets.LG_row_2_1_STATIC.addWidget(widgets.STATIC_c, 0, 6, 1, 3)

        # FOURTH ROW

        # widgets.STATIC_plot = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_plot, 1, 0, 1, 3)

        # widgets.STATIC_round = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_round.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_round, 1, 3, 1, 3)


        # widgets.STATIC_stats = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_stats.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_stats, 1, 6, 1, 3)

        # PLOT BUTTON

        widgets.STATIC_plot_button = QPushButton(widgets.row_2_STATIC)
        widgets.STATIC_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_plot_button.setText("Plot")
        # widgets.STATIC_plot_button.setMinimumHeight(50)
        widgets.LG_row_2_1_STATIC.addWidget(widgets.STATIC_plot_button, 0, 9, 1, 4)

        #Tipo de gráfico
        widgets.STATIC_type_button = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_type_button.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_type_button.setMinimumHeight(50)
        widgets.LG_row_2_2_STATIC.addWidget(widgets.STATIC_type_button, 0, 0, 1, 6.5)

        widgets.STATIC_stats = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_stats.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.LG_row_2_2_STATIC.addWidget(widgets.STATIC_stats, 0, 6.5, 1, 6.5)

        # FIFTH ROW

        # widgets.STATIC_combo_variable = ExtendedComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_combo_variable.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_combo_variable, 2, 0, 1, 3)

        # widgets.STATIC_combo_sinal = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_combo_sinal.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_combo_sinal, 2, 3, 1, 3)

        # widgets.STATIC_label_value = QLineEdit(widgets.row_2_STATIC)
        # widgets.STATIC_label_value.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_label_value, 2, 6, 1, 3)

        # widgets.STATIC_button_apply_filter = QPushButton(widgets.row_2_STATIC)
        # widgets.STATIC_button_apply_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_button_apply_filter.setText("Apply Filter")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_button_apply_filter, 2, 9, 1, 2)

        # widgets.STATIC_button_remove_filter = QPushButton(widgets.row_2_STATIC)
        # widgets.STATIC_button_remove_filter.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_button_remove_filter.setText("Remove Filter")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_button_remove_filter, 2, 11, 1, 2)


        widgets.verticalLayout_STATIC.addWidget(widgets.row_2_STATIC)


        # ------------------------------------------------------------------------------------------


        widgets.row_3_STATIC = QFrame(widgets.infos_STATIC)
        widgets.row_3_STATIC.setObjectName(u"row_3_STATIC")
        widgets.row_3_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_3_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_3_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        widgets.row_3_STATIC.setMinimumHeight(500)

        widgets.LG_row_3_STATIC = QGridLayout(widgets.row_3_STATIC)
        widgets.LG_row_3_STATIC.setSpacing(5)
        widgets.LG_row_3_STATIC.setObjectName(u"LG_row_3_STATIC")
        widgets.LG_row_3_STATIC.setContentsMargins(0, 0, 1, 1)



        widgets.STATIC_sc = MplCanvas(self, width=12, height=12, dpi=100)        
        widgets.STATIC_sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        widgets.STATIC_sc.axes.grid(True)

        widgets.toolbar = NavigationToolbar2QT(widgets.STATIC_sc)

        widgets.LG_row_3_STATIC.addWidget(widgets.toolbar   , 0, 0,  1, 10)
        widgets.LG_row_3_STATIC.addWidget(widgets.STATIC_sc, 1, 0, 10, 10)



        widgets.verticalLayout_STATIC.addWidget(widgets.row_3_STATIC)


        # ------------------------------------------------------------------------------------------


        widgets.row_4_STATIC = QFrame(widgets.infos_STATIC)
        widgets.row_4_STATIC.setObjectName(u"row_4_STATIC")
        widgets.row_4_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_4_STATIC.setMaximumHeight(130)

        widgets.LG_row_4_STATIC = QGridLayout(widgets.row_4_STATIC)
        widgets.LG_row_4_STATIC.setSpacing(5)
        widgets.LG_row_4_STATIC.setObjectName(u"LG_row_4_STATIC")
        widgets.LG_row_4_STATIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_1_STATIC = QFrame(widgets.row_4_STATIC)
        widgets.row_4_1_STATIC.setObjectName(u"row_4_1_STATIC")
        widgets.row_4_1_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_1_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_4_1_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_1_STATIC = QGridLayout(widgets.row_4_1_STATIC)
        widgets.LG_row_4_1_STATIC.setSpacing(5)
        widgets.LG_row_4_1_STATIC.setObjectName(u"LG_row_4_1_STATIC")
        widgets.LG_row_4_1_STATIC.setContentsMargins(0, 0, 1, 1)


        widgets.row_4_2_STATIC = QFrame(widgets.row_4_STATIC)
        widgets.row_4_2_STATIC.setObjectName(u"row_4_2_STATIC")
        widgets.row_4_2_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.row_4_2_STATIC.setFrameShadow(QFrame.Raised)
        widgets.row_4_2_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        widgets.LG_row_4_2_STATIC = QGridLayout(widgets.row_4_2_STATIC)
        widgets.LG_row_4_2_STATIC.setSpacing(5)
        widgets.LG_row_4_2_STATIC.setObjectName(u"LG_row_4_2_STATIC")
        widgets.LG_row_4_2_STATIC.setContentsMargins(0, 0, 1, 1)



        widgets.LG_row_4_STATIC.addWidget(widgets.row_4_1_STATIC, 0, 0, 1, 1)
        widgets.LG_row_4_STATIC.addWidget(widgets.row_4_2_STATIC, 0, 1, 1, 1)


        # # SIXTH ROW


        # widgets.STATIC_add_section = QLineEdit(widgets.row_4_1_STATIC)
        # widgets.STATIC_add_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_4_1_STATIC.addWidget(widgets.STATIC_add_section, 0, 0, 1, 4)

        # widgets.STATIC_add_section_button = QPushButton(widgets.row_4_1_STATIC)
        # widgets.STATIC_add_section_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_add_section_button.setText("Add Section")
        # widgets.LG_row_4_1_STATIC.addWidget(widgets.STATIC_add_section_button, 0, 4, 1, 4)

        # widgets.STATIC_sections_ava = QComboBox(widgets.row_4_1_STATIC)
        # widgets.STATIC_sections_ava.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_4_1_STATIC.addWidget(widgets.STATIC_sections_ava, 1, 0, 1, 2)

        # widgets.STATIC_add_plot = QLineEdit(widgets.row_4_1_STATIC)
        # widgets.STATIC_add_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_4_1_STATIC.addWidget(widgets.STATIC_add_plot, 1, 2, 1, 2)

        # widgets.STATIC_add_plot_button = QPushButton(widgets.row_4_1_STATIC)
        # widgets.STATIC_add_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_add_plot_button.setText("Add Page")
        # widgets.LG_row_4_1_STATIC.addWidget(widgets.STATIC_add_plot_button, 1, 4, 1, 4)


        # # SEVENTH ROW


        # widgets.STATIC_select_section = QComboBox(widgets.row_4_2_STATIC)
        # widgets.STATIC_select_section.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_4_2_STATIC.addWidget(widgets.STATIC_select_section, 0, 0, 1, 4)

        # widgets.STATIC_select_plot = QComboBox(widgets.row_4_2_STATIC)
        # widgets.STATIC_select_plot.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_4_2_STATIC.addWidget(widgets.STATIC_select_plot, 0, 4, 1, 4)

        # widgets.STATIC_add_to_json_button = QPushButton(widgets.row_4_2_STATIC)
        # widgets.STATIC_add_to_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_add_to_json_button.setText("Add Plot to Page")
        # widgets.LG_row_4_2_STATIC.addWidget(widgets.STATIC_add_to_json_button, 1, 0, 1, 4)

        # widgets.STATIC_page_to_plot_button = QPushButton(widgets.row_4_2_STATIC)
        # widgets.STATIC_page_to_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_page_to_plot_button.setText("Plot Page")
        # widgets.LG_row_4_2_STATIC.addWidget(widgets.STATIC_page_to_plot_button, 1, 4, 1, 4)

        # widgets.STATIC_save_json_button = QPushButton(widgets.row_4_2_STATIC)
        # widgets.STATIC_save_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_save_json_button.setText("Save")
        # widgets.STATIC_save_json_button.setMinimumHeight(80)
        # widgets.LG_row_4_2_STATIC.addWidget(widgets.STATIC_save_json_button, 0, 8, 2, 1)


        # widgets.verticalLayout_STATIC.addWidget(widgets.row_4_STATIC)


        widgets.mainLayout_STATIC.addWidget(widgets.infos_STATIC)




        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ///                                                                                                                                                ///
        # ///                                                                     DIREITA                                                                    ///
        # ///                                                                                                                                                ///
        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



        # widgets.pdf_STATIC = QFrame(widgets.STATIC)
        # widgets.pdf_STATIC.setObjectName(u"row_1")
        # widgets.pdf_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.pdf_STATIC.setFrameShadow(QFrame.Raised)

        # widgets.verticalLayout_pdf_STATIC = QVBoxLayout(widgets.pdf_STATIC)
        # widgets.verticalLayout_pdf_STATIC.setSpacing(10)
        # widgets.verticalLayout_pdf_STATIC.setObjectName(u"verticalLayout_pdf_STATIC")
        # widgets.verticalLayout_pdf_STATIC.setContentsMargins(10, 10, 10, 10)





        # widgets.row_5_STATIC = QFrame(widgets.pdf_STATIC)
        # widgets.row_5_STATIC.setObjectName(u"row_5_STATIC")
        # widgets.row_5_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_5_STATIC.setFrameShadow(QFrame.Raised)
        # # widgets.row_5_STATIC.setMaximumHeight(110)
        # widgets.row_5_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        

        # widgets.LG_row_5_STATIC = QGridLayout(widgets.row_5_STATIC)
        # widgets.LG_row_5_STATIC.setSpacing(5)
        # widgets.LG_row_5_STATIC.setObjectName(u"LG_row_5_STATIC")
        # widgets.LG_row_5_STATIC.setContentsMargins(0, 0, 1, 1)



        # # FIRST ROW

        # widgets.STATIC_search_json_button = QPushButton(widgets.row_5_STATIC)
        # widgets.STATIC_search_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_search_json_button.setText("Search")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_search_json_button, 0, 0, 1, 2)

        # widgets.STATIC_qline_json_files = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_json_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_json_files, 0, 2, 1, 8)

        # widgets.STATIC_read_json_button = QPushButton(widgets.row_5_STATIC)
        # widgets.STATIC_read_json_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_read_json_button.setText("Open")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_read_json_button, 0, 10, 1, 2)

        # # SECOND ROW

        # widgets.STATIC_label_00 = QLabel(widgets.row_5_STATIC)
        # widgets.STATIC_label_00.setText("File")
        # widgets.STATIC_label_00.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_label_00, 1, 0, 1, 6)

        # widgets.STATIC_qline_00 = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_00.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_00, 2, 0, 1, 6)


        # widgets.STATIC_label_01 = QLabel(widgets.row_5_STATIC)
        # widgets.STATIC_label_01.setText("Version")
        # widgets.STATIC_label_01.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_label_01, 1, 6, 1, 6)

        # widgets.STATIC_qline_01 = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_01.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_01, 2, 6, 1, 6)


        # # THIRD ROW

        # widgets.STATIC_label_10 = QLabel(widgets.row_5_STATIC)
        # widgets.STATIC_label_10.setText("Responsible")
        # widgets.STATIC_label_10.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_label_10, 3, 0, 1, 6)

        # widgets.STATIC_qline_10 = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_10.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_10, 4, 0, 1, 6)


        # widgets.STATIC_label_11 = QLabel(widgets.row_5_STATIC)
        # widgets.STATIC_label_11.setText("Date")
        # widgets.STATIC_label_11.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_label_11, 3, 6, 1, 6)

        # widgets.STATIC_qline_11 = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_11.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_11, 4, 6, 1, 6)

        # # THIRD ROW

        # widgets.STATIC_label_20 = QLabel(widgets.row_5_STATIC)
        # widgets.STATIC_label_20.setText("")
        # widgets.STATIC_label_20.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_label_20, 5, 0, 1, 6)

        # widgets.STATIC_qline_20 = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_20.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_20, 6, 0, 1, 6)


        # widgets.STATIC_label_21 = QLabel(widgets.row_5_STATIC) 
        # widgets.STATIC_label_21.setText("")
        # widgets.STATIC_label_21.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_label_21, 5, 6, 1, 6)

        # widgets.STATIC_qline_21 = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_21.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_21, 6, 6, 1, 6)


        # # THIRD ROW

        # widgets.STATIC_label_30 = QLabel(widgets.row_5_STATIC)
        # widgets.STATIC_label_30.setText("Comment")
        # widgets.STATIC_label_30.setStyleSheet("QFrame {border-width: 0; border-style: transparent;}")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_label_30, 7, 0, 1, 12)

        # widgets.STATIC_qline_30 = QLineEdit(widgets.row_5_STATIC)
        # widgets.STATIC_qline_30.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_5_STATIC.addWidget(widgets.STATIC_qline_30, 8, 0, 1, 12)





        # widgets.STATIC_read_vars_button = QPushButton(widgets.row_1_STATIC)
        # widgets.STATIC_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_read_vars_button.setText("Open")
        # widgets.LG_row_1_STATIC.addWidget(widgets.STATIC_read_vars_button, 1, 10, 1, 2)



        # widgets.verticalLayout_pdf_STATIC.addWidget(widgets.row_5_STATIC)





        

      


        # widgets.d_row_1_STATIC = QFrame(widgets.pdf_STATIC)
        # widgets.d_row_1_STATIC.setObjectName(u"d_row_1_STATIC")
        # widgets.d_row_1_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.d_row_1_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.d_row_1_STATIC.setMaximumHeight(600)
        # # widgets.d_row_1_STATIC.setMaximumSize(QSize(600, 400))

        # widgets.d_LG_row_1_STATIC = QGridLayout(widgets.d_row_1_STATIC)
        # widgets.d_LG_row_1_STATIC.setSpacing(0)
        # widgets.d_LG_row_1_STATIC.setObjectName(u"d_LG_row_1_STATIC")
        # widgets.d_LG_row_1_STATIC.setContentsMargins(0, 0, 1, 1)

        # ## ============================


        # widgets.pdfView_STATIC = QPdfView(widgets.pdf_STATIC)
        # widgets.pdfView_STATIC.setObjectName(u"pdfView_STATIC")

        # widgets.STATIC_document = QPdfDocument(widgets.pdf_STATIC)

        # widgets.pdfView_STATIC.setDocument(widgets.STATIC_document)


        # ## ============================



        # widgets.mainToolBar = QToolBar(widgets.d_row_1_STATIC)
        # widgets.mainToolBar.setObjectName(u"mainToolBar")
        # widgets.mainToolBar.setMovable(False)
        # widgets.mainToolBar.setFloatable(False)


        # # ACTIONS


        # widgets.run_STATIC = QPushButton(widgets.d_row_1_STATIC)
        # widgets.run_STATIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.run_STATIC.setText("Run")

        # widgets.actionZoom_In_STATIC = QPushButton(widgets.d_row_1_STATIC)
        # widgets.actionZoom_In_STATIC.setText('In')
        # widgets.actionZoom_In_STATIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        # widgets.actionZoom_Out_STATIC = QPushButton(widgets.d_row_1_STATIC)
        # widgets.actionZoom_Out_STATIC.setText('Out')
        # widgets.actionZoom_Out_STATIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        # widgets.m_zoomSelector_STATIC = ZoomSelector(widgets.d_row_1_STATIC)
        # widgets.m_zoomSelector_STATIC.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.m_zoomSelector_STATIC.zoom_mode_changed.connect(widgets.pdfView_STATIC.setZoomMode)
        # widgets.m_zoomSelector_STATIC.zoom_factor_changed.connect(widgets.pdfView_STATIC.setZoomFactor)
        # widgets.m_zoomSelector_STATIC.reset()
        # widgets.pdfView_STATIC.zoomFactorChanged.connect(widgets.m_zoomSelector_STATIC.set_zoom_factor)

        # widgets.actionPage_down_STATIC = QPushButton(widgets.d_row_1_STATIC)
        # widgets.actionPage_down_STATIC.setText('-')
        # widgets.actionPage_down_STATIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        # widgets.actionPage_up_STATIC = QPushButton(widgets.d_row_1_STATIC)
        # widgets.actionPage_up_STATIC.setText('+')
        # widgets.actionPage_up_STATIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")

        # widgets.m_pageSelector_STATIC = QSpinBox(widgets.d_row_1_STATIC)
        # widgets.m_pageSelector_STATIC.valueChanged.connect(widgets.page_selected)
        # widgets.m_pageSelector_STATIC.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # nav = widgets.pdfView_STATIC.pageNavigator()
        # nav.currentPageChanged.connect(widgets.m_pageSelector_STATIC.setValue)

    
        # widgets.actionSave_STATIC = QPushButton(widgets.d_row_1_STATIC)
        # widgets.actionSave_STATIC.setText('Save')
        # widgets.actionSave_STATIC.setStyleSheet(u"background-color: rgb(91, 95, 199)")





        # widgets.mainToolBar.addWidget(widgets.run_STATIC)
        # widgets.mainToolBar.addSeparator()
        # widgets.mainToolBar.addWidget(widgets.actionZoom_In_STATIC)
        # widgets.mainToolBar.addSeparator()
        # widgets.mainToolBar.addWidget(widgets.m_zoomSelector_STATIC)
        # widgets.mainToolBar.addSeparator()
        # widgets.mainToolBar.addWidget(widgets.actionZoom_Out_STATIC)
        # widgets.mainToolBar.addSeparator()
        # widgets.mainToolBar.addWidget(widgets.actionPage_down_STATIC)
        # widgets.mainToolBar.addSeparator()
        # widgets.mainToolBar.addWidget(widgets.m_pageSelector_STATIC)
        # widgets.mainToolBar.addSeparator()
        # widgets.mainToolBar.addWidget(widgets.actionPage_up_STATIC)
        # widgets.mainToolBar.addSeparator()
        # widgets.mainToolBar.addWidget(widgets.actionSave_STATIC)




        ## =============


        # widgets.d_LG_row_1_STATIC.addWidget(widgets.mainToolBar, 0, 0, 1, 1)
        # widgets.d_LG_row_1_STATIC.addWidget(widgets.pdfView_STATIC, 1, 0, 1, 1)

        # widgets.verticalLayout_pdf_STATIC.addWidget(widgets.d_row_1_STATIC)
        # widgets.mainLayout_STATIC.addWidget(widgets.pdf_STATIC)
       

        # ADD ALL

        widgets.stackedWidget.addWidget(widgets.STATIC)






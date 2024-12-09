from PySide6.QtCore       import *
from PySide6.QtGui        import *
from PySide6.QtWidgets    import *
from PySide6.QtCharts     import *
from PySide6.QtPdfWidgets import *
from PySide6.QtPdf        import *
from PySide6.QtWebEngineWidgets import QWebEngineView

from Modules.UIWidgets.Help_Widgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

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

        # widgets.mainLayout_STATIC = QHBoxLayout(widgets.STATIC)
        widgets.mainLayout_STATIC = QGridLayout(widgets.STATIC)
        widgets.mainLayout_STATIC.setSpacing(10)
        widgets.mainLayout_STATIC.setObjectName(u"mainLayout_STATIC")
        widgets.mainLayout_STATIC.setContentsMargins(10, 10, 10, 10)
        # widgets.label = QLabel('testando aqui')
        # widgets.mainLayout_STATIC.addWidget(widgets.label, 0, 0, 0, 0)

        # === ESQUERDA

        widgets.infos_STATIC = QFrame(widgets.STATIC)
        widgets.infos_STATIC.setObjectName(u"row_1")
        widgets.infos_STATIC.setFrameShape(QFrame.StyledPanel)
        widgets.infos_STATIC.setFrameShadow(QFrame.Raised)
        widgets.infos_STATIC.setMinimumWidth(1000)

        widgets.verticalLayout_STATIC = QVBoxLayout(widgets.infos_STATIC)
        widgets.verticalLayout_STATIC.setSpacing(10)
        widgets.verticalLayout_STATIC.setObjectName(u"verticalLayout_STATIC")
        widgets.verticalLayout_STATIC.setContentsMargins(10, 10, 10, 10)

        # # === ESQUERDA

        # # Criando a QScrollArea para inserir a área de rolagem
        # widgets.scroll_area_STATIC = QScrollArea(widgets.STATIC)  # A área de rolagem será criada dentro de "widgets.STATIC"
        # widgets.scroll_area_STATIC.setWidgetResizable(True)  # Permite que o conteúdo seja redimensionado dentro da área de rolagem

        # # Definindo a política de rolagem (desativando a rolagem horizontal)
        # widgets.scroll_area_STATIC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Desativa a barra de rolagem horizontal
        # widgets.scroll_area_STATIC.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Exibe a barra de rolagem vertical conforme necessário

        # # Criando o QFrame (que será o conteúdo dentro da área de rolagem)
        # widgets.infos_STATIC = QFrame()
        # widgets.infos_STATIC.setObjectName(u"row_1")
        # widgets.infos_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.infos_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.infos_STATIC.setMinimumWidth(1000)

        # # Adicionando um layout vertical ao QFrame (onde você coloca seus widgets)
        # widgets.verticalLayout_STATIC = QVBoxLayout(widgets.infos_STATIC)
        # widgets.verticalLayout_STATIC.setSpacing(10)
        # widgets.verticalLayout_STATIC.setObjectName(u"verticalLayout_STATIC")
        # widgets.verticalLayout_STATIC.setContentsMargins(10, 10, 10, 10)

        # # Configurando o QFrame como o widget rolável na área de rolagem
        # widgets.scroll_area_STATIC.setWidget(widgets.infos_STATIC)

        # # Agora você pode adicionar a QScrollArea ao layout principal (ou outro layout)
        # # Supondo que você tenha um layout principal chamado "mainLayout"
        # widgets.mainLayout_STATIC.addWidget(widgets.scroll_area_STATIC)

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

        widgets.LG_row_1_STATIC.addWidget(widgets.row_1_1_STATIC, 0, 0, 1, 3)



        # FIRST ROW

        # widgets.STATIC_search_button = QPushButton(widgets.row_1_1_STATIC)
        # widgets.STATIC_search_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_search_button.setText("Search")
        # # widgets.STATIC_search_button.setToolTip('Path related to script generation')  # Defina a mensagem da tooltip
        # widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_search_button, 1, 0, 1, 1)

        # widgets.STATIC_qline_files = QLineEdit(widgets.row_1_1_STATIC)
        # widgets.STATIC_qline_files.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_qline_files.setToolTip('Path related to script generation, OPF simulation and data processing.')  # Defina a mensagem da tooltip
        # widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_qline_files, 0, 2, 1, 7)

        # widgets.STATIC_opf_button = QPushButton(widgets.row_1_1_STATIC)
        # widgets.STATIC_opf_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_opf_button.setText("OPF Simulation")
        # widgets.STATIC_opf_button.setToolTip('Button related to OPF simulation and script generation for Organon.')  # Defina a mensagem da tooltip
        # widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_opf_button, 0, 0, 1, 1)

        # widgets.STATIC_genscript_button = QPushButton(widgets.row_1_1_STATIC)
        # widgets.STATIC_genscript_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_genscript_button.setText("Generate Script")
        # widgets.STATIC_genscript_button.setToolTip('Button related to script generation for Organon. It will use the path beside it.')  # Defina a mensagem da tooltip
        # widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_genscript_button, 0, 10, 1, 1)

        # widgets.STATIC_read_file_button = QPushButton(widgets.row_1_1_STATIC)
        # widgets.STATIC_read_file_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_read_file_button.setText("Process")
        # widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_read_file_button, 0, 11, 1, 1)

        widgets.STATIC_read_file_button2 = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_read_file_button2.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_read_file_button2.setText("Process")
        widgets.STATIC_read_file_button2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_read_file_button2, 0, 0, 2, 1)
        

        # SECOND ROW

        widgets.STATIC_vars_search = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_vars_search.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_vars_search.setText("Processed")
        widgets.STATIC_vars_search.setToolTip('Search for already processed cases.')  # Defina a mensagem da tooltip
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_vars_search, 0, 1, 1, 1)
        

        widgets.STATIC_vars_qline = QLineEdit(widgets.row_1_1_STATIC)
        widgets.STATIC_vars_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.STATIC_vars_qline.setPlaceholderText("Enter the path of the already processed CSV or HTML file.")  # Texto de exemplo
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_vars_qline, 0, 2, 1, 8)

        widgets.STATIC_read_vars_button = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_read_vars_button.setText("Open")
        widgets.STATIC_read_vars_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_read_vars_button, 0, 10, 2, 2)

        # criando uma segunda linha de line edit pra testar o plot do marck
        widgets.STATIC_vars_qline2 = QLineEdit(widgets.row_1_1_STATIC)
        widgets.STATIC_vars_qline2.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.STATIC_vars_qline2.setPlaceholderText("Enter the path of the already processed CSV or HTML file.")  # Texto de exemplo
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_vars_qline2, 1, 2, 1, 8)

        # widgets.STATIC_botao_teste = QPushButton(widgets.row_1_1_STATIC)
        # widgets.STATIC_botao_teste.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_botao_teste.setText("Procurar Marck")
        # widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_botao_teste, 2, 10, 1, 2)

        widgets.STATIC_processed_2 = QPushButton(widgets.row_1_1_STATIC)
        widgets.STATIC_processed_2.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_processed_2.setText("Processed")
        widgets.STATIC_processed_2.setToolTip('Search for already processed cases.')  # Defina a mensagem da tooltip
        widgets.LG_row_1_1_STATIC.addWidget(widgets.STATIC_processed_2, 1, 1, 1, 1)

        widgets.verticalLayout_STATIC.addWidget(widgets.row_1_STATIC)

        # # Testando janela de opções para geração e processamento dos arquivos

        # widgets.row_0_STATIC = QFrame(widgets.infos_STATIC)
        # widgets.row_0_STATIC.setObjectName(u"row_0_STATIC")
        # widgets.row_0_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_0_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_0_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")
        # widgets.row_0_STATIC.setMaximumHeight(200)

        # widgets.LG_row_0_STATIC = QGridLayout(widgets.row_0_STATIC)
        # widgets.LG_row_0_STATIC.setSpacing(5)
        # widgets.LG_row_0_STATIC.setObjectName(u"LG_row_0_STATIC")
        # widgets.LG_row_0_STATIC.setContentsMargins(0, 0, 1, 1)


        # #Norma
        # widgets.STATIC_norm_label = QLabel("Norm:")
        # widgets.STATIC_norm_label.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_norm_label.setToolTip('Select the chosen norm for data processing. If the norm is infinite, the others will be disabled.')  # Defina a mensagem da tooltip
        # widgets.STATIC_norm_combobox = QComboBox()
        # widgets.STATIC_norm_combobox.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_norm_combobox.addItems(["1", "2", "3"])  # Exemplo de normas
        # widgets.STATIC_norm_checkbox = QCheckBox('Infinite Norm?')
        # widgets.STATIC_norm_checkbox.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_norm_checkbox.setMinimumHeight(32)
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_norm_label, 0, 0, 1, 2)
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_norm_combobox, 0, 2, 1, 2)
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_norm_checkbox, 0, 4, 1, 2)


        # # Caso OneCase assinalado (processar apenas um dia/hora específica) - DIA (xx) e HORA (xx-yy)
        # # widgets.STATIC_onecase_label = QLabel("One Case: Day (xx) | Hour (xx-yy)")
        # # widgets.STATIC_onecase_label.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_day_qline = QLineEdit(widgets.row_1_1_STATIC)
        # widgets.STATIC_day_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_day_qline.setToolTip('Enter the specific day in the format xx.')  # Defina a mensagem da tooltip
        # widgets.STATIC_hour_qline = QLineEdit(widgets.row_1_1_STATIC)
        # widgets.STATIC_hour_qline.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_hour_qline.setToolTip('Enter the specific hour in the format xx-xx.')  # Defina a mensagem da tooltip

        # widgets.STATIC_onecase = QCheckBox('One Case?')
        # widgets.STATIC_onecase.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_onecase.setMinimumHeight(32)
        # widgets.STATIC_onecase.setToolTip('Check this option if you want to analyze an individual case. Otherwise, all cases in the path will be considered.')  # Defina a mensagem da tooltip
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onecase, 1, 0, 1, 2)

        # # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onecase_label, 1, 0, 1, 2)
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_day_qline, 1, 2, 1, 2)
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_hour_qline, 1, 4, 1, 2)
        
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onecase_label, 1, 0, 1, 2)
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_day_qline, 1, 2, 1, 2)
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_hour_qline, 1, 4, 1, 2)


        # #Onecase? Desmarcado (All) e Marcado (Apenas um caso)
        # widgets.STATIC_onecase = QCheckBox('One Case?')
        # widgets.STATIC_onecase.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onecase, 2, 0, 1, 3)

        # #OnlyPWF_datagen
        # widgets.STATIC_onlypwf = QCheckBox('Only PWF Datagen')
        # widgets.STATIC_onlypwf.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_onlypwf, 2, 3, 1, 3)

        # #Extract from CSV
        # widgets.STATIC_extract_from_csv = QCheckBox('Extract from CSV')
        # widgets.STATIC_extract_from_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_extract_from_csv, 2, 2, 1, 1)


        # #Bus Data
        # widgets.STATIC_bus_data = QCheckBox('Bus Data')
        # widgets.STATIC_bus_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_bus_data, 2, 3, 1, 1)


        # #Linhas data
        # widgets.STATIC_line_data = QCheckBox('Linha Data')
        # widgets.STATIC_line_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_line_data, 2, 4, 1, 1)

        # #HVDCData
        # widgets.STATIC_hvdc_data = QCheckBox('HVDC Data')
        # widgets.STATIC_hvdc_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_hvdc_data, 2, 5, 1, 1)

        # #ReservaData
        # widgets.STATIC_reserva_data = QCheckBox('Reserva Data')
        # widgets.STATIC_reserva_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_reserva_data, 3, 0, 1, 1)

        # #IntercambiosData
        # widgets.STATIC_intercambio_data = QCheckBox('Intercambios Data')
        # widgets.STATIC_intercambio_data.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_intercambio_data, 3, 1, 1, 1)

        # #ComputeDPI
        # widgets.STATIC_compute_dpi = QCheckBox('Compute DPI')
        # widgets.STATIC_compute_dpi.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_compute_dpi, 3, 2, 1, 1)

        # #linhascsv
        # widgets.STATIC_linhas_csv = QCheckBox('Linhas CSV')
        # widgets.STATIC_linhas_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_linhas_csv, 3, 3, 1, 1)

        # #reservacsv
        # widgets.STATIC_reserva_csv = QCheckBox('Reserva CSV')
        # widgets.STATIC_reserva_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_reserva_csv, 3, 4, 1, 1)

        # #HVDCcsv
        # widgets.STATIC_hvdc_csv = QCheckBox('HVDC CSV')
        # widgets.STATIC_hvdc_csv.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.LG_row_0_STATIC.addWidget(widgets.STATIC_hvdc_csv, 3, 5, 1, 1)

        # widgets.verticalLayout_STATIC.addWidget(widgets.row_0_STATIC)


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

        # widgets.row_2_1_STATIC = QFrame(widgets.row_2_STATIC)
        # widgets.row_2_1_STATIC.setObjectName(u"row_2_1_STATIC")
        # widgets.row_2_1_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_2_1_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_2_1_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        # widgets.LG_row_2_1_STATIC = QGridLayout(widgets.row_2_1_STATIC)
        # widgets.LG_row_2_1_STATIC.setSpacing(5)
        # widgets.LG_row_2_1_STATIC.setObjectName(u"LG_row_2_1_STATIC")
        # widgets.LG_row_2_1_STATIC.setContentsMargins(0, 0, 1, 1)

        # widgets.row_2_2_STATIC = QFrame(widgets.row_2_STATIC)
        # widgets.row_2_2_STATIC.setObjectName(u"row_2_2_STATIC")
        # widgets.row_2_2_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_2_2_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_2_2_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        # widgets.LG_row_2_2_STATIC = QGridLayout(widgets.row_2_2_STATIC)
        # widgets.LG_row_2_2_STATIC.setSpacing(5)
        # widgets.LG_row_2_2_STATIC.setObjectName(u"LG_row_2_2_STATIC")
        # widgets.LG_row_2_2_STATIC.setContentsMargins(0, 0, 1, 1)

        # widgets.LG_row_2_STATIC.addWidget(widgets.row_2_1_STATIC, 0, 0, 1, 1)
        # widgets.LG_row_2_STATIC.addWidget(widgets.row_2_2_STATIC, 1, 0, 1, 1)



        # THIRD ROW

        # Tipo de plot - padrão, sempre aparece
        widgets.STATIC_type_button = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_type_button.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        widgets.STATIC_type_button.setToolTip('Select the plot type.')  # Defina a mensagem da tooltip
        # widgets.STATIC_type_button.setMinimumHeight(50)
        widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_type_button, 0, 0, 1, 1)

        # # visualização padrão
        # widgets.STATIC_x = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_x.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # # widgets.STATIC_x.setMinimumHeight(50)
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_x, 0, 1, 1, 1)

        # # Criando o QLabel para indicar o que a ComboBox faz
        # widgets.STATIC_voltage_label = QLabel("Selecione a tensão:", widgets.row_2_STATIC)
        # widgets.STATIC_voltage_label.setStyleSheet("background-color: rgb(218, 218, 233)")

        # # Adicionando o QLabel ao layout
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_voltage_label, 2, 0, 1, 1)  # Ajuste a posição conforme necessário

        widgets.STATIC_y = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_y.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_y.setMinimumHeight(50)
        widgets.STATIC_y.setToolTip('Choose the information related to the Y-axis.')  # Defina a mensagem da tooltip
        widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_y, 0, 1, 1, 1)

        widgets.STATIC_c = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_c.setStyleSheet(u"background-color: rgb(218, 218, 233)") 
        # widgets.STATIC_c.setMinimumHeight(50)
        widgets.STATIC_c.setToolTip('Choose the categorical information.')  # Defina a mensagem da tooltip
        widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_c, 0, 2, 1, 1)


        #visualização caso arquivo = df_ger ou df_nf
        widgets.STATIC_group_reg = QCheckBox('Group by Region?')
        widgets.STATIC_group_reg.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_group_reg.setMinimumHeight(50)
        widgets.STATIC_group_reg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        widgets.STATIC_group_reg.setToolTip('Available only for boxplots. If true, the software will create a boxplot grouped by region; otherwise, it will be grouped by types of generation.')  # Defina a mensagem da tooltip
        widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_group_reg, 1, 0, 1, 1)

        # # combobox de escolha de região (para os casos dos índices)
        # widgets.STATIC_region = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_region.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # # widgets.STATIC_region.setMinimumHeight(50)
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_region, 2, 1, 1, 1)

         # combobox de escolha das tensões (para os casos dos índices)
        widgets.STATIC_voltage_ind = QComboBox(widgets.row_2_STATIC)
        widgets.STATIC_voltage_ind.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.STATIC_voltage_ind.setMinimumHeight(50)
        widgets.STATIC_voltage_ind.setToolTip('Categorical information for filtering.')  # Defina a mensagem da tooltip
        widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_voltage_ind, 1, 2, 1, 1)

        #checkbox all same plot (para os casos dos índices)
        widgets.STATIC_all_sameplot = QCheckBox('Plot all in same plot?')
        widgets.STATIC_all_sameplot.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_all_sameplot.setMinimumHeight(50)
        widgets.STATIC_all_sameplot.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        widgets.STATIC_all_sameplot.setToolTip('Available only for index plots. If true, the grouping will be done for all categorical variables; otherwise, it will be based on the selected categories.')  # Defina a mensagem da tooltip
        widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_all_sameplot, 1, 1, 1, 1)

        # PLOT BUTTON

        widgets.STATIC_plot_button = QPushButton(widgets.row_2_STATIC)
        widgets.STATIC_plot_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        widgets.STATIC_plot_button.setText("Plot")
        # widgets.STATIC_plot_button.setMinimumHeight(50)
        widgets.STATIC_plot_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_plot_button, 0, 3, 3, 1)

        # # clear plot button
        # widgets.STATIC_clear_button = QPushButton(widgets.row_2_STATIC)
        # widgets.STATIC_clear_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.STATIC_clear_button.setText("Clear Plot")
        # # widgets.STATIC_clear_button.setMinimumHeight(50)
        # widgets.STATIC_clear_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_clear_button, 0, 4, 3, 1)

        # widgets.botao_html = QPushButton(widgets.row_2_STATIC)
        # widgets.botao_html.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # widgets.botao_html.setText("HTML")
        # widgets.botao_html.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # widgets.LG_row_2_STATIC.addWidget(widgets.botao_html, 0, 4, 3, 1)


        # #Tipo de gráfico
        # widgets.STATIC_type_button = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_type_button.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # # widgets.STATIC_type_button.setMinimumHeight(50)
        # widgets.LG_row_2_2_STATIC.addWidget(widgets.STATIC_type_button, 0, 0, 1, 4)

        # widgets.STATIC_stats = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_stats.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_stats, 1, 0, 1, 3)

        # widgets.STATIC_choose_reg = QComboBox(widgets.row_2_STATIC)
        # widgets.STATIC_choose_reg.setStyleSheet(u"background-color: rgb(218, 218, 233)")
        # widgets.LG_row_2_STATIC.addWidget(widgets.STATIC_choose_reg, 1, 3, 1, 3)
        

    


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


        # widgets.row_4_STATIC = QFrame(widgets.infos_STATIC)
        # widgets.row_4_STATIC.setObjectName(u"row_4_STATIC")
        # widgets.row_4_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_4_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_4_STATIC.setMaximumHeight(130)

        # widgets.LG_row_4_STATIC = QGridLayout(widgets.row_4_STATIC)
        # widgets.LG_row_4_STATIC.setSpacing(5)
        # widgets.LG_row_4_STATIC.setObjectName(u"LG_row_4_STATIC")
        # widgets.LG_row_4_STATIC.setContentsMargins(0, 0, 1, 1)


        # widgets.row_4_1_STATIC = QFrame(widgets.row_4_STATIC)
        # widgets.row_4_1_STATIC.setObjectName(u"row_4_1_STATIC")
        # widgets.row_4_1_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_4_1_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_4_1_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        # widgets.LG_row_4_1_STATIC = QGridLayout(widgets.row_4_1_STATIC)
        # widgets.LG_row_4_1_STATIC.setSpacing(5)
        # widgets.LG_row_4_1_STATIC.setObjectName(u"LG_row_4_1_STATIC")
        # widgets.LG_row_4_1_STATIC.setContentsMargins(0, 0, 1, 1)


        # widgets.row_4_2_STATIC = QFrame(widgets.row_4_STATIC)
        # widgets.row_4_2_STATIC.setObjectName(u"row_4_2_STATIC")
        # widgets.row_4_2_STATIC.setFrameShape(QFrame.StyledPanel)
        # widgets.row_4_2_STATIC.setFrameShadow(QFrame.Raised)
        # widgets.row_4_2_STATIC.setStyleSheet("QFrame {border-width: 1; border-style: solid; border-color: rgb(100, 100, 100); padding: 5px}")

        # widgets.LG_row_4_2_STATIC = QGridLayout(widgets.row_4_2_STATIC)
        # widgets.LG_row_4_2_STATIC.setSpacing(5)
        # widgets.LG_row_4_2_STATIC.setObjectName(u"LG_row_4_2_STATIC")
        # widgets.LG_row_4_2_STATIC.setContentsMargins(0, 0, 1, 1)



        # widgets.LG_row_4_STATIC.addWidget(widgets.row_4_1_STATIC, 0, 0, 1, 1)
        # widgets.LG_row_4_STATIC.addWidget(widgets.row_4_2_STATIC, 0, 1, 1, 1)


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





        # # widgets.STATIC_read_vars_button = QPushButton(widgets.row_1_STATIC)
        # # widgets.STATIC_read_vars_button.setStyleSheet(u"background-color: rgb(91, 95, 199)")
        # # widgets.STATIC_read_vars_button.setText("Open")
        # # widgets.LG_row_1_STATIC.addWidget(widgets.STATIC_read_vars_button, 1, 10, 1, 2)



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




        # # =============


        # widgets.d_LG_row_1_STATIC.addWidget(widgets.mainToolBar, 0, 0, 1, 1)
        # widgets.d_LG_row_1_STATIC.addWidget(widgets.pdfView_STATIC, 1, 0, 1, 1)

        # widgets.verticalLayout_pdf_STATIC.addWidget(widgets.d_row_1_STATIC)
        # widgets.mainLayout_STATIC.addWidget(widgets.pdf_STATIC)
       

        # ADD ALL

        widgets.stackedWidget.addWidget(widgets.STATIC)






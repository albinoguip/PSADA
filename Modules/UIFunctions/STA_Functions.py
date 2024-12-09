from main import *
from PySide6.QtCore    import *
from PySide6.QtGui     import *
from PySide6.QtWidgets import *

from Modules.UIWidgets.custom_grips import *
from Modules.UIWidgets.Help_Widgets import *

from Modules.UIFunctions.Plotter       import *
from Modules.UIFunctions.PDF_Generator import *

import shutil, json

from win32com.shell import shell, shellcon 

 

from PowerSystemsAnalysis import *
from StaticAnalysis import *

import os, glob, shutil, json

from tqdm import tqdm
import pandas as pd
import time

import numpy as np
import seaborn as sns
import folium
from folium.vector_layers import CircleMarker
from sklearn.preprocessing import MinMaxScaler
from branca.colormap import StepColormap
import webbrowser
from matplotlib.colorbar import Colorbar

# import json
# import os




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///----------------------------------------------------------------- HELP FUNCTION ----------------------------------------------------------------///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////





def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




GLOBAL_STATE = False

class OPF_PopupJanela(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OPF Simulation")
        self.setGeometry(500, 500, 500, 400)

        layout = QGridLayout()
        self.label = QLabel("Path Search:")
        self.label.setAlignment(Qt.AlignCenter)  # Centraliza o texto no QLabel
        layout.addWidget(self.label, 0, 0, 1, 1)

        # path searching button
        self.button_search = QPushButton("Search")
        layout.addWidget(self.button_search, 0, 1, 1, 1)
        self.button_search.clicked.connect(self.opf_path_searching)  # Conecta o botão a um método

        # QLineEdit (campo de texto)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Path")  # Texto de exemplo
        layout.addWidget(self.line_edit, 1, 0, 1, 2)

        # self.cpy_pwf_chkbox = QCheckBox("Copy PWF")
        # # self.onecase_label.setAlignment(Qt.AlignCenter)  # Centraliza o texto no QLabel
        # self.cpy_pwf_chkbox.setStyleSheet("border: 2px solid white;")  # Adiciona uma borda branca
        # # self.cpy_pwf_chkbox.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # layout.addWidget(self.cpy_pwf_chkbox, 2, 0, 1, 1)

        # self.ger_dsa_file = QCheckBox("Generate DSA File")
        # # self.onecase_label.setAlignment(Qt.AlignCenter)  # Centraliza o texto no QLabel
        # self.ger_dsa_file.setStyleSheet("border: 2px solid white;")  # Adiciona uma borda branca
        # # self.ger_dsa_file.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # layout.addWidget(self.ger_dsa_file, 2, 0, 1, 2)
        
        # Adicionando um botão na janela popup
        self.botao_opf_process = QPushButton("OPF Process")
        layout.addWidget(self.botao_opf_process, 2, 0, 1, 1)
        self.botao_opf_process.clicked.connect(self.opf_process_run)

        self.botao_hvdc_changer = QPushButton("HVDC Changer")
        layout.addWidget(self.botao_hvdc_changer, 2, 1, 1, 1)
        self.botao_hvdc_changer.clicked.connect(self.opf_hvdc_changer)
        

        self.setLayout(layout)

    # def on_botao_clicked(self):
    #     selected_item = self.combo.currentText()  # Obtém o item selecionado da QComboBox
    #     print(f"Você selecionou: {selected_item}")
    #     self.label.setText(f"Você atualizou o item selecionado: {selected_item}")  # Atualiza o texto do Qself.label
    
    def opf_path_searching(self):

        self.file_data_match = str(QFileDialog.getExistingDirectory(self, "Select Directory")) + '/'
        self.line_edit.setText(self.file_data_match)

    def opf_process_run(self):

        path = self.line_edit.text()
        paths = [path]

        for path_folder in paths:
            path_folderFrom = 'StaticAnalysis/RECURSOS/OPF_files/'  #Ese path deve conter as ultimas modificações dos arquivos necesarios para rodar o OPF no Organon (Ex: file.prm, file.def, file.opf, ...)
            nomefolder = ''
            OPF = Opf_Simulation(path_folderFrom, nomefolder, path_folder, GerDSAFile=True) # Para gerar as pastas
            OPF.OPF_Process()

    def opf_hvdc_changer(self):

        path = self.line_edit.text()
        paths = [path]

        for path_folder in paths:
            path_folderFrom = 'StaticAnalysis/RECURSOS/OPF_files/'  #Ese path deve conter as ultimas modificações dos arquivos necesarios para rodar o OPF no Organon (Ex: file.prm, file.def, file.opf, ...)
            nomefolder = ''
            OPF = Opf_Simulation(path_folderFrom, nomefolder, path_folder, GerDSAFile=True) # Para gerar as pastas
            OPF.HVDCchanger()



class Process_Parameters(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process Parameters")
        self.setGeometry(500, 500, 500, 400)

        layout1 = QGridLayout()
        self.norm_label = QLabel("Norm:")
        self.norm_label.setAlignment(Qt.AlignCenter)  # Centraliza o texto no QLabel
        self.norm_label.setStyleSheet("border: 2px solid white;")
        layout1.addWidget(self.norm_label, 0, 0, 2, 1)

        self.infinite_norm_checkbox = QCheckBox('Infinite norm?')
        layout1.addWidget(self.infinite_norm_checkbox, 0, 1, 1, 1)

        self.norm_combobox = QComboBox()
        self.norm_combobox.addItems(["1", "2", "3"])
        layout1.addWidget(self.norm_combobox, 1, 1, 1, 1)

        self.onecase_label = QCheckBox("One Case?")
        # self.onecase_label.setAlignment(Qt.AlignCenter)  # Centraliza o texto no QLabel
        self.onecase_label.setStyleSheet("border: 2px solid white;")  # Adiciona uma borda branca
        self.onecase_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        layout1.addWidget(self.onecase_label, 2, 0, 2, 1)
        self.onecase_label.stateChanged.connect(self.STATIC_checkbox_FUNCTION)

        self.onecase_day = QLineEdit()
        self.onecase_day.setPlaceholderText("Set the specific day (xx).")  # Texto de exemplo
        layout1.addWidget(self.onecase_day, 2, 1, 1, 1)

        self.onecase_hour = QLineEdit()
        self.onecase_hour.setPlaceholderText("Set the specific hour (xx-xx).")  # Texto de exemplo
        layout1.addWidget(self.onecase_hour, 3, 1, 1, 1)

        self.search_path_button = QPushButton("Search")
        layout1.addWidget(self.search_path_button, 4, 0, 1, 2)
        self.search_path_button.clicked.connect(self.processing_path_searching)  # Conecta o botão a um método

        self.search_path_line = QLineEdit()
        self.search_path_line.setPlaceholderText("Insert the path for data processing.")  # Texto de exemplo
        layout1.addWidget(self.search_path_line, 5, 0, 1, 2)

        # Adicionando um botão na janela popup
        self.process_button = QPushButton("Process")
        layout1.addWidget(self.process_button, 6, 1, 1, 1)
        self.process_button.clicked.connect(self.process_button_action)  # Conecta o botão a um método

        # Adicionando um botão na janela popup
        self.genscript_button = QPushButton("Generate Script")
        layout1.addWidget(self.genscript_button, 6, 0, 1, 1)
        self.genscript_button.clicked.connect(self.genscript_function)  # Conecta o botão a um método

        # Cria a barra de progresso
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)  # Define o intervalo da barra
        layout1.addWidget(self.progress_bar)  # Adiciona ao layout

        self.setLayout(layout1)

    def STATIC_checkbox_FUNCTION(self):
        
        
        options = {
                            'Norm': '',          # Write None for using infinite norm in voltage analysis
                            # 'OneCase': self.ui.STATIC_onecase_combobox.currentText(),       # (1) for All cases or (2) for Just One Case analysis
                            'OneCase': self.onecase_label.isChecked(),       # (1) for All cases or (2) for Just One Case analysis
                            'DayOneCase': self.onecase_day.text(),
                            'HourOneCase': self.onecase_hour.text(),
                            'SavePath': self.search_path_line.text(),
        # ---------------------------------------------------
                            'generatescript' : False,  # Put TRUE just for generate the script for simulation and saving the flows in Organon
                            'OPFsimulation': False,
                            'ReadPWF_files':True,
                            'OnlyPWF_datagen': False,   # Put TRUE just for generate the data for Interconnection and Line Flow Analysis
                            # 'extract_fromcsv' :self.ui.STATIC_extract_from_csv.isChecked(),   # Put TRUE just in the first simulation, once the ProcessedDataBase.csv is generated it is not necessary
                            'extract_fromcsv' :False,   # Put TRUE just in the first simulation, once the ProcessedDataBase.csv is generated it is not necessary
                            'savedata': True,            # To save the data of the electric variables in the folders
                            # 'busdata' : self.ui.STATIC_bus_data.isChecked(),           # Let like TRUE
                            'busdata' : True,           # Let like TRUE
        # ---------------------------------------------------
                            'ConvergenceData' : True,   # To analyze just the converged cases   
                            # 'LinhasData': self.ui.STATIC_line_data.isChecked(),
                            # 'HVDCData': self.ui.STATIC_hvdc_data.isChecked(),
                            # 'ReservaData': self.ui.STATIC_reserva_data.isChecked(), 
                            # 'IntercambiosData': self.ui.STATIC_intercambio_data.isChecked(),
                            # 'ComputeDPI': self.ui.STATIC_compute_dpi.isChecked(),
                            'LinhasData': True,
                            'HVDCData': True,
                            'ReservaData': True, 
                            'IntercambiosData': True,
                            'ComputeDPI': True,
                            'resumoIndice': True,
        # ---------------------------------------------------
                            # 'linhascsv': self.ui.STATIC_linhas_csv.isChecked(),          # Put TRUE once is generated the LinhasInfo file
                            # 'reservacsv': self.ui.STATIC_reserva_csv.isChecked(),         # Put TRUE once is generated the ReserveInfo file
                            # 'HVDCcsv': self.ui.STATIC_hvdc_csv.isChecked(),          # Put TRUE once is generated the HVDCinfo file
                            'linhascsv': False,          # Put TRUE once is generated the LinhasInfo file
                            'reservacsv': False,         # Put TRUE once is generated the ReserveInfo file
                            'HVDCcsv': False,          # Put TRUE once is generated the HVDCinfo file
        # ---------------------------------------------------
                            # 'PlotGeralPotencia': True,
                            'MapasPlots': True,
                            # 'Plot_Tensao_Geral': True,
                            # 'plotDPI': True,
                            # 'Plot_Boxplot_DPI': True,
                            # 'PlotIntercambios': True
                            'PlotGeralPotencia': False,
                            # 'MapasPlots': False,
                            'Plot_Tensao_Geral': False,
                            'plotDPI': False,
                            'Plot_Boxplot_DPI': False,
                            'PlotIntercambios': False
                        }
        
        enabled_onecase = self.onecase_label.isChecked()
        self.onecase_day.setEnabled(enabled_onecase)
        self.onecase_hour.setEnabled(enabled_onecase)

        enabled_norm = self.infinite_norm_checkbox.isChecked()
        self.norm_combobox.setEnabled(not enabled_norm)
        
        #filtro onecase
        if options['OneCase']:
            print('True, ele quer apenas um caso')
            options['OneCase'] = 2
        else:
            print('False, todos os casos')
            options['OneCase'] = 1
        
        #filtro norma
        if self.infinite_norm_checkbox.isChecked():
            print('Norma é infinita')
            options['Norm'] = None
        else:
            print('Norma não é infinita')
            options['Norm'] = int(self.norm_combobox.currentText())


        print(options)

        return options
    
    
    def processing_path_searching(self):

        self.file_data_match = str(QFileDialog.getExistingDirectory(self, "Select Directory")) + '/'
        self.search_path_line.setText(self.file_data_match)

    def process_button_action(self):

        start_time = time.time()

        Options_Readprocess = self.STATIC_checkbox_FUNCTION()
        print(Options_Readprocess)

        print('DEU CERTO, ver abaixo')
        print(Options_Readprocess)
        path_folder = self.search_path_line.text()

        # Verifica se o caminho está vazio
        if not path_folder:
            QMessageBox.warning(self, "Erro", "Por favor, insira um caminho válido.")
            return

        path_folders = [Options_Readprocess['SavePath']]

        try:
            total_steps = 7  # Total de etapas a serem processadas
            for i, path_folder in enumerate(path_folders):
                cenarios = Analyze_Save_Info.AnalyzeStaticCases(path=path_folder, Options=Options_Readprocess)
                
                cenarios.extraction_process()
                self.update_progress((i + 1) * 100 / total_steps)

                cenarios.LinhaAnalise()
                self.update_progress((i + 2) * 100 / total_steps)

                cenarios.ReservaAnalise()
                self.update_progress((i + 3) * 100 / total_steps)

                cenarios.ActiveReactivePower()
                self.update_progress((i + 4) * 100 / total_steps)

                cenarios.Plot_Tensao_Geral()
                self.update_progress((i + 5) * 100 / total_steps)

                cenarios.MapasPlots()
                self.update_progress((i + 6) * 100 / total_steps)

                cenarios.ComputeDPI()
                self.update_progress((i + 7) * 100 / total_steps)

                cenarios.save_csv()

            QMessageBox.information(self, "Sucesso", "Processamento concluído.")
            self.progress_bar.setValue(100)  # Define a barra como completa
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {str(e)}")

        end_time = time.time()
        execution_time = end_time - start_time
        print("Tempo de execução:", execution_time, "segundos")

    def update_progress(self, value):
        self.progress_bar.setValue(value)  # Atualiza o valor da barra de progresso
        QApplication.processEvents()  # Permite que a interface gráfica atualize

        # try:
        #     for path_folder in path_folders:

        #         cenarios = Analyze_Save_Info.AnalyzeStaticCases(path=path_folder, Options = Options_Readprocess)
        #         cenarios.extraction_process()
        #         cenarios.LinhaAnalise()
        #         cenarios.ReservaAnalise()
        #         cenarios.ActiveReactivePower()
        #         cenarios.Plot_Tensao_Geral()
        #         cenarios.MapasPlots()
        #         cenarios.ComputeDPI()
        #         cenarios.save_csv()
        #     QMessageBox.information(self, "Sucesso", "Processamento concluído.")
        # except Exception as e:
        #     # Captura e exibe qualquer erro que ocorra durante a geração do script
        #     QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {str(e)}")

        # end_time = time.time()
        # execution_time = end_time - start_time
        # print("Tiempo de ejecución:", execution_time, "segundos")

    def genscript_function(self):
        path_folder = self.search_path_line.text()
        
        # Verifica se o caminho está vazio
        if not path_folder:
            QMessageBox.warning(self, "Erro", "Por favor, insira um caminho válido.")
            return

        path_folders = [path_folder]

        try:
            for path_teste in path_folders:
                Read_Process_Cases.ReadScenarios.generate_script(self, path=path_teste)
            
            QMessageBox.information(self, "Sucesso", "Script gerado com sucesso!")
        except Exception as e:
            # Captura e exibe qualquer erro que ocorra durante a geração do script
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {str(e)}")





class STA_Functions(MainWindow):

    def __init__(self, ui):

        # self.last_directory = '\home'
        
        pass   


    # def STATIC_search_button_FUNCTION(self): 

    #     self.file_data_match = str(QFileDialog.getExistingDirectory(self, "Select Directory")) + '/'

    #     self.ui.STATIC_qline_files.setText(self.file_data_match)



    # def STATIC_checkbox_FUNCTION(self):
        
        
    #     options = {
    #                         'Norm': '',          # Write None for using infinite norm in voltage analysis
    #                         # 'OneCase': self.ui.STATIC_onecase_combobox.currentText(),       # (1) for All cases or (2) for Just One Case analysis
    #                         'OneCase': self.ui.STATIC_onecase.isChecked(),       # (1) for All cases or (2) for Just One Case analysis
    #                         'DayOneCase': self.ui.STATIC_day_qline.text(),
    #                         'HourOneCase': self.ui.STATIC_hour_qline.text(),
    #                         'SavePath': self.ui.STATIC_qline_files.text(),
    #     # ---------------------------------------------------
    #                         'generatescript' : False,  # Put TRUE just for generate the script for simulation and saving the flows in Organon
    #                         'OPFsimulation': False,
    #                         'ReadPWF_files':True,
    #                         'OnlyPWF_datagen': False,   # Put TRUE just for generate the data for Interconnection and Line Flow Analysis
    #                         # 'extract_fromcsv' :self.ui.STATIC_extract_from_csv.isChecked(),   # Put TRUE just in the first simulation, once the ProcessedDataBase.csv is generated it is not necessary
    #                         'extract_fromcsv' :False,   # Put TRUE just in the first simulation, once the ProcessedDataBase.csv is generated it is not necessary
    #                         'savedata': True,            # To save the data of the electric variables in the folders
    #                         # 'busdata' : self.ui.STATIC_bus_data.isChecked(),           # Let like TRUE
    #                         'busdata' : True,           # Let like TRUE
    #     # ---------------------------------------------------
    #                         'ConvergenceData' : True,   # To analyze just the converged cases   
    #                         # 'LinhasData': self.ui.STATIC_line_data.isChecked(),
    #                         # 'HVDCData': self.ui.STATIC_hvdc_data.isChecked(),
    #                         # 'ReservaData': self.ui.STATIC_reserva_data.isChecked(), 
    #                         # 'IntercambiosData': self.ui.STATIC_intercambio_data.isChecked(),
    #                         # 'ComputeDPI': self.ui.STATIC_compute_dpi.isChecked(),
    #                         'LinhasData': True,
    #                         'HVDCData': True,
    #                         'ReservaData': True, 
    #                         'IntercambiosData': True,
    #                         'ComputeDPI': True,
    #                         'resumoIndice': True,
    #     # ---------------------------------------------------
    #                         # 'linhascsv': self.ui.STATIC_linhas_csv.isChecked(),          # Put TRUE once is generated the LinhasInfo file
    #                         # 'reservacsv': self.ui.STATIC_reserva_csv.isChecked(),         # Put TRUE once is generated the ReserveInfo file
    #                         # 'HVDCcsv': self.ui.STATIC_hvdc_csv.isChecked(),          # Put TRUE once is generated the HVDCinfo file
    #                         'linhascsv': False,          # Put TRUE once is generated the LinhasInfo file
    #                         'reservacsv': False,         # Put TRUE once is generated the ReserveInfo file
    #                         'HVDCcsv': False,          # Put TRUE once is generated the HVDCinfo file
    #     # ---------------------------------------------------
    #                         # 'PlotGeralPotencia': True,
    #                         'MapasPlots': True,
    #                         # 'Plot_Tensao_Geral': True,
    #                         # 'plotDPI': True,
    #                         # 'Plot_Boxplot_DPI': True,
    #                         # 'PlotIntercambios': True
    #                         'PlotGeralPotencia': False,
    #                         # 'MapasPlots': False,
    #                         'Plot_Tensao_Geral': False,
    #                         'plotDPI': False,
    #                         'Plot_Boxplot_DPI': False,
    #                         'PlotIntercambios': False
    #                     }
        
    #     enabled_onecase = self.ui.STATIC_onecase.isChecked()
    #     self.ui.STATIC_day_qline.setEnabled(enabled_onecase)
    #     self.ui.STATIC_hour_qline.setEnabled(enabled_onecase)

    #     enabled_norm = self.ui.STATIC_norm_checkbox.isChecked()
    #     self.ui.STATIC_norm_combobox.setEnabled(not enabled_norm)
        
    #     #filtro onecase
    #     if options['OneCase']:
    #         print('True, ele quer apenas um caso')
    #         options['OneCase'] = 2
    #     else:
    #         print('False, todos os casos')
    #         options['OneCase'] = 1
        
    #     #filtro norma
    #     if self.ui.STATIC_norm_checkbox.isChecked():
    #         print('Norma é infinita')
    #         options['Norm'] = None
    #     else:
    #         print('Norma não é infinita')
    #         options['Norm'] = int(self.ui.STATIC_norm_combobox.currentText())


    #     print(options)

    #     return options
  
        

    # def STATIC_genscript_button_FUNCTION(self): 

    #     path_folder = self.ui.STATIC_qline_files.text()
        
    #     path_folders = [path_folder]

    #     for path_teste in path_folders:

    #         Read_Process_Cases.ReadScenarios.generate_script(self, path=path_teste)

    #     # print("Tiempo de ejecución:", execution_time, "segundos")

    
    # def STATIC_process_button_FUNCTION(self): 

    #     start_time = time.time()

    #     Options_Readprocess = STA_Functions.STATIC_checkbox_FUNCTION(self=self)
        
    #     print('DEU CERTO, ver abaixo')
    #     print(Options_Readprocess)

    #     path_folders = [Options_Readprocess['SavePath']]

    #     for path_folder in path_folders:

    #         cenarios = Analyze_Save_Info.AnalyzeStaticCases(path=path_folder, Options = Options_Readprocess)
    #         cenarios.extraction_process()
    #         cenarios.LinhaAnalise()
    #         cenarios.ReservaAnalise()
    #         cenarios.ActiveReactivePower()
    #         cenarios.Plot_Tensao_Geral()
    #         cenarios.MapasPlots()
    #         cenarios.ComputeDPI()
    #         cenarios.save_csv()

    #     end_time = time.time()
    #     execution_time = end_time - start_time
    #     print("Tiempo de ejecución:", execution_time, "segundos")


    
    def STATIC_vars_search_FUNCTION(self): 


        # self.file_vars, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Excel (*.csv);;All files(*.*)")
        if self.ui.STATIC_vars_qline.text() == '':
            self.file_vars, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Excel (*.csv);;HTML (*.html);;All files(*.*)")
        # self.file_vars    = self.file_vars[0]

        else:
            last_directory = self.ui.STATIC_vars_qline.text()
            self.file_vars, _ = QFileDialog.getOpenFileNames(self, "Open File", last_directory, "Excel (*.csv);;HTML (*.html);;All files(*.*)")
        
        self.file_vars = self.file_vars[0]
        self.ui.STATIC_vars_qline.setText(self.file_vars)
        # self.ui.STATIC_vars_qline.setText(self.file_vars)

    def procura_linha2(self): 

        # self.file_vars, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Excel (*.csv);;All files(*.*)")
        if self.ui.STATIC_vars_qline2.text() == '':
            self.file_vars2, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Excel (*.csv);;HTML (*.html);;All files(*.*)")
        # self.file_vars2    = self.file_vars2[0]

        else:
            last_directory = self.ui.STATIC_vars_qline2.text()
            self.file_vars2, _ = QFileDialog.getOpenFileNames(self, "Open File", last_directory, "Excel (*.csv);;HTML (*.html);;All files(*.*)")

        self.file_vars2 = self.file_vars2[0]
        self.ui.STATIC_vars_qline2.setText(self.file_vars2)

       
    # def procurar_marck(self):

    #     # leitura dos dois arquivos
    #     self.file_vars1 = self.ui.STATIC_vars_qline.text()
    #     self.file_vars2 = self.ui.STATIC_vars_qline2.text()
    #     select_data1 = self.file_vars1.split('/')[-1].replace('.csv', '')
    #     select_data2 = self.file_vars2.split('/')[-1].replace('.csv', '')

    #     if 'DF_Intercambios' in select_data1 and 'DF_HVDC' in select_data2:

    #         # concatenação dos dois arquivos
    #         # df_pwf16 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_Intercambios.csv').drop('key', axis=1)
    #         df_pwf16 = pd.read_csv(self.file_vars1).drop('key', axis=1)
    #         df_pwf16.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']
    #         # # df_pwf25 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_HVDC.csv').drop('key', axis=1)
    #         df_pwf25 = pd.read_csv(self.file_vars2).drop('key', axis=1)
    #         df_pwf25_cols = df_pwf25.columns.tolist()
    #         df_pwf25_cols = df_pwf25_cols[-1:] + df_pwf25_cols[:-1]
    #         df_pwf25 = df_pwf25[df_pwf25_cols]
    #         df_pwf25.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']

    #         df_pwf = pd.concat([df_pwf16, df_pwf25], axis=0).reset_index().drop('index', axis=1)

    #         plotter = CreatePlots(self.ui)
    #         # plotter.persistency_curve(dataset=df_pwf, 
    #         #                         col='Q(MVAr)',
    #         #                         ui=self.ui, 
    #         #                         #   path=path, 
    #         #                         ax_fontsize=13)
    #         # plotter.box_plots(dataset=df_pwf, 
    #         #                   col='P(MW)', 
    #         #                   ui=self.ui,
    #         #                   split_flows=False,
    #         #                 #   path=path,
    #         #                   ax_fontsize=11
    #         #                   )
    #         # plotter.violin_plots(dataset=df_pwf, 
    #         #                      col='P(MW)', 
    #         #                      ui=self.ui,
    #         #                      split_flows=False,
    #         #                     #  path=path,
    #         #                      ax_fontsize=11,
    #         #                      )
    #         # plotter.create_heatmap(dataset=df_pwf, 
    #         #                        col='P(MW)',
    #         #                        ui=self.ui,
    #         #                     #    path=path, 
    #         #                        ax_fontsize=11)
    #         # plotter.flow_profiles(dataset=df_pwf, 
    #         #                       col='P(MW)', 
    #         #                       ui=self.ui,
    #         #                       path=path)
    #         plotter.create_contourplot(dataset=df_pwf, 
    #                                    col='P(MW)', 
    #                                    ui=self.ui,
    #                                 #    path=path, 
    #                                    ax_fontsize=11)
        
    #     elif 'DF_Intercambios' in select_data2 and 'DF_HVDC' in select_data1:

    #         # concatenação dos dois arquivos
    #         # df_pwf16 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_Intercambios.csv').drop('key', axis=1)
    #         df_pwf16 = pd.read_csv(self.file_vars2).drop('key', axis=1)
    #         df_pwf16.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']
    #         # # df_pwf25 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_HVDC.csv').drop('key', axis=1)
    #         df_pwf25 = pd.read_csv(self.file_vars1).drop('key', axis=1)
    #         df_pwf25_cols = df_pwf25.columns.tolist()
    #         df_pwf25_cols = df_pwf25_cols[-1:] + df_pwf25_cols[:-1]
    #         df_pwf25 = df_pwf25[df_pwf25_cols]
    #         df_pwf25.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']

    #         df_pwf = pd.concat([df_pwf16, df_pwf25], axis=0).reset_index().drop('index', axis=1)

    #         plotter = CreatePlots(self.ui)
    #         # plotter.persistency_curve(dataset=df_pwf, 
    #         #                         col='Q(MVAr)',
    #         #                         ui=self.ui, 
    #         #                         #   path=path, 
    #         #                         ax_fontsize=13)
    #         # plotter.box_plots(dataset=df_pwf, 
    #         #                   col='P(MW)', 
    #         #                   ui=self.ui,
    #         #                   split_flows=False,
    #         #                 #   path=path,
    #         #                   ax_fontsize=11
    #         #                   )
    #         # plotter.violin_plots(dataset=df_pwf, 
    #         #                      col='P(MW)', 
    #         #                      ui=self.ui,
    #         #                      split_flows=False,
    #         #                     #  path=path,
    #         #                      ax_fontsize=11,
    #         #                      )
            # plotter.create_heatmap(dataset=df_pwf, 
            #                        col='P(MW)',
            #                        ui=self.ui,
            #                     #    path=path, 
            #                        ax_fontsize=11)
    #         # plotter.flow_profiles(dataset=df_pwf, 
    #         #                       col='P(MW)', 
    #         #                       ui=self.ui,
    #         #                       path=path)
    #         plotter.create_contourplot(dataset=df_pwf, 
    #                                    col='P(MW)', 
    #                                    ui=self.ui,
    #                                 #    path=path, 
    #                                    ax_fontsize=11)

    #     else:
    #         pass

       

 

    # def STATIC_dynamic_ui_plot(self):
    #     # self.ui.LG_row_1_1_STATIC.removeWidget(self.ui.STATIC_search_button)
    #     self.ui.STATIC_search_button.deleteLater()

    #     self.ui.STATIC_botaoteste = QPushButton(self.ui.row_1_1_STATIC)
    #     self.ui.STATIC_botaoteste.setStyleSheet(u"background-color: rgb(91, 95, 199)")
    #     self.ui.STATIC_botaoteste.setText("Novinho")
    #     # self.ui..STATIC_botaoteste.setToolTip('Path related to script generation')  # Defina a mensagem da tooltip
    #     self.ui.LG_row_1_1_STATIC.addWidget(self.ui.STATIC_botaoteste, 0, 0, 1, 2)

    #     # self.ui.LG_row_1_1_STATIC.update()


    # def teste_html(self):

    #     # Cria o componente QWebEngineView
    #     # self.browser = QWebEngineView()

    #     # Carrega o conteúdo HTML no QWebEngineView
    #     html_file_path = self.ui.STATIC_vars_qline.text()
    #     # Abre o arquivo HTML no navegador padrão
    #     file_url = os.path.abspath(html_file_path)
    #     webbrowser.open(f'file://{file_url}')           
    #     # file_url = QUrl.fromLocalFile(os.path.abspath(html_file_path))
    #     # self.browser.setUrl(file_url)
    #     # self.browser.setHtml(html_content)
        

    #     # self.browser.show()



    def STATIC_read_vars_button_FUNCTION(self): 

        self.ui.STATIC_type_button.clear()
        self.ui.STATIC_y.clear()
        self.ui.STATIC_c.clear()

        file_vars = self.ui.STATIC_vars_qline.text()
        file_vars2 = self.ui.STATIC_vars_qline2.text()

        if file_vars2 == '':

            if not file_vars.endswith('.html'):

                # self.ui.row_2_STATIC.show()

                try:

                    select_data = self.file_vars.split('/')[-1].replace('.csv', '')
                    # select_data2 = self.file_vars2.split('/')[-1].replace('.csv', '')

                    self.dataframe = pd.read_csv(file_vars)
                    # self.dataframe2 = pd.read_csv(file_vars)
                except Exception as e:
                    QMessageBox.warning(self, "Erro", "Por favor, insira um arquivo com formato válido.")
                    return

                aux = False

                if "Df_ger" in select_data or "Df_nt" in select_data:
                    
                    # excluindo widgets desnecessários
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_group_reg.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.hide()
                    self.ui.STATIC_c.hide()
                    self.ui.STATIC_all_sameplot.hide()
                    self.ui.STATIC_voltage_ind.hide()

                    # reconfigurando a caixa de opções de plot
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_group_reg, 0, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)


                    # self.ui.STATIC_voltage_ind.clear()
                    self.ui.STATIC_type_button.addItems(['Boxplot'])
                    # self.ui.STATIC_y.setEnabled(aux)
                    # self.ui.STATIC_c.setEnabled(aux)
                    # self.ui.STATIC_group_reg.setEnabled(not aux)
                    # self.ui.STATIC_all_sameplot.setEnabled(aux)
                    # self.ui.STATIC_all_sameplot.setChecked(aux)
                    # self.ui.STATIC_voltage_ind.setEnabled(aux)

                elif 'Df_PQ_DPI_S1' in select_data or 'Df_PV_DPI_S1' in select_data:

                    # escondendo widgets desnecessários
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.show()
                    self.ui.STATIC_all_sameplot.show()
                    self.ui.STATIC_voltage_ind.show()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 2, 1)
                    self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 1, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 3, 2, 1)

                    self.ui.STATIC_type_button.addItems(['Line', 'Persistence Curve'])
                    # self.ui.STATIC_y.setEnabled(not aux)
                    # self.ui.STATIC_c.setEnabled(not aux)
                    # self.ui.STATIC_group_reg.setChecked(aux)
                    # self.ui.STATIC_group_reg.setEnabled(aux)
                    # self.ui.STATIC_all_sameplot.setEnabled(not aux)
                    # self.ui.STATIC_voltage_ind.setEnabled(not aux)

                    # armazenando as informações do df
                    self.y_var = self.dataframe[['CSI_INF', 'CSI_SUP']]
                    self.c_var = self.dataframe['REG'].unique()

                    self.ui.STATIC_y.addItems(self.y_var)
                    self.ui.STATIC_c.addItems(self.c_var)


                elif 'Df_DPI_S2' in select_data:

                    # escondendo widgets desnecessários
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.show()
                    self.ui.STATIC_all_sameplot.show()
                    self.ui.STATIC_voltage_ind.show()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 2, 1)
                    self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 1, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 3, 2, 1)

                    self.ui.STATIC_type_button.addItems(['Line', 'Persistence Curve'])
                    # self.ui.STATIC_y.setEnabled(not aux)
                    # self.ui.STATIC_c.setEnabled(not aux)
                    # self.ui.STATIC_group_reg.setChecked(aux)
                    # self.ui.STATIC_group_reg.setEnabled(aux)
                    # self.ui.STATIC_all_sameplot.setEnabled(not aux)
                    # self.ui.STATIC_voltage_ind.setEnabled(not aux)

                    self.y_var = self.dataframe[['OV DPI', 'UV DPI', 'OV condition', 'UV condition']]
                    # self.c_var = self.dataframe['level_0'].unique()
                    # print(self.c_var)

                    self.ui.STATIC_y.addItems(self.y_var)
                    self.ui.STATIC_c.addItems(['DPI_PQ', 'DPI_PV'])

                elif 'Df_DPI_S3' in select_data or 'Df_DPI_S4' in select_data:

                    # escondendo widgets desnecessários
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.hide()
                    self.ui.STATIC_all_sameplot.hide()
                    self.ui.STATIC_voltage_ind.hide()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 1, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                    self.ui.STATIC_voltage_ind.clear()
                    self.ui.STATIC_type_button.addItems(['Line', 'Persistence Curve'])
                    # self.ui.STATIC_y.setEnabled(not aux)
                    # self.ui.STATIC_c.setEnabled(aux)
                    # self.ui.STATIC_group_reg.setChecked(aux)
                    # self.ui.STATIC_group_reg.setEnabled(aux)
                    # self.ui.STATIC_all_sameplot.setEnabled(aux)
                    # self.ui.STATIC_voltage_ind.setEnabled(aux)

                    self.y_var = self.dataframe[['DPI_PO', 'DPI_PO_final']] if 'Df_DPI_S4' in select_data else self.dataframe[['PV_lower', 'PV_upper', 'PQ_lower', 'PQ_upper']]
                    print(self.y_var)
                    # self.c_var = self.dataframe['level_0'].unique()
                    # print(self.c_var)

                    self.ui.STATIC_y.addItems(self.y_var)
                    # self.ui.STATIC_c.addItems(['DPI_PQ', 'DPI_PV'])
                
                elif 'DF_POT_Reg' in select_data or 'Df_Reserva_REG_MW' in select_data:

                    # escondendo widgets desnecessários
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.hide()
                    self.ui.STATIC_all_sameplot.show()
                    self.ui.STATIC_voltage_ind.show()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 0, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 1, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 2, 1)

                    self.ui.STATIC_type_button.addItems(['Line', 'Persistence Curve'])
                    # self.ui.STATIC_y.setEnabled(not aux)
                    # self.ui.STATIC_c.setEnabled(aux)
                    # self.ui.STATIC_group_reg.setChecked(aux)
                    # self.ui.STATIC_group_reg.setEnabled(aux)
                    # self.ui.STATIC_all_sameplot.setEnabled(not aux)
                    # self.ui.STATIC_voltage_ind.setEnabled(not aux)

                    # self.y_var = self.dataframe.columns
                    # self.y_var = self.dataframe[['PG_MW', 'QG_MVAR', 'PL_MW', 'QL_MVAR', 'Shunt_Ind', 'Shunt_Cap', 'SHUNT_INST_IND', 'SHUNT_INST_CAP', 'ReservaIND', 'ReservaCAP', 'PG_UHE', 'PG_UTE', 'PG_EOL', 'PG_SOL', 'PG_BIO', 'PG_Dist', 'ReservaINDshunt', 'ReservaCAPshunt']] if 'DF_POT_Reg' in select_data else self.dataframe.columns.strip()
                    # self.y_var = self.dataframe[['PG_MW', 'QG_MVAR', 'PL_MW', 'QL_MVAR', 'Shunt_Ind', 'Shunt_Cap', 'SHUNT_INST_IND', 'SHUNT_INST_CAP', 'ReservaIND', 'ReservaCAP', 'PG_UHE', 'PG_UTE', 'PG_EOL', 'PG_SOL', 'PG_BIO', 'PG_Dist', 'ReservaINDshunt', 'ReservaCAPshunt']] if 'DF_POT_Reg' in select_data else [col.strip() for col in self.dataframe.columns]

                    self.y_var = (self.dataframe[['PG_MW', 'QG_MVAR', 'PL_MW', 'QL_MVAR', 'Shunt_Ind', 'Shunt_Cap', 'SHUNT_INST_IND', 'SHUNT_INST_CAP', 'ReservaIND', 'ReservaCAP', 'PG_UHE', 'PG_UTE', 'PG_EOL', 'PG_SOL', 'PG_BIO', 'PG_Dist', 'ReservaINDshunt', 'ReservaCAPshunt']] 
                    if 'DF_POT_Reg' in select_data 
                    else self.dataframe[[col for col in self.dataframe.columns if col.strip() == 'Reserve']])


                    self.ui.STATIC_y.addItems(self.y_var)

                elif 'Df_MW-MVAR_PO' in select_data or 'Df_Reserva_PO_MW' in select_data:

                    # escondendo widgets desnecessários
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.hide()
                    self.ui.STATIC_all_sameplot.hide()
                    self.ui.STATIC_voltage_ind.hide()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 1, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                    self.ui.STATIC_voltage_ind.clear()
                    self.ui.STATIC_type_button.addItems(['Line', 'Persistence Curve'])
                    # self.ui.STATIC_y.setEnabled(not aux)
                    # self.ui.STATIC_c.setEnabled(aux)
                    # self.ui.STATIC_group_reg.setChecked(aux)
                    # self.ui.STATIC_group_reg.setEnabled(aux)
                    # self.ui.STATIC_all_sameplot.setEnabled(aux)
                    # self.ui.STATIC_all_sameplot.setChecked(aux)
                    # self.ui.STATIC_voltage_ind.setEnabled(aux)

                    self.y_var = (self.dataframe[['PG_MW', 'PL_MW', 'PG_EOL', 'PG_SOL', 'QG_MVAR', 'PG_FERV']]
                    if 'Df_MW-MVAR_PO' in select_data
                    else self.dataframe[[col for col in self.dataframe.columns if col.strip() == 'Reserve']])
                    # self.c_var = self.dataframe.columns

                    self.ui.STATIC_y.addItems(self.y_var)
                    # self.ui.STATIC_c.addItems(self.c_var)

                else:
                    QMessageBox.warning(self, "Erro", "Por favor, insira um arquivo válido.")
                    return
            
            else:

                # self.ui.row_2_STATIC.hide()

                self.ui.STATIC_type_button.hide()
                self.ui.STATIC_plot_button.hide()
                self.ui.STATIC_y.hide()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                file_url = os.path.abspath(file_vars)
                webbrowser.open(f'file://{file_url}') 

        
        else:
            
            try:

                select_data1 = self.file_vars.split('/')[-1].replace('.csv', '')
                select_data2 = self.file_vars2.split('/')[-1].replace('.csv', '')

                self.dataframe = pd.read_csv(file_vars)
                self.dataframe = pd.read_csv(file_vars2)
            except Exception as e:
                QMessageBox.warning(self, "Erro", "Por favor, insira um arquivo com formato válido.")
                return
            select_data1 = self.file_vars.split('/')[-1].replace('.csv', '')
            select_data2 = self.file_vars2.split('/')[-1].replace('.csv', '')

            if 'DF_Intercambios' in select_data1 and 'DF_HVDC' in select_data2:

                # escondendo widgets desnecessários
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.show()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 1, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                self.ui.STATIC_voltage_ind.clear()
                self.ui.STATIC_type_button.addItems(['Persistence Curve', 'Boxplot', 'Violin Plot', 'Heatmap'])
                # self.ui.STATIC_y.addItems(['P(MW)', 'Q(MVAr)'])


            elif 'DF_Intercambios' in select_data2 and 'DF_HVDC' in select_data1:

                # escondendo widgets desnecessários
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.show()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 1, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                self.ui.STATIC_voltage_ind.clear()
                self.ui.STATIC_type_button.addItems(['Persistence Curve', 'Boxplot', 'Violin Plot', 'Heatmap'])
                # self.ui.STATIC_y.addItems(['P(MW)', 'Q(MVAr)'])

            elif 'Df_Linhas' in select_data1 and 'PWF_NC' in select_data2:

                # escondendo widgets desnecessários
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.hide()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 0, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 1, 1, 1)

                self.ui.STATIC_voltage_ind.clear()
                self.ui.STATIC_type_button.addItems(['Maior L1', 'Heatmap Região', 'Boxplot por Região', 'Média Geral por Região', 'Histograma por Tensão', 'Histograma por Região', 'Por Região e por Tensão', 'Heatmap Tensão', 'Maior Carregamento'])
                # self.reg_unico = pd.read_csv(self.file_vars)
                # reg_filt_unico = self.reg_unico['REG'].unique()
                # self.ui.STATIC_c.addItems(reg_filt_unico)
                

            elif 'Df_Linhas' in select_data2 and 'PWF_NC' in select_data1:

                # escondendo widgets desnecessários
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.hide()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 0, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 1, 1, 1)

                self.ui.STATIC_voltage_ind.clear()
                self.ui.STATIC_type_button.addItems(['Maior L1', 'Heatmap Região', 'Boxplot por Região', 'Média Geral por Região', 'Histograma por Tensão', 'Histograma por Região', 'Por Região e por Tensão', 'Heatmap Tensão', 'Maior Carregamento'])
                # self.reg_unico = pd.read_csv(self.file_vars)
                # reg_filt_unico = self.reg_unico['REG'].unique()
                # self.ui.STATIC_c.addItems(reg_filt_unico)
            
            else:

                QMessageBox.warning(self, "Erro", "Por favor, insira um arquivo válido.")
                return

    

    def aux_func_df_linhas(self):

        texto_atual = self.ui.STATIC_type_button.currentText()
        read_file = self.ui.STATIC_vars_qline.text()
        select_data = read_file.split('/')[-1].replace('.csv', '')

        if texto_atual not in ['Maior L1', 'Heatmap Região', 'Boxplot por Região', 'Média Geral por Região', 'Histograma por Tensão', 'Histograma por Região', 'Por Região e por Tensão', 'Heatmap Tensão', 'Maior Carregamento']:
            
            if texto_atual not in ['Persistence Curve', 'Boxplot', 'Violin Plot', 'Heatmap']:
                pass
            else:

                if texto_atual == 'Persistence Curve' and (select_data == 'DF_Intercambios' or select_data == 'DF_HVDC'):

                    self.ui.STATIC_c.clear()
                    self.ui.STATIC_y.clear()

                    # mostrando campos de interesse
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.show()
                    self.ui.STATIC_all_sameplot.hide()
                    self.ui.STATIC_voltage_ind.hide()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 3, 1, 1)

                    self.ui.STATIC_c.addItems(['NE -> T', 'NE -> SE', 'N -> S', 'SUL -> SECO', 'NE -> N', 'RSUL -> T', 'FOZ -> IBIUNA', 'PVEL -> ARARQ', 'CPVBTB -> PVEL', 'XINGU -> SE'])
                    self.ui.STATIC_y.addItems(['P(MW)', 'Q(MVAr)'])

                if texto_atual == 'Boxplot' and (select_data == 'DF_Intercambios' or select_data == 'DF_HVDC'):

                    self.ui.STATIC_c.clear()
                    self.ui.STATIC_y.clear()

                    # mostrando campos de interesse
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.hide()
                    self.ui.STATIC_all_sameplot.hide()
                    self.ui.STATIC_voltage_ind.hide()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                    self.ui.STATIC_y.addItems(['P(MW)', 'Q(MVAr)'])

                if texto_atual == 'Violin Plot':

                    self.ui.STATIC_c.clear()
                    self.ui.STATIC_y.clear()

                    # mostrando campos de interesse
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.hide()
                    self.ui.STATIC_all_sameplot.hide()
                    self.ui.STATIC_voltage_ind.hide()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                    self.ui.STATIC_y.addItems(['P(MW)', 'Q(MVAr)'])

                if texto_atual == 'Heatmap':

                    self.ui.STATIC_c.clear()
                    self.ui.STATIC_y.clear()

                    # mostrando campos de interesse
                    self.ui.STATIC_type_button.show()
                    self.ui.STATIC_plot_button.show()
                    self.ui.STATIC_y.show()
                    self.ui.STATIC_c.show()
                    self.ui.STATIC_all_sameplot.hide()
                    self.ui.STATIC_voltage_ind.hide()
                    self.ui.STATIC_group_reg.hide()

                    # reconfigurar os posicionamentos
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                    # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                    # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                    self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 3, 1, 1)

                    self.ui.STATIC_c.addItems(['NE -> T', 'NE -> SE', 'N -> S', 'SUL -> SECO', 'NE -> N', 'RSUL -> T', 'FOZ -> IBIUNA', 'PVEL -> ARARQ', 'CPVBTB -> PVEL', 'XINGU -> SE'])
                    self.ui.STATIC_y.addItems(['P(MW)', 'Q(MVAr)'])



        else:

            if texto_atual == 'Maior L1':
                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.show()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                self.reg_unico = pd.read_csv(read_file)
                reg_filt_unico = self.reg_unico['REG'].unique()
                self.ui.STATIC_y.addItems(reg_filt_unico)

            elif texto_atual == 'Heatmap Região':
                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.show()
                self.ui.STATIC_c.show()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 2, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 3, 1, 1)

                self.reg_unico = pd.read_csv(read_file)
                reg_filt_unico = self.reg_unico['REG'].unique()
                self.ui.STATIC_y.addItems(reg_filt_unico)
                self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])

            elif texto_atual == 'Boxplot por Região':
                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.hide()
                self.ui.STATIC_c.show()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                # self.reg_unico = pd.read_csv(read_file)
                # reg_filt_unico = self.reg_unico['REG'].unique()
                # self.ui.STATIC_y.addItems(reg_filt_unico)
                self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])

            elif texto_atual == 'Média Geral por Região':
                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.show()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                self.reg_unico = pd.read_csv(read_file)
                reg_filt_unico = self.reg_unico['REG'].unique()
                self.ui.STATIC_y.addItems(reg_filt_unico)
                # self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])

            elif texto_atual == 'Histograma por Tensão':

                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.hide()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.show()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 2, 1, 1)

                # self.reg_unico = pd.read_csv(read_file)
                # reg_filt_unico = self.reg_unico['REG'].unique()
                # self.ui.STATIC_y.addItems(reg_filt_unico)
                # self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])
            
            
            elif texto_atual == 'Histograma por Região':

                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.hide()
                self.ui.STATIC_c.show()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.show()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 3, 1, 1)

                self.reg_unico = pd.read_csv(read_file)
                reg_filt_unico = self.reg_unico['REG'].unique()
                self.ui.STATIC_c.addItems(reg_filt_unico)
                # self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])

            elif texto_atual == 'Por Região e por Tensão':

                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.show()
                self.ui.STATIC_c.show()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.show()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 3, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 4, 1, 1)

                self.reg_unico = pd.read_csv(read_file)
                reg_filt_unico = self.reg_unico['REG'].unique()
                self.ui.STATIC_y.addItems(reg_filt_unico)
                self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])
            
            elif texto_atual == 'Heatmap Tensão':

                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.show()
                self.ui.STATIC_c.show()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.show()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 3, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 4, 1, 1)

                self.reg_unico = pd.read_csv(read_file)
                reg_filt_unico = self.reg_unico['REG'].unique()
                self.ui.STATIC_y.addItems(reg_filt_unico)
                self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])

            elif texto_atual == 'Maior Carregamento':

                self.ui.STATIC_c.clear()
                self.ui.STATIC_y.clear()

                # mostrando campos de interesse
                self.ui.STATIC_type_button.show()
                self.ui.STATIC_plot_button.show()
                self.ui.STATIC_y.hide()
                self.ui.STATIC_c.hide()
                self.ui.STATIC_all_sameplot.hide()
                self.ui.STATIC_voltage_ind.hide()
                self.ui.STATIC_group_reg.hide()

                # reconfigurar os posicionamentos
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_type_button, 0, 0, 1, 1)
                # self.ui.STATIC_type_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_y, 0, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_c, 0, 3, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_all_sameplot, 1, 1, 1, 1)
                # self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_voltage_ind, 0, 2, 1, 1)
                self.ui.LG_row_2_STATIC.addWidget(self.ui.STATIC_plot_button, 0, 1, 1, 1)

                # self.reg_unico = pd.read_csv(read_file)
                # reg_filt_unico = self.reg_unico['REG'].unique()
                # self.ui.STATIC_y.addItems(reg_filt_unico)
                # self.ui.STATIC_c.addItems(['% L1', 'MVAr Losses'])
            



    def update_voltage_indice(self):

        self.caminho = self.ui.STATIC_vars_qline.text()
        self.caminho2 = self.ui.STATIC_vars_qline2.text()

        if not self.caminho.endswith('.html'):

            if self.caminho2 == '':

                dado = self.caminho.split('/')[-1].replace('.csv', '')
                self.data = pd.read_csv(self.ui.STATIC_vars_qline.text())
                # Obter a região selecionada na primeira combo box
                selected_region = self.ui.STATIC_c.currentText()

                if 'Df_PQ_DPI_S1' in dado:

                    # Limpar a segunda combo box
                    self.ui.STATIC_voltage_ind.clear()

                    # Verificar se uma região foi selecionada
                    if selected_region:
                        # Filtrar o DataFrame para a região selecionada
                        filtered_data = self.data[self.data['REG'] == selected_region]

                        # Obter os valores únicos de tensão (VBASEKV) para a região selecionada
                        unique_voltages = filtered_data['VBASEKV'].unique()
                        # Converter os valores para inteiros, se apropriado
                        unique_voltages = [int(v) if v.is_integer() else v for v in unique_voltages]

                        print(unique_voltages)  # Para verificar os valores

                        # Criar um modelo para a combobox que suporta checkboxes
                        model = QStandardItemModel(self.ui.STATIC_voltage_ind)

                        # # Adicionar uma opção 'All' no final, caso o usuário deseje selecionar todas
                        # item_none = QStandardItem('')
                        # item_none.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                        # item_none.setData(Qt.Unchecked, Qt.CheckStateRole)
                        # model.appendRow(item_none)

                        for voltage in unique_voltages:
                            item = QStandardItem(str(voltage))  # Converter tensão para string para exibir corretamente
                            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # Permitir checkbox
                            item.setData(Qt.Unchecked, Qt.CheckStateRole)  # Inicialmente desmarcada
                            model.appendRow(item)

                        # Adicionar uma opção 'All' para selecionar todos os valores de tensão
                        # item_all = QStandardItem('All')
                        # item_all.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                        # item_all.setData(Qt.Unchecked, Qt.CheckStateRole)
                        # model.appendRow(item_all)

                        # Definir o modelo atualizado na combo box de tensão
                        self.ui.STATIC_voltage_ind.setModel(model)

                    else:
                        # Caso nenhuma região seja selecionada, limpar a combo box de tensão
                        self.ui.STATIC_voltage_ind.clear()

                elif 'Df_PV_DPI_S1' in dado:
                    # Verificar se uma região foi selecionada
                    if selected_region:
                        # Filtrar o DataFrame para a região selecionada
                        filtered_data = self.data[self.data['REG'] == selected_region]

                        # Obter os valores únicos de tensão (VBASEKV) para a região selecionada
                        unique_voltages = filtered_data['Gen_Type'].unique()
                        # Converter os valores para inteiros, se apropriado
                        # unique_voltages = [int(v) if v.is_integer() else v for v in unique_voltages]

                        print(unique_voltages)  # Para verificar os valores

                        # Criar um modelo para a combobox que suporta checkboxes
                        model = QStandardItemModel(self.ui.STATIC_voltage_ind)

                        # # Adicionar uma opção 'All' no final, caso o usuário deseje selecionar todas
                        # item_none = QStandardItem('')
                        # item_none.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                        # item_none.setData(Qt.Unchecked, Qt.CheckStateRole)
                        # model.appendRow(item_none)

                        for voltage in unique_voltages:
                            item = QStandardItem(str(voltage))  # Converter tensão para string para exibir corretamente
                            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # Permitir checkbox
                            item.setData(Qt.Unchecked, Qt.CheckStateRole)  # Inicialmente desmarcada
                            model.appendRow(item)

                        # Adicionar uma opção 'All' para selecionar todos os valores de tensão
                        # item_all = QStandardItem('All')
                        # item_all.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                        # item_all.setData(Qt.Unchecked, Qt.CheckStateRole)
                        # model.appendRow(item_all)

                        # Definir o modelo atualizado na combo box de tensão
                        self.ui.STATIC_voltage_ind.setModel(model)

                    else:
                        # Caso nenhuma região seja selecionada, limpar a combo box de tensão
                        self.ui.STATIC_voltage_ind.clear()

                elif 'Df_DPI_S2' in dado:
                    # Limpar a segunda combo box
                    self.ui.STATIC_voltage_ind.clear()

                    if selected_region:
                        # Filtrar o DataFrame para a região selecionada
                        filtered_data = self.data[self.data['level_0'] == selected_region]

                        # Obter os valores únicos de tensão (VBASEKV) para a região selecionada
                        unique_voltages = filtered_data['REG'].unique()
                        # Converter os valores para inteiros, se apropriado
                        # unique_voltages = [int(v) if v.is_integer() else v for v in unique_voltages]

                        print(unique_voltages)  # Para verificar os valores

                        # Criar um modelo para a combobox que suporta checkboxes
                        model = QStandardItemModel(self.ui.STATIC_voltage_ind)

                        for voltage in unique_voltages:
                            item = QStandardItem(str(voltage))  # Converter tensão para string para exibir corretamente
                            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # Permitir checkbox
                            item.setData(Qt.Unchecked, Qt.CheckStateRole)  # Inicialmente desmarcada
                            model.appendRow(item)

                        # Definir o modelo atualizado na combo box de tensão
                        self.ui.STATIC_voltage_ind.setModel(model)

                    else:
                        # Caso nenhuma região seja selecionada, limpar a combo box de tensão
                        self.ui.STATIC_voltage_ind.clear()
                        # pass


                else:
                        # Caso nenhuma região seja selecionada, limpar a combo box de tensão
                        self.ui.STATIC_voltage_ind.clear()
            

        else:
            pass

    
    
    def voltage_indice_path2(self):
        self.caminho1 = self.ui.STATIC_vars_qline.text()
        self.caminho2 = self.ui.STATIC_vars_qline2.text()

        if self.caminho2 != '':

            dado = self.caminho1.split('/')[-1].replace('.csv', '')
            dado2 = self.caminho2.split('/')[-1].replace('.csv', '')

            if 'Df_Linhas' in dado and 'PWF_NC' in dado2:
                self.data2 = pd.read_csv(self.ui.STATIC_vars_qline.text())
                # Limpar a segunda combo box
                self.ui.STATIC_voltage_ind.clear()

                unique_voltages = self.data2['VBASEKV'].unique()
                print(unique_voltages)

                # Criar um modelo para a combobox que suporta checkboxes
                model = QStandardItemModel(self.ui.STATIC_voltage_ind)

                for voltage in unique_voltages:
                    item = QStandardItem(str(voltage))  # Converter tensão para string para exibir corretamente
                    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # Permitir checkbox
                    item.setData(Qt.Unchecked, Qt.CheckStateRole)  # Inicialmente desmarcada
                    model.appendRow(item)

                # Definir o modelo atualizado na combo box de tensão
                self.ui.STATIC_voltage_ind.setModel(model)
                
            elif 'Df_Linhas' in dado2 and 'PWF_NC' in dado:
                self.data2 = pd.read_csv(self.ui.STATIC_vars_qline2.text())

                # Limpar a segunda combo box
                self.ui.STATIC_voltage_ind.clear()

                unique_voltages = self.data2['VBASEKV'].unique()
                print(unique_voltages)

                # Criar um modelo para a combobox que suporta checkboxes
                model = QStandardItemModel(self.ui.STATIC_voltage_ind)

                for voltage in unique_voltages:
                    item = QStandardItem(str(voltage))  # Converter tensão para string para exibir corretamente
                    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # Permitir checkbox
                    item.setData(Qt.Unchecked, Qt.CheckStateRole)  # Inicialmente desmarcada
                    model.appendRow(item)

                # Definir o modelo atualizado na combo box de tensão
                self.ui.STATIC_voltage_ind.setModel(model)

            else:
                pass

        else:
            pass


    
    def opf_window(self):

        self.popup_window = OPF_PopupJanela()  # Cria uma instância da janela popup
        self.popup_window.exec_()  # Exibe a janela como modal

    def teste_process(self):
        self.janelinha = Process_Parameters()
        self.janelinha.exec_()



    def update_region_type(self):

        self.caminho = self.ui.STATIC_vars_qline.text()

        if not self.caminho.endswith('.html'):

            dado = self.caminho.split('/')[-1].replace('.csv', '')
            self.data = pd.read_csv(self.ui.STATIC_vars_qline.text())

            if 'DF_POT_Reg' in dado or 'Df_Reserva_REG_MW' in dado:
                # Limpar a segunda combo box
                self.ui.STATIC_voltage_ind.clear()

                # Filtrar o DataFrame para a região selecionada
                # filtered_data = self.data[self.data['level_0'] == selected_region]

                # Obter os valores únicos de tensão (VBASEKV) para a região selecionada
                unique_voltages = self.data['REG'].unique()
                # Converter os valores para inteiros, se apropriado
                # unique_voltages = [int(v) if v.is_integer() else v for v in unique_voltages]

                print('achei as regioes unicas', unique_voltages)  # Para verificar os valores

                # Criar um modelo para a combobox que suporta checkboxes
                model = QStandardItemModel(self.ui.STATIC_voltage_ind)

                # # Adicionar uma opção 'All' no final, caso o usuário deseje selecionar todas
                # item_none = QStandardItem('')
                # item_none.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                # item_none.setData(Qt.Unchecked, Qt.CheckStateRole)
                # model.appendRow(item_none)

                for voltage in unique_voltages:
                    item = QStandardItem(str(voltage))  # Converter tensão para string para exibir corretamente
                    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # Permitir checkbox
                    item.setData(Qt.Unchecked, Qt.CheckStateRole)  # Inicialmente desmarcada
                    model.appendRow(item)

                # Adicionar uma opção 'All' para selecionar todos os valores de tensão
                # item_all = QStandardItem('All')
                # item_all.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                # item_all.setData(Qt.Unchecked, Qt.CheckStateRole)
                # model.appendRow(item_all)

                # Definir o modelo atualizado na combo box de tensão
                self.ui.STATIC_voltage_ind.setModel(model)
            else:
                pass

        else:
            pass


    def STATIC_plot_button_FUNCTION(self):

        path1 = self.ui.STATIC_vars_qline.text()
        path2 = self.ui.STATIC_vars_qline2.text()

        if path2 == '':

            # if plot_type == 'Line':

            # # Acesse o modelo do QComboBox
            # model = self.ui.STATIC_choose_reg.model()

            # # Lista para armazenar os textos das regiões marcadas
            # selected_regions = []

            # # Itere pelos itens no modelo para verificar o estado da checkbox
            # for index in range(model.rowCount()):
            #     item = model.item(index)  # Obtenha o QStandardItem
            #     if item.checkState() == Qt.Checked:  # Verifique se a checkbox está marcada
            #         selected_regions.append(item.text())  # Adicione o texto à lista

            # # Agora, selected_regions_str contém os nomes das regiões marcadas, separados por vírgulas
            # print(f"Regiões selecionadas: {selected_regions}")

            # # Armazene em outro lugar (por exemplo, uma variável de classe)
            # self.selected_regions = selected_regions


            # se for boxplot, ele precisa dessa info pra plotar uma ou mais regiões
            groupbyreg = self.ui.STATIC_group_reg.isChecked()
            print("groupbyreg deu:", groupbyreg)

            # informações referentes aos plots de índices
            model = self.ui.STATIC_voltage_ind.model()
            all_same_plot = self.ui.STATIC_all_sameplot.isChecked()
            regions_selected = self.ui.STATIC_c.currentText()
            checked_voltages = [model.item(i).text() for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]
            # voltage_group = self.get_checked_voltage_levels()
            print()
            print(all_same_plot)
            print(regions_selected)
            print(checked_voltages)
            print()
                
            y_var = self.ui.STATIC_y.currentText()
            c_var = self.ui.STATIC_c.currentText()



            # if c_var == 'REG':
            #     reg_var = self.selected_regions
            # else:
            #     reg_var = ''

            # reg_var = self.selected_regions

            p_var = self.ui.STATIC_type_button.currentText()
            # s_var = self.ui.STATIC_stats.currentText()


            self.STATIC_plot = {'y' : y_var,
                                'c' : c_var,

                                'groupbyreg' : groupbyreg,
                                'all same plot' : all_same_plot,
                                'region_selected' : regions_selected,
                                'checked_voltages' : checked_voltages,

                                'plot'  : p_var,

                                'y_label' : y_var
                                }

            # data = pd.read_csv(self.ui.STATIC_vars_qline.text())
            print(y_var)

            # guip = GUI_Plotter_STATIC(data, self.STATIC_plot, self.ui)
            guip = PlotterMainStatic(path1, self.ui, self.STATIC_plot, p_var, y_var)
            guip.update()
        
        else:

            select_data1 = path1.split('/')[-1].replace('.csv', '')
            select_data2 = path2.split('/')[-1].replace('.csv', '')
            plot_type = self.ui.STATIC_type_button.currentText()
            current_column = self.ui.STATIC_y.currentText()

            if 'DF_Intercambios' in select_data1 and 'DF_HVDC' in select_data2:

                # concatenação dos dois arquivos
                # df_pwf16 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_Intercambios.csv').drop('key', axis=1)
                df_pwf16 = pd.read_csv(path1).drop('key', axis=1)
                df_pwf16.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']
                # # df_pwf25 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_HVDC.csv').drop('key', axis=1)
                df_pwf25 = pd.read_csv(path2).drop('key', axis=1)
                df_pwf25_cols = df_pwf25.columns.tolist()
                df_pwf25_cols = df_pwf25_cols[-1:] + df_pwf25_cols[:-1]
                df_pwf25 = df_pwf25[df_pwf25_cols]
                df_pwf25.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']
                df_pwf = pd.concat([df_pwf16, df_pwf25], axis=0).reset_index().drop('index', axis=1)

                # Sua lista de opções
                options = ['NE -> T', 'NE -> SE', 'N -> S', 'SUL -> SECO', 'NE -> N', 
                        'RSUL -> T', 'FOZ -> IBIUNA', 'PVEL -> ARARQ', 'CPVBTB -> PVEL', 'XINGU -> SE']

                # Valor selecionado da combobox (por exemplo, o item selecionado)
                # selected_value = 'NE -> SE'  # Este valor você irá recuperar da sua combobox

                if plot_type in ['Persistence Curve', 'Heatmap']:
                    selected_value = self.ui.STATIC_c.currentText()

                    # Encontrar o índice 'k' do item selecionado
                    k = options.index(selected_value)
                else:
                    selected_value = ''
                    k = ''

                print(f"O índice do item selecionado '{selected_value}' é: {k}")

                # selected_value = self.ui.STATIC_y.currentText()

                plotter = CreatePlots(self.ui, fluxo=selected_value, indice=k)

                if plot_type == 'Persistence Curve':
                    print('entrei no persistence')
                    print(current_column)
                    plotter.persistency_curve(dataset=df_pwf, 
                                            col=current_column,
                                            ui=self.ui,
                                            fluxo=selected_value,
                                            indice=k,
                                            #   path=path, 
                                            ax_fontsize=13)
                elif plot_type == 'Boxplot':
                    plotter.box_plots(dataset=df_pwf, 
                                    col=current_column, 
                                    ui=self.ui,
                                    split_flows=False,
                                    #   path=path,
                                    ax_fontsize=11
                                    )
                elif plot_type == 'Violin Plot':
                    print('entrei no violin')
                    print(current_column)
                    plotter.violin_plots(dataset=df_pwf, 
                                        col=current_column, 
                                        ui=self.ui,
                                        split_flows=False,
                                        #  path=path,
                                        ax_fontsize=11,
                                        )
                elif plot_type == 'Heatmap':
                    print('entrei no heatmap')
                    print(current_column)
                    plotter.create_heatmap(dataset=df_pwf, 
                                   col=current_column,
                                   ui=self.ui,
                                   indice=k,
                                #    path=path, 
                                   ax_fontsize=11)
                elif plot_type == 'Contour Plot':
                    plotter.create_contourplot(dataset=df_pwf, 
                                       col='P(MW)', 
                                       ui=self.ui,
                                    #    path=path, 
                                       ax_fontsize=11)


            elif 'DF_Intercambios' in select_data2 and 'DF_HVDC' in select_data1:

                # concatenação dos dois arquivos
                # df_pwf16 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_Intercambios.csv').drop('key', axis=1)
                df_pwf16 = pd.read_csv(path2).drop('key', axis=1)
                df_pwf16.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']
                # # df_pwf25 = pd.read_csv(main_path+'/Data/Fluxo em Ramos/DF_HVDC.csv').drop('key', axis=1)
                df_pwf25 = pd.read_csv(path1).drop('key', axis=1)
                df_pwf25_cols = df_pwf25.columns.tolist()
                df_pwf25_cols = df_pwf25_cols[-1:] + df_pwf25_cols[:-1]
                df_pwf25 = df_pwf25[df_pwf25_cols]
                df_pwf25.columns = ['Nome Elo', 'Dia', 'Hora', 'P(MW)', 'Q(MVAr)']
                df_pwf = pd.concat([df_pwf16, df_pwf25], axis=0).reset_index().drop('index', axis=1)

                # Sua lista de opções
                options = ['NE -> T', 'NE -> SE', 'N -> S', 'SUL -> SECO', 'NE -> N', 
                        'RSUL -> T', 'FOZ -> IBIUNA', 'PVEL -> ARARQ', 'CPVBTB -> PVEL', 'XINGU -> SE']

                # Valor selecionado da combobox (por exemplo, o item selecionado)
                # selected_value = 'NE -> SE'  # Este valor você irá recuperar da sua combobox

                if plot_type in ['Persistence Curve', 'Heatmap']:
                    selected_value = self.ui.STATIC_c.currentText()

                    # Encontrar o índice 'k' do item selecionado
                    k = options.index(selected_value)
                else:
                    selected_value = ''
                    k = ''

                print(f"O índice do item selecionado '{selected_value}' é: {k}")

                plotter = CreatePlots(self.ui, fluxo=selected_value, indice=k)

                if plot_type == 'Persistence Curve':
                    plotter.persistency_curve(dataset=df_pwf, 
                                            col=current_column,
                                            ui=self.ui,
                                            fluxo=selected_value,
                                            indice=k,
                                            #   path=path, 
                                            ax_fontsize=13)
                elif plot_type == 'Boxplot':
                    plotter.box_plots(dataset=df_pwf, 
                                    col=current_column, 
                                    ui=self.ui,
                                    split_flows=False,
                                    #   path=path,
                                    ax_fontsize=11
                                    )
                elif plot_type == 'Violin Plot':
                    plotter.violin_plots(dataset=df_pwf, 
                                        col=current_column, 
                                        ui=self.ui,
                                        split_flows=False,
                                        #  path=path,
                                        ax_fontsize=11,
                                        )
                elif plot_type == 'Heatmap':
                    print('entrei no heatmap')
                    print(current_column)
                    plotter.create_heatmap(dataset=df_pwf, 
                                   col=current_column,
                                   ui=self.ui,
                                   indice=k,
                                #    path=path, 
                                   ax_fontsize=11)
                elif plot_type == 'Contour Plot':
                    plotter.create_contourplot(dataset=df_pwf, 
                                       col='P(MW)', 
                                       ui=self.ui,
                                    #    path=path, 
                                       ax_fontsize=11)
                    
            elif 'Df_Linhas' in select_data1 and 'PWF_NC' in select_data2:

                PWF16_Filt = pd.read_csv(path1)

                tipo_plot = self.ui.STATIC_type_button.currentText()
                reg = self.ui.STATIC_y.currentText()
                categoria_plot = self.ui.STATIC_c.currentText()

                model = self.ui.STATIC_voltage_ind.model()
                checked_voltages = [model.item(i).text() for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

                print(checked_voltages)  # Imprime a lista já ordenada
                print(tipo_plot, reg, categoria_plot)

                linha_teste = Analise_Linhas(PWF16_Filt, ui=self.ui, tipo=tipo_plot, regiao=reg, categoria=categoria_plot, voltages=checked_voltages)
                linha_teste.Removedor_n_convergiu(path2)

                if tipo_plot == 'Maior L1' or tipo_plot == 'Heatmap Região' or tipo_plot == 'Boxplot por Região' or tipo_plot == 'Média Geral por Região' or tipo_plot == 'Histograma por Tensão' or tipo_plot == 'Histograma por Região':
                    print('aqui eu entrei')

                    linha_teste.Graficos_Por_REG(ui=self.ui, regiao=reg, categoria=categoria_plot, voltages=checked_voltages)
                
                elif tipo_plot == 'Por Região e por Tensão' or tipo_plot == 'Heatmap Tensão':
                    print('agora entrei aqui')

                    linha_teste.Graficos_Por_VBA(ui=self.ui, regiao=reg, categoria=categoria_plot, voltages=checked_voltages)
                
                elif tipo_plot == 'Maior Carregamento':
                    print('fechei entrando aqui')

                    linha_teste.Analises_Especificas(ui=self.ui)



            elif 'Df_Linhas' in select_data2 and 'PWF_NC' in select_data1:

                PWF16_Filt = pd.read_csv(path2)

                tipo_plot = self.ui.STATIC_type_button.currentText()
                reg = self.ui.STATIC_y.currentText()
                categoria_plot = self.ui.STATIC_c.currentText()

                model = self.ui.STATIC_voltage_ind.model()
                checked_voltages = [model.item(i).text() for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

                print(checked_voltages)  # Imprime a lista já ordenada
                print(tipo_plot, reg, categoria_plot)

                linha_teste = Analise_Linhas(PWF16_Filt, ui=self.ui, tipo=tipo_plot, regiao=reg, categoria=categoria_plot, voltages=checked_voltages)
                linha_teste.Removedor_n_convergiu(path1)

                if tipo_plot == 'Maior L1' or tipo_plot == 'Heatmap Região' or tipo_plot == 'Boxplot por Região' or tipo_plot == 'Média Geral por Região' or tipo_plot == 'Histograma por Tensão' or tipo_plot == 'Histograma por Região':
                    print('aqui eu entrei')

                    linha_teste.Graficos_Por_REG(ui=self.ui, regiao=reg, categoria=categoria_plot, voltages=checked_voltages)
                
                elif tipo_plot == 'Por Região e por Tensão' or tipo_plot == 'Heatmap Tensão':
                    print('agora entrei aqui')

                    linha_teste.Graficos_Por_VBA(ui=self.ui, regiao=reg, categoria=categoria_plot, voltages=checked_voltages)
                
                elif tipo_plot == 'Maior Carregamento':
                    print('fechei entrando aqui')

                    linha_teste.Analises_Especificas(ui=self.ui)








    def STATIC_add_section_button_FUNCTION(self):

        

        self.STA_json_to_plot[self.ui.STATIC_add_section.text()] = {}

        self.STA_sections.append(self.ui.STATIC_add_section.text())

        for i in range(len(self.STA_sections)-1):
            self.ui.STATIC_sections_ava.removeItem(0)
            self.ui.STATIC_select_section.removeItem(0)

        self.ui.STATIC_sections_ava.addItems(self.STA_sections)

        self.ui.STATIC_select_section.addItems(self.STA_sections)

        for i in range(self.ui.STATIC_select_plot.count()):
            self.ui.STATIC_select_plot.removeItem(0)

        self.ui.STATIC_select_plot.addItems(list(self.STA_json_to_plot[self.ui.STATIC_select_section.currentText()].keys()))


    def STATIC_add_plot_button_FUNCTION(self):

        self.STA_json_to_plot[self.ui.STATIC_sections_ava.currentText()][self.ui.STATIC_add_plot.text()] = []

        for i in range(self.ui.STATIC_select_plot.count()):
            self.ui.STATIC_select_plot.removeItem(0)

        self.ui.STATIC_select_plot.addItems(list(self.STA_json_to_plot[self.ui.STATIC_select_section.currentText()].keys()))


    def STATIC_select_section_FUNCTION(self):

        for i in range(self.ui.STATIC_select_plot.count()):
            self.ui.STATIC_select_plot.removeItem(0)

        self.ui.STATIC_select_plot.addItems(list(self.STA_json_to_plot[self.ui.STATIC_select_section.currentText()].keys()))


    def STATIC_add_to_json_button_FUNCTION(self):
        
        page    = self.ui.STATIC_select_plot.currentText()
        section = self.ui.STATIC_select_section.currentText()

        self.STA_json_to_plot[section][page].append(self.STATIC_plot)


    def STATIC_page_to_plot_button_FUNCTION(self):

        page    = self.ui.STATIC_select_plot.currentText()
        section = self.ui.STATIC_select_section.currentText()

        self.STATIC_plot = self.STA_json_to_plot[section][page][0]


        temp_filter = []
        if self.STATIC_plot['filter'] is not None and self.STATIC_plot['filter'] != '':

            for f_var, i_var, t_var in self.STATIC_plot['filter']:
        
                if ',' in str(t_var):
                    try:
                        t_var = [float(f) for f in t_var.split(',')]
                    except:
                        t_var = [f for f in t_var.split(',')]

                try:
                    t_var = float(t_var)
                except:
                    pass

                temp_filter.append((f_var, i_var, t_var))    

            self.STATIC_plot['filter'] = temp_filter   

        data = pd.read_csv(self.ui.STATIC_vars_qline.text())        

        guip = GUI_Plotter(data, self.STATIC_plot, self.ui)
        guip.update()




    def STATIC_save_json_button_FUNCTION(self):
        
        path = self.ui.STATIC_vars_qline.text().split('/')
        path = '/'.join(path[:-1]) + '/plot.json'


        with open(path, 'w') as fp:
            json.dump(self.STA_json_to_plot, fp)





    def STATIC_search_json_button_FUNCTION(self): 


        self.file_vars, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "json (*.json);;All files(*.*)")
        self.file_vars    = self.file_vars[0]

        self.ui.STATIC_qline_json_files.setText(self.file_vars)    


    def STATIC_read_json_button_FUNCTION(self): 

        path = self.ui.STATIC_qline_json_files.text()

        with open(path) as f:
            data = json.load(f)

        self.STA_json_to_plot = data
        self.STA_sections     = list(self.STA_json_to_plot.keys())


        for i in range(self.ui.STATIC_sections_ava.count()):
            self.ui.STATIC_sections_ava.removeItem(0)
            self.ui.STATIC_select_section.removeItem(0)

        self.ui.STATIC_sections_ava.addItems(self.STA_sections)
        self.ui.STATIC_select_section.addItems(self.STA_sections)



        for i in range(self.ui.STATIC_select_plot.count()):
            self.ui.STATIC_select_plot.removeItem(0)

        self.ui.STATIC_select_plot.addItems(list(self.STA_json_to_plot[self.ui.STATIC_select_section.currentText()].keys()))


    def run_STATIC_FUNCTION(self): 
        
        base_path = self.ui.STATIC_qline_json_files.text().split('/')
        save_path = '/'.join(base_path[:-1]) + '/Report.pdf'

        data_p = self.ui.STATIC_vars_qline.text()
        path   = self.ui.STATIC_qline_json_files.text()

        data = pd.read_csv(data_p)


        PP = Plotter(data, path)

        data_plot = {}

        for section in PP.plot.keys():

            temp = PP.plot[section]

            data_plot[section] = []        
            
            for page in temp.keys():

                plots = temp[page]
                figs  = []

                for plot in plots:

                    fig = PP.plot_from_json(data, plot, len(plots))
                    figs.append(fig)

                    data_plot[section].append((figs, page))
            


        PDF = PDFGenerator('Report', data_plot)
        pdf = PDF.fit()
        pdf.output(save_path)  

        self.ui.STATIC_document.load(save_path)


    def actionSave_STATIC_FUNCTION(self): 

        base_path = self.ui.STATIC_qline_json_files.text().split('/')
        file_path = '/'.join(base_path[:-1]) + '/Report.pdf'
        
        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.pdf);;All files(*.*)")
        save_path    = save_path.split('.')[0]

        shutil.copyfile(file_path, save_path + '.pdf')


    def actionZoom_In_STATIC_FUNCTION(self):

        factor = self.ui.pdfView_STATIC.zoomFactor() * 2
        self.ui.pdfView_STATIC.setZoomFactor(factor)

    
    def actionZoom_Out_STATIC_FUNCTION(self):

        factor = self.ui.pdfView_STATIC.zoomFactor() / 2
        self.ui.pdfView_STATIC.setZoomFactor(factor)

    def actionPage_down_STATIC_FUNCTION(self):

        nav = self.ui.pdfView_STATIC.pageNavigator()
        nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    def actionPage_up_STATIC_FUNCTION(self):

        nav = self.ui.pdfView_STATIC.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())





























    def instavel_button(self): 

        save_path = '/'.join(self.file_vars.split('/')[:-1]) + '/IMAGENS/INSTAVEL/'

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        RP = RST_Plot_instavel(report_path = self.file_vars,
                                save_path   = save_path)

        RP.plot_inst_days_hours(show=False)
        RP.plot_inst_contigence_bus(show=False)
        RP.plot_inst_contigence_op(show=False)
        RP.plot_inst_histogram_contingence(show=False)
        RP.plot_inst_histogram_operation_points(show=False)
        RP.plot_inst_histogram_day(show=False)
        RP.plot_inst_histogram_hour(show=False)
        RP.plot_inst_histogram_CODE(show=False)
        RP.plot_code_histogram_CODE(show=False)

        for code in [2, 3, 4]:

            save_path = '/'.join(self.file_vars.split('/')[:-1]) + f'/IMAGENS/INSTAVEL/CODE_{code}/'

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            RP = RST_Plot_instavel(report_path  = self.file_vars,
                                    save_path   = save_path,
                                    code_filtro = [code])

            RP.plot_inst_days_hours(show=False)
            RP.plot_inst_contigence_bus(show=False)
            RP.plot_inst_contigence_op(show=False)
            RP.plot_inst_histogram_contingence(show=False)
            RP.plot_inst_histogram_operation_points(show=False)
            RP.plot_inst_histogram_day(show=False)
            RP.plot_inst_histogram_hour(show=False)
            RP.plot_inst_histogram_CODE(show=False)
            RP.plot_code_histogram_CODE(show=False)


    def estavel_button(self): 



        tipos = {'CC e Abertura de Linha'                       : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], #1, 8, 9
                'Perda de Geração'                             : [11, 12, 13, 14, 15],
                'Bloqueio de Polo'                             : [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                'Falha de comutação nos elos HVDC'             : [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 46, 47],
                'Perda dupla de linha'                         : [44, 45],
                'Curto na LT CC seguido do bloqueio do bipolo' : [48, 49],
                'Bloqueio (ESOF) do bipolo com FCB'            : [50, 51],}


        cc = tipos['CC e Abertura de Linha']
        pg = tipos['Perda de Geração']
        bp = tipos['Bloqueio de Polo']
        fc = tipos['Falha de comutação nos elos HVDC']
        dl = tipos['Perda dupla de linha']
        cb = tipos['Curto na LT CC seguido do bloqueio do bipolo']
        es = tipos['Bloqueio (ESOF) do bipolo com FCB']

        conts = [cc, pg, bp, fc, dl, cb, es]



        save_path = '/'.join(self.file_vars.split('/')[:-1]) + '/IMAGENS/ESTAVEL/'

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        RP = RST_Plot_estavel(report_path = self.file_vars,
                               save_path  = save_path)

        RP.plot_est_violin_rocof()
        RP.plot_est_violin_nadir()

        RP.plot_est_duplo_hist_RCFC_NDRC()
        RP.plot_est_duplo_hist_NDRC_NDRC()



    def per_cont_button(self): 



        tipos = {'CC e Abertura de Linha'                       : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], #1, 8, 9
                'Perda de Geração'                             : [11, 12, 13, 14, 15],
                'Bloqueio de Polo'                             : [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                'Falha de comutação nos elos HVDC'             : [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 46, 47],
                'Perda dupla de linha'                         : [44, 45],
                'Curto na LT CC seguido do bloqueio do bipolo' : [48, 49],
                'Bloqueio (ESOF) do bipolo com FCB'            : [50, 51],}


        cc = tipos['CC e Abertura de Linha']
        pg = tipos['Perda de Geração']
        bp = tipos['Bloqueio de Polo']
        fc = tipos['Falha de comutação nos elos HVDC']
        dl = tipos['Perda dupla de linha']
        cb = tipos['Curto na LT CC seguido do bloqueio do bipolo']
        es = tipos['Bloqueio (ESOF) do bipolo com FCB']

        conts = [cc, pg, bp, fc, dl, cb, es]


        for i in tqdm(range(0, 52)):

            save_path = '/'.join(self.file_vars.split('/')[:-1])

            folder = f'{save_path}/IMAGENS/CONT/CONT_' + str(i) + '/'

            if not os.path.exists(folder):
                os.makedirs(folder)

            RP = RST_Plot_estavel(report_path   = self.file_vars,
                                    save_path   = folder)


            RP.RCFC_comparation(x_variable='DCIM'  , xlabel='DCIM', title='RoCoF x DCIM [ILHA 1][Mean]', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='TGEN'  , xlabel='TGEN', title='RoCoF x TGEN [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GMAX'  , xlabel='GMAX', title='RoCoF x GMAX [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GRES'  , xlabel='GRES', title='RoCoF x GRES [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GINR'  , xlabel='GINR', title='RoCoF x GINR [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GIMX'  , xlabel='GIMX', title='RoCoF x GIMX [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GIRS'  , xlabel='GIRS', title='RoCoF x GIRS [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='EMXI'  , xlabel='EMXI', title='RoCoF x EMXI [ILHA 1][Mean]', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='TINR'  , xlabel='Inertia [MW.s]', title='RoCoF x Inertia', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='LOAD'  , xlabel='LOAD', title='RoCoF x LOAD [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='LOSS'  , xlabel='LOSS', title='RoCoF x LOSS [ILHA 1][Mean]', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='INER'  , xlabel='INER', title='RoCoF x INER [ILHA 1][Mean]', contigence=[i], mean=True , round=3   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='INDC'  , xlabel='INDC', title='RoCoF x INDC [ILHA 1][Mean]', contigence=[i], mean=True , round=4   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='INLD'  , xlabel='INLD', title='RoCoF x INLD [ILHA 1][Mean]', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='TRSV'  , xlabel='TRSV', title='RoCoF x TRSV [ILHA 1][Mean]', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='HRSV'  , xlabel='HRSV', title='RoCoF x HRSV [ILHA 1][Mean]', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='Reserva', xlabel='Generation Reserve [MW]', title='RoCoF x Generation Reserve', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)


            RP.NDRC_comparation(x_variable='DCIM'  , xlabel='DCIM', title='Frequency Nadir x DCIM [ILHA 1][Mean]', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='TGEN'  , xlabel='TGEN', title='Frequency Nadir x TGEN [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GMAX'  , xlabel='GMAX', title='Frequency Nadir x GMAX [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GRES'  , xlabel='GRES', title='Frequency Nadir x GRES [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GINR'  , xlabel='GINR', title='Frequency Nadir x GINR [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GIMX'  , xlabel='GIMX', title='Frequency Nadir x GIMX [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GIRS'  , xlabel='GIRS', title='Frequency Nadir x GIRS [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='EMXI'  , xlabel='EMXI', title='Frequency Nadir x EMXI [ILHA 1][Mean]', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='TINR'  , xlabel='Inertia [MW.s]', title='Frequency Nadir x Inertia', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='LOAD'  , xlabel='LOAD', title='Frequency Nadir x LOAD [ILHA 1][Mean]', contigence=[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='LOSS'  , xlabel='LOSS', title='Frequency Nadir x LOSS [ILHA 1][Mean]', contigence=[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='INER'  , xlabel='INER', title='Frequency Nadir x INER [ILHA 1][Mean]', contigence=[i], mean=True , round=3   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='INDC'  , xlabel='INDC', title='Frequency Nadir x INDC [ILHA 1][Mean]', contigence=[i], mean=True , round=4   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='INLD'  , xlabel='INLD', title='Frequency Nadir x INLD [ILHA 1][Mean]', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='TRSV'  , xlabel='TRSV', title='Frequency Nadir x TRSV [ILHA 1][Mean]', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='HRSV'  , xlabel='HRSV', title='Frequency Nadir x HRSV [ILHA 1][Mean]', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='Reserva'  , xlabel='Generation Reserve [MW]', title='Frequency Nadir x Generation Reserve', contigence=[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)




            RP.RCFC_comparation(x_variable='DCIM'  , xlabel='DCIM', title='RoCoF x DCIM [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='TGEN'  , xlabel='TGEN', title='RoCoF x TGEN [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='GMAX'  , xlabel='GMAX', title='RoCoF x GMAX [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='GRES'  , xlabel='GRES', title='RoCoF x GRES [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='GINR'  , xlabel='GINR', title='RoCoF x GINR [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='GIMX'  , xlabel='GIMX', title='RoCoF x GIMX [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='GIRS'  , xlabel='GIRS', title='RoCoF x GIRS [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='EMXI'  , xlabel='EMXI', title='RoCoF x EMXI [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='TINR'  , xlabel='Inertia [MW.s]', title='RoCoF x Inertia', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='LOAD'  , xlabel='LOAD', title='RoCoF x LOAD [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='LOSS'  , xlabel='LOSS', title='RoCoF x LOSS [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='INER'  , xlabel='INER', title='RoCoF x INER [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='INDC'  , xlabel='INDC', title='RoCoF x INDC [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='INLD'  , xlabel='INLD', title='RoCoF x INLD [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='TRSV'  , xlabel='TRSV', title='RoCoF x TRSV [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='HRSV'  , xlabel='HRSV', title='RoCoF x HRSV [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.RCFC_comparation(x_variable='Reserva'  , xlabel='Generation Reserve [MW]', title='RoCoF x Generation Reserve', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)


            RP.NDRC_comparation(x_variable='DCIM'   , xlabel='DCIM', title='Frequency Nadir x DCIM [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='TGEN'   , xlabel='TGEN', title='Frequency Nadir x TGEN [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='GMAX'   , xlabel='GMAX', title='Frequency Nadir x GMAX [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='GRES'   , xlabel='GRES', title='Frequency Nadir x GRES [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='GINR'   , xlabel='GINR', title='Frequency Nadir x GINR [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='GIMX'   , xlabel='GIMX', title='Frequency Nadir x GIMX [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='GIRS'   , xlabel='GIRS', title='Frequency Nadir x GIRS [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='EMXI'   , xlabel='EMXI', title='Frequency Nadir x EMXI [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='TINR'   , xlabel='Inertia [MW.s]', title='Frequency Nadir x Inertia', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='LOAD'   , xlabel='LOAD', title='Frequency Nadir x LOAD [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='LOSS'   , xlabel='LOSS', title='Frequency Nadir x LOSS [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='INER'   , xlabel='INER', title='Frequency Nadir x INER [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='INDC'   , xlabel='INDC', title='Frequency Nadir x INDC [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='INLD'   , xlabel='INLD', title='Frequency Nadir x INLD [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='TRSV'   , xlabel='TRSV', title='Frequency Nadir x TRSV [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='HRSV'   , xlabel='HRSV', title='Frequency Nadir x HRSV [ILHA 1]', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)
            RP.NDRC_comparation(x_variable='Reserva', xlabel='Generation Reserve [MW]', title='Frequency Nadir x Generation Reserve', contigence=[i], mean=False , round=None  , islands=[1], single=True , show=False, line=False)


    def per_group_button(self): 



        tipos = {'CC e Abertura de Linha'                       : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], #1, 8, 9
                'Perda de Geração'                             : [11, 12, 13, 14, 15],
                'Bloqueio de Polo'                             : [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                'Falha de comutação nos elos HVDC'             : [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 46, 47],
                'Perda dupla de linha'                         : [44, 45],
                'Curto na LT CC seguido do bloqueio do bipolo' : [48, 49],
                'Bloqueio (ESOF) do bipolo com FCB'            : [50, 51],}


        cc = tipos['CC e Abertura de Linha']
        pg = tipos['Perda de Geração']
        bp = tipos['Bloqueio de Polo']
        fc = tipos['Falha de comutação nos elos HVDC']
        dl = tipos['Perda dupla de linha']
        cb = tipos['Curto na LT CC seguido do bloqueio do bipolo']
        es = tipos['Bloqueio (ESOF) do bipolo com FCB']

        conts = [cc, pg, bp, fc, dl, cb, es]

        for i in tqdm(range(0, 7)):


            save_path = '/'.join(self.file_vars.split('/')[:-1])

            folder = f'{save_path}/IMAGENS/GRUPOS/GRUPO_' + str(i) + '/'

            if not os.path.exists(folder):
                os.makedirs(folder)

            RP = RST_Plot_estavel(report_path   = self.file_vars,
                                    save_path   = folder)


            RP.RCFC_comparation(x_variable='DCIM'  , xlabel='DCIM', title='RoCoF x DCIM [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='TGEN'  , xlabel='TGEN', title='RoCoF x TGEN [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GMAX'  , xlabel='GMAX', title='RoCoF x GMAX [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GRES'  , xlabel='GRES', title='RoCoF x GRES [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GINR'  , xlabel='GINR', title='RoCoF x GINR [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GIMX'  , xlabel='GIMX', title='RoCoF x GIMX [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='GIRS'  , xlabel='GIRS', title='RoCoF x GIRS [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='EMXI'  , xlabel='EMXI', title='RoCoF x EMXI [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='TINR'  , xlabel='TINR', title='RoCoF x TINR [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='LOAD'  , xlabel='LOAD', title='RoCoF x LOAD [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='LOSS'  , xlabel='LOSS', title='RoCoF x LOSS [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='INER'  , xlabel='INER', title='RoCoF x INER [ILHA 1][Mean]', contigence=conts[i], mean=True , round=3   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='INDC'  , xlabel='INDC', title='RoCoF x INDC [ILHA 1][Mean]', contigence=conts[i], mean=True , round=4   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='INLD'  , xlabel='INLD', title='RoCoF x INLD [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='TRSV'  , xlabel='TRSV', title='RoCoF x TRSV [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='HRSV'  , xlabel='HRSV', title='RoCoF x HRSV [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.RCFC_comparation(x_variable='Reserva'  , xlabel='Reserva', title='RoCoF x Reserva [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)


            RP.NDRC_comparation(x_variable='DCIM'  , xlabel='DCIM', title='Nadir x DCIM [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='TGEN'  , xlabel='TGEN', title='Nadir x TGEN [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GMAX'  , xlabel='GMAX', title='Nadir x GMAX [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GRES'  , xlabel='GRES', title='Nadir x GRES [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GINR'  , xlabel='GINR', title='Nadir x GINR [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GIMX'  , xlabel='GIMX', title='Nadir x GIMX [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='GIRS'  , xlabel='GIRS', title='Nadir x GIRS [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='EMXI'  , xlabel='EMXI', title='Nadir x EMXI [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='TINR'  , xlabel='TINR', title='Nadir x TINR [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='LOAD'  , xlabel='LOAD', title='Nadir x LOAD [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-3  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='LOSS'  , xlabel='LOSS', title='Nadir x LOSS [ILHA 1][Mean]', contigence=conts[i], mean=True , round=-2  , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='INER'  , xlabel='INER', title='Nadir x INER [ILHA 1][Mean]', contigence=conts[i], mean=True , round=3   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='INDC'  , xlabel='INDC', title='Nadir x INDC [ILHA 1][Mean]', contigence=conts[i], mean=True , round=4   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='INLD'  , xlabel='INLD', title='Nadir x INLD [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='TRSV'  , xlabel='TRSV', title='Nadir x TRSV [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='HRSV'  , xlabel='HRSV', title='Nadir x HRSV [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)
            RP.NDRC_comparation(x_variable='Reserva'  , xlabel='Reserva', title='Nadir x Reserva [ILHA 1][Mean]', contigence=conts[i], mean=True , round=1   , islands=[1], single=True , show=False, line=True)

        
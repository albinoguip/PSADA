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
# GLOBAL_TITLE_BAR = True


class DYN_Functions(MainWindow):

    def __init__(self, ui):
        
        
        # self.ui = ui

        # self.ui.dvp_sf_button.clicked.connect(self.button_clicked)

        pass

        


    def constructor(self):

        self.data_match_df = None




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                       DVP                                                                      ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    def data_match_local_search_button_function(self): 

        self.file_data_match = str(QFileDialog.getExistingDirectory(self, "Select Directory")) + '/'

        self.ui.dynamic_qline_files.setText(self.file_data_match)


    def dvp_sf_button_function(self): 

        self.file_names_dvp = str(QFileDialog.getExistingDirectory(self, "Select Directory")) + '/'

        self.ui.dynamic_qline_files_out.setText(self.file_names_dvp)


    def processed_open_button_function(self): 


        self.file_vars, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Excel (*.csv);;All files(*.*)")

        self.file_vars = self.file_vars[0]

        self.ui.dynamic_vars_qline.setText(self.file_vars)     

        self.rst_generic = RST_Generic(report_path = self.file_vars,
                                       eol         = None,
                                       sol         = None,
                                       save_path   = None,
                                       code_filtro = None)
        

        c_options = [None]
        c_options.extend(list(self.rst_generic._get_variables()))

        self.ui.dynamic_x.addItems(self.rst_generic._get_variables())
        self.ui.dynamic_y.addItems(self.rst_generic._get_variables())
        self.ui.dynamic_c.addItems(c_options)

        self.ui.dynamic_plot.addItems(['Scatter', 'Line', 'Histogram'])
        self.ui.dynamic_c.addItems([None, 'Mean'])





    def dvp_read_file_button_function(self):

        PATH    = self.file_data_match
        # FOLDERS = os.listdir(PATH)
        POUT    = self.file_names_dvp + 'OUT/'

        if not os.path.exists(POUT):
            os.makedirs(POUT)

        RSTS = os.listdir(PATH)
        RSTS = [rst for rst in RSTS if '.rst' in rst]

        for rst in RSTS:
            new_name =  'D_' + rst.replace('Dia_', '').split('_')[0] + '_H_' + rst.split('_')[-1].split('.')[0] + '.rst'
            shutil.copyfile(PATH + rst, POUT + '/' + new_name)

        PATH = POUT 
        RSTS = glob.glob(PATH + "*.rst")
        vars = pd.DataFrame()


        for RST in tqdm(RSTS):

            RR = RST_Reader(RST)
            a, net_info = RR.generate_json()

            rede = np.expand_dims(np.array(net_info).ravel(), axis=(0))
            columns = []
            for isl in net_info['ISLD']:
                for col in net_info.columns:
                    columns.append(col + '_I' + isl)
            net_info = pd.DataFrame(rede, columns=columns)

            name          = RST.split('\\')[-1].split('.')[0]
            RP            = RST_Process(a, name=name)

            # print(RP.df)

            if RP.df is not None:

                RP.df.columns = [col[0] if col[1] == '' else col[0] + '_' + col[1] for col in RP.df.columns]

                RP.df['Dia']        = name.split('_')[1]
                RP.df['Contigence'] = [int(a.split('_')[-1]) for a in RP.df['Contigence']]
                RP.df['Hora']       = [a.split('_')[-1] for a in RP.df['OP']]
                RP.df['OP']         = 'D_' + RP.df['Dia'] + '_H_' + RP.df['Hora']
                RP.df['Dia']        = RP.df['Dia'].astype('int')
                RP.df['A_CODE']     = RP.df['A_CODE'].astype('int')

                RP.df = RP.df.sort_values(by=['Dia', 'Hora', 'Contigence']).reset_index(drop=True)
                
                net_info['OP'] = RP.df['OP'].values[0]

                RP.df = RP.df.merge(net_info, on='OP', how='left')
                vars  = pd.concat([vars, RP.df]).reset_index(drop=True)

        vars.to_csv(PATH.replace('OUT/', '') + 'vars.csv', index=False)



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


    def dynamic_plot_function(self):

        print('cliclou')

        self.ui.sc.axes.cla()

        x_var = self.ui.dynamic_x.currentText()
        y_var = self.ui.dynamic_y.currentText()
        c_var = self.ui.dynamic_c.currentText()

        p_var = self.ui.dynamic_plot.currentText()
        s_var = self.ui.dynamic_stats.currentText()

        self.ui = self.rst_generic._change_plot(self.ui, 
                                                x_var, 
                                                y_var,
                                                p_var,
                                                c     = c_var, 
                                                stats = s_var)
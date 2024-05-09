from main import *
from PySide6.QtCore    import *
from PySide6.QtGui     import *
from PySide6.QtWidgets import *

from Modules.custom_grips import *
from Modules.Help_Widgets import *

import shutil, json

from win32com.shell import shell, shellcon




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


class UIFunctions(MainWindow):

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

        self.file_data_match, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Excel (*.xlsx);;All files(*.*)")

        file_str = ''
        for idx, f in enumerate(self.file_data_match):
            file_str += '\"' + f + '\"'

            if idx != len(self.file_data_match)-1: file_str += ', '

        self.ui.data_match_qline_files.setText(file_str)

    def data_match_read_file_button_function(self):

        print(self.file_data_match) 
        print(self.ui.dvp_combo_ptc.currentText())

        self.data_match_df = pd.read_excel(self.file_data_match[0])
        self.ui.dvp_combo_ptc.clear()
        self.ui.dvp_combo_ptc.addItems(self.data_match_df.drop('BASE', axis=1).columns)


    def dvp_sf_button_function(self): 

        self.file_names_dvp, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Files (*.csv *.dat);;All files(*.*)")

        file_str = ''
        for idx, f in enumerate(self.file_names_dvp):
            file_str += '\"' + f + '\"'

            if idx != len(self.file_names_dvp)-1: file_str += ', '

        self.ui.dvp_qline_files.setText(file_str)

    def dvp_read_file_button_function(self):

        print(self.file_names_dvp) 
        print(self.ui.dvp_combo_ptc.currentText())

        if self.data_match_df is None:
            self.data_match_df = pd.read_excel(resource_path('assets/Data_match.xlsx'))


        actual_data_match = self.data_match_df[[self.ui.dvp_combo_ptc.currentText(), 'BASE']]
        actual_data_match = actual_data_match.dropna().reset_index(drop=True)

        print(actual_data_match)

        data_match    = {k:v for k, v in zip(actual_data_match[self.ui.dvp_combo_ptc.currentText()], actual_data_match['BASE'])}
        paths         = self.file_names_dvp  

        print(data_match) 

        self.datas = []
        for path in paths:
            self.DPP = DataPreProcess(path, data_match)
            data, voltages, speed, name = self.DPP.fit()

            self.datas.append((data, voltages, speed, name))

        self.speed = speed

        self.DP = DataPlot(datas=[data for data, _, _, _ in self.datas], names=[name for _, _, _, name in self.datas])

        self.ui.dvp_select_data.clear()
        self.ui.dvp_select_data.addItems(paths)

        self.ui.dvp_combo_variable.clear()
        self.ui.dvp_combo_variable.addItems(self.DP.datas[0].columns)

        self.ui.dvp_combo_sinal.clear()
        self.ui.dvp_combo_sinal.addItems(['>', '<', '>=', '<='])

        self.DT = DataTransform()

    def dvp_read_file_button_ptc_function(self):
        print(self.ui.dvp_multi_combo_ptc.currentData()) 

    def dvp_concat_function(self):

        df_concat = pd.concat([help_concat(path) for path in self.file_names_dvp], axis=0)

        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        file_path  = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/concat_data.csv'

        df_concat.to_csv(file_path)

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.csv);;All files(*.*)")
        save_path    = save_path.split('.')[0]

        shutil.copyfile(file_path, save_path + '.csv')


    def dvp_see_plot_function(self):

        self.ui.sc.axes.cla()

        params=plots_list[self.ui.dvp_select_plot.currentText()]
        speed = None if self.ui.speed_select.currentText() == 'None' else self.ui.speed_select.currentText()
        voltage=None
        remove_zeros=False

        if not isinstance(params, list):
            params = [params]

        param = params[0]

        datas = [data for data in [self.DP.datas[self.ui.dvp_select_data.currentIndex()]]]    

        print(datas[0])
        datas = [self.DP._speed_filter(data, speed) for data in datas]                           # SELECT SPEED'S SIGN
        datas = [self.DP._voltage_filter(data, voltage) for data in datas]                           # SPECIFIC VOLTAGE
        datas = [self.DP._zero_filter(data, remove_zeros, param['c']) for data in datas]             # REMOVE ZEROS
        plot_data = [data.sort_values(by=param['x']) for data in datas]                           # SORT VALUES

        valores = None
        if param['c'] is not None:
            set_c = set()
            for data in plot_data:
                set_c = set_c.union(set(data[param['c']].unique()))
            valores = sorted(list(set_c), reverse=(speed == '-'))

        cu = plot_data[0]

        figs, colors, labels = [], [], []
        for idx in range(len(plot_data)):

            fig = plt.figure(figsize=(10, 8))
            for param in params:
                if param['c'] is None:

                    data  = cu
                    param = param

                    if param['stat'] is not None:
                        data = self.DP._stat_plots(data, param['stat'], param['x'], param['y'])
                
                    x = data[param['x']]
                    y = data[param['stat']] if param['stat'] is not None else data[param['y']]

                    l_scatter = param['label'] if (param['label'] is not None and param['scatter']) else None
                    l_label   = param['label'] if (param['label'] is not None and not param['scatter'] and param['line']) else None

                    color = param['color'] if param['color'] is not None else None

                    if param['scatter']: self.ui.sc.axes.scatter(x, y, color=color, label=l_scatter)
                    if param['line']:    self.ui.sc.axes.plot(x, y, color=color, label=l_label)


                else:

                    plot_data = plot_data[idx]
                    valores=valores
                    param=param
                    speed=speed

                    data = plot_data.sort_values(by=[param['c'], param['x']])

                    colormap = plt.cm.gist_rainbow
                    colors   = [colormap(i) for i in np.linspace(0, 1, len(valores))]

                    for idx, c in enumerate(valores):
                        
                        c_data = data[data[param['c']] == c]
                        c_data = self.DP._regen_power_check(c_data, param, speed) if param['title'] == 'DC Regen Power Check' else c_data

                        if c_data is None: continue

                        x, y      = c_data[param['x']], c_data[param['y']]
                        l_scatter = str(int(c))
                        l_label   = None

                        if param['scatter']: self.ui.sc.axes.scatter(x, y, color=colors[idx], label=l_scatter)
                        if param['line']:    self.ui.sc.axes.plot(x, y, color=colors[idx], label=l_label)

        self.ui.sc.axes.set_xlabel(param['x'])
        self.ui.sc.axes.set_ylabel(param['y'])

        self.ui.sc.axes.legend(bbox_to_anchor=(1.15, 1.5), loc='upper right', borderaxespad=0)
        self.ui.sc.axes.grid()

        self.ui.sc.draw()

    def dvp_apply_filter(self):


        
        self.DP.datas[self.ui.dvp_select_data.currentIndex()] = self.DT.fit(self.DP.datas[self.ui.dvp_select_data.currentIndex()], 
                                                                            filters=[(self.ui.dvp_combo_variable.currentText(), self.ui.dvp_combo_sinal.currentText(), float(self.ui.dvp_label_value.text()))],
                                                                            name=self.ui.dvp_select_data.currentText().split('/')[-1].split('.')[0])

 

    def run_dvp_function(self):

        lista = list(plots_list.values())


        chapters = [
                    ('Chapter: Overview', overview),
                    ('Chapter: Temperature', temps),
                    ('Chapter: Comparison', errorComparison),
                    ('Chapter: Comparison Torque', torques),
                    ('Chapter: Comparison Loss', losses_comp0),
                    ('Chapter: Estimated Loss', losses),
                    ('Chapter: Power Efficiency', wattEff),                
                    ('Chapter: Comparison Loss (eDrive)', E_losses_comp)
                    ]
       
        base_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        save_path = base_path + '/temp_dvp.pdf'

        PDF = PDFGenerator(self.file_names_dvp[0].split('/')[-1].split('.')[0], self.DP, chapters, self.speed)
        pdf = PDF.fit([self.ui.dvp_infos00_l.text(), self.ui.dvp_infos10_l.text(), self.ui.dvp_infos20_l.text(), 
                       self.ui.dvp_infos01_l.text(), self.ui.dvp_infos11_l.text(), self.ui.dvp_infos21_l.text(),
                       self.ui.dvp_infos30_l.text()], 

                       self.DT, self.DPP)
        
        
        pdf.output(save_path)    

        self.ui.m_document.load(save_path)

    def actionSave_function(self):

        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        file_path  = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_dvp.pdf'

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.pdf);;All files(*.*)")
        save_path    = save_path.split('.')[0]

        shutil.copyfile(file_path, save_path + '.pdf')

        print(save_path.split('/')[:-1])

        n = ''
        for a in save_path.split('/')[:-1]:
            n += a + '/'

        self.DP.excel(n, names=[path.split('/')[-1].split('.')[0] for path in self.file_names_dvp])


    def dvp_actionZoom_In_function(self):

        factor = self.ui.pdfView_dvp.zoomFactor() * 2
        self.ui.pdfView_dvp.setZoomFactor(factor)

    
    def dvp_actionZoom_Out_function(self):

        factor = self.ui.pdfView_dvp.zoomFactor() / 2
        self.ui.pdfView_dvp.setZoomFactor(factor)

    def dvp_actionPage_down_function(self):

        nav = self.ui.pdfView_dvp.pageNavigator()
        nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    def dvp_actionPage_up_function(self):

        nav = self.ui.pdfView_dvp.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                      DELAY                                                                     ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def delay_sf_button_function(self):

        self.file_names_delay, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Files (*.csv *.dat);;All files(*.*)")

        file_str = ''
        for idx, f in enumerate(self.file_names_delay):
            file_str += '\"' + f + '\"'

            if idx != len(self.file_names_delay)-1:
                file_str += ', '

        self.ui.delay_qline_files.setText(file_str)


    def delay_read_file_button_function(self):

        path = self.ui.delay_qline_files.text().replace("\"", '')

        with open(path, "r") as f:
            lines, skiprows = f.readlines(), []
            for idx, line in enumerate(lines[1:]):
                try:
                    int(line.split(',')[1])
                except:
                    skiprows.append(idx+1)

        data = pd.read_csv(path, skiprows=skiprows)

        df_simi = word_similarity(data)

        self.ui.delay_infos00_l.addItems(df_simi.sort_values(by='MotorSpeedSPT', ascending=False).index)
        self.ui.delay_infos01_l.addItems(df_simi.sort_values(by='Torque'       , ascending=False).index)
        self.ui.delay_infos10_l.addItems(df_simi.sort_values(by='n IdCmd'      , ascending=False).index)
        self.ui.delay_infos11_l.addItems(df_simi.sort_values(by='n IqCmd'      , ascending=False).index)

    def run_delay_function(self):

        self.ui.pdf = self.ui.pdfView_delay


        labels = [self.ui.delay_infos00_l.currentText(),
                  self.ui.delay_infos01_l.currentText(),
                  self.ui.delay_infos10_l.currentText(),
                  self.ui.delay_infos11_l.currentText()]
        
        path = self.ui.delay_qline_files.text().replace("\"", '')

        self.DC = DelayComp(path, channel_list=labels, imag1=int(self.ui.delay_infos20_l.currentText()), imag2=int(self.ui.delay_infos21_l.currentText()))
        self.DC.delayComp()

        model = PandasModel(self.DC.data_results)

        self.ui.delay_view.setModel(model)

        save_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_dec.pdf'

        pdf = self.DC.export_as_pdf(plots=None, titles=None, legend=None, bbox=None)
        pdf.output(save_path)

        self.ui.m_document_delay.load(save_path)



    def delay_actionZoom_In_function(self):

        factor = self.ui.pdfView_delay.zoomFactor() * 2
        self.ui.pdfView_delay.setZoomFactor(factor)

    
    def delay_actionZoom_Out_function(self):

        factor = self.ui.pdfView_delay.zoomFactor() / 2
        self.ui.pdfView_delay.setZoomFactor(factor)

    def delay_actionPage_down_function(self):

        nav = self.ui.pdfView_delay.pageNavigator()
        nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    def delay_actionPage_up_function(self):

        nav = self.ui.pdfView_delay.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())

    def actionSave_delay_function(self):

        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        file_path  = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_dec.pdf'

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.pdf);;All files(*.*)")
        save_path    = save_path.split('.')[0]

        self.DC.data_results.to_excel(save_path + '_results.xlsx')
        self.DC.data_results_abs.to_excel(save_path + '_abs_results.xlsx')

        shutil.copyfile(file_path, save_path + '.pdf')

        print(save_path)




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                    DELAY  INCA                                                                 ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def delay_inca_sf_button_function(self):

        self.file_names_delay_inca = QFileDialog.getExistingDirectory(self, "Open Directory", "/home", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)

        print(self.file_names_delay_inca)

        self.ui.delay_inca_qline_files.setText(self.file_names_delay_inca)


    def delay_inca_read_file_button_function(self):

        # path = self.ui.delay_inca_qline_files.text().replace("\"", '')

        # with open(path, "r") as f:
        #     lines, skiprows = f.readlines(), []
        #     for idx, line in enumerate(lines[1:]):
        #         try:
        #             int(line.split(',')[1])
        #         except:
        #             skiprows.append(idx+1)

        # data = pd.read_csv(path, skiprows=skiprows)

        # df_simi = word_similarity(data)

        # self.ui.delay_inca_infos00_l.addItems(df_simi.sort_values(by='MotorSpeedSPT', ascending=False).index)
        # self.ui.delay_inca_infos01_l.addItems(df_simi.sort_values(by='Torque'       , ascending=False).index)
        # self.ui.delay_inca_infos10_l.addItems(df_simi.sort_values(by='n IdCmd'      , ascending=False).index)
        # self.ui.delay_inca_infos11_l.addItems(df_simi.sort_values(by='n IqCmd'      , ascending=False).index)

        pass

    def run_delay_inca_function(self):

        self.ui.pdf = self.ui.pdfView_delay_inca


        labels = [self.ui.delay_inca_infos00_l.text(),
                  self.ui.delay_inca_infos01_l.text(),
                  self.ui.delay_inca_infos10_l.text(),
                  self.ui.delay_inca_infos11_l.text(),
                  self.ui.delay_inca_infos20_l.text(),
                  self.ui.delay_inca_infos21_l.text()]
        
        path = self.ui.delay_inca_qline_files.text().replace("\"", '')

        self.DCI = DelayCompINCA(path, labels)
        self.DCI.delay_comp_process()

        model = PandasModel(self.DCI.excel)
        self.ui.delay_inca_view.setModel(model)

        save_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_dec_inca.pdf'

        pdf = self.DCI.export_as_pdf(plots=None, titles=None, legend=None, bbox=None)
        pdf.output(save_path)

        self.ui.m_document_delay_inca.load(save_path)



    def delay_inca_actionZoom_In_function(self):
        factor = self.ui.pdfView_delay_inca.zoomFactor() * 2
        self.ui.pdfView_delay_inca.setZoomFactor(factor)

    
    def delay_inca_actionZoom_Out_function(self):
        factor = self.ui.pdfView_delay_inca.zoomFactor() / 2
        self.ui.pdfView_delay_inca.setZoomFactor(factor)

    def delay_inca_actionPage_down_function(self):
        nav = self.ui.pdfView_delay_inca.pageNavigator()
        nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    def delay_inca_actionPage_up_function(self):
        nav = self.ui.pdfView_delay_inca.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())

    def actionSave_delay_inca_function(self):

        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        file_path  = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_dec_inca.pdf'

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.pdf);;All files(*.*)")
        save_path    = save_path.split('.')[0]

        self.DCI.excel.to_excel(save_path + '_results.xlsx')

        shutil.copyfile(file_path, save_path + '.pdf')

        print(save_path)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                      IDIQ                                                                      ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def idq_sf_button_function(self):

        self.file_names_delay, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Files (*.xlsx *.csv *.dat);;All files(*.*)")

        file_str = ''
        for idx, f in enumerate(self.file_names_delay):
            file_str += '\"' + f + '\"'

            if idx != len(self.file_names_delay)-1:
                file_str += ', '

        self.ui.idq_qline_files.setText(file_str)


    def idq_read_file_button_function(self):

        path = self.ui.idq_qline_files.text().replace("\"", '')

        with open(path, "r") as f:
            lines, skiprows = f.readlines(), []
            for idx, line in enumerate(lines[1:]):
                try:
                    int(line.split(',')[1])
                except:
                    skiprows.append(idx+1)

        if '.xlsx' in path: data = pd.read_excel(path)
        if '.csv'  in path: data = pd.read_csv(path)
        if '.dat'  in path: data = pd.read_csv(path)

        df_simi = word_similarity(data)

        self.ui.idq_infos00_l.addItems(df_simi.sort_values(by='MotorSpeedSPT', ascending=False).index)
        self.ui.idq_infos01_l.addItems(df_simi.sort_values(by='Torque'       , ascending=False).index)
        self.ui.idq_infos10_l.addItems(df_simi.sort_values(by='n IdCmd'      , ascending=False).index)
        self.ui.idq_infos11_l.addItems(df_simi.sort_values(by='n IqCmd'      , ascending=False).index)
        self.ui.idq_infos20_l.addItems(df_simi.sort_values(by='n IdFB'       , ascending=False).index)
        self.ui.idq_infos21_l.addItems(df_simi.sort_values(by='n IqFB'       , ascending=False).index)
        self.ui.idq_infos30_l.addItems(df_simi.sort_values(by='n UdFB'       , ascending=False).index)
        self.ui.idq_infos31_l.addItems(df_simi.sort_values(by='n UqFB'       , ascending=False).index)
        self.ui.idq_infos40_l.addItems(df_simi.sort_values(by='n ModIndex'   , ascending=False).index)
        self.ui.idq_infos41_l.addItems(df_simi.sort_values(by='n Vdc'        , ascending=False).index)

        self.PCAS = ProcessCurrentAngleSweep(path)
        

    def run_idq_function(self):

        self.data = self.PCAS.process_pipeline(motorspeed = self.ui.idq_infos00_l.currentText(),
                                               torque     = self.ui.idq_infos01_l.currentText(),
                                               idcmd      = self.ui.idq_infos10_l.currentText(),
                                               iqcmd      = self.ui.idq_infos11_l.currentText(),
                                               idfb       = self.ui.idq_infos20_l.currentText(),
                                               iqfb       = self.ui.idq_infos21_l.currentText(),
                                               udfb       = self.ui.idq_infos30_l.currentText(),
                                               uqfb       = self.ui.idq_infos31_l.currentText(),
                                               modindex   = self.ui.idq_infos40_l.currentText(),
                                               vdc        = self.ui.idq_infos41_l.currentText())


        out_data      = self.PCAS.gerate_reports(self.data, var_ref='TqFB_rnd')
        graphs, title = self.PCAS.graphs_to_pdf(out_data)
        fig, bbox     = self.PCAS.legend(out_data)


        PDF = GeneratePDF_IDQ()
        pdf = PDF.export_as_pdf(graphs, title, fig, bbox)

        model = PandasModel(out_data)
        self.ui.idq_view.setModel(model)

        save_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_idq.pdf'
        pdf.output(save_path)

        self.ui.m_document_idq.load(save_path)

    def actionSave_idq_function(self):

        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        file_path  = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_idq.pdf'

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.pdf);;All files(*.*)")
        save_path = save_path.split('.')[0]

        shutil.copyfile(file_path, save_path + '.pdf')

        self.PCAS.out_df.to_excel(save_path + '_results.xlsx')


    def idq_actionZoom_In_function(self):
        factor = self.ui.pdfView_idq.zoomFactor() * 2
        self.ui.pdfView_idq.setZoomFactor(factor)

    
    def idq_actionZoom_Out_function(self):
        factor = self.ui.pdfView_idq.zoomFactor() / 2
        self.ui.pdfView_idq.setZoomFactor(factor)

    def idq_actionPage_down_function(self):
        nav = self.ui.pdfView_idq.pageNavigator()
        nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    def idq_actionPage_up_function(self):
        nav = self.ui.pdfView_idq.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                    IDIQ INCA                                                                   ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                      TEMP                                                                      ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def tem_sf_button_function(self):

        self.file_names_temp, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Files (*.xlsx *.csv *.dat);;All files(*.*)")

        file_str = ''
        for idx, f in enumerate(self.file_names_temp):
            file_str += '\"' + f + '\"'

            if idx != len(self.file_names_temp)-1:
                file_str += ', '

        self.ui.temp_qline_files.setText(file_str)

    def tem_sf_button_2_function(self):

        self.file_names_temp, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Files (*.xlsx *.csv *.dat);;All files(*.*)")

        file_str = ''
        for idx, f in enumerate(self.file_names_temp):
            file_str += '\"' + f + '\"'

            if idx != len(self.file_names_temp)-1:
                file_str += ', '

        self.ui.temp_qline_2_files.setText(file_str)

    def run_temp_function(self):

        motor                    = self.ui.temp_qline_files.text().replace('\"', '')
        regen                    = self.ui.temp_qline_files.text().replace('\"', '')
        volt_breakpoints         = [int(t) for t in self.ui.temp_infos00_l.text().split(',')]
        corner_speeds            = [int(t) for t in self.ui.temp_infos01_l.text().split(',')]
        max_volt                 = int(self.ui.temp_infos10_l.text())
        back_emf_cte             = float(self.ui.temp_infos11_l.text())
        peak_trq                 = int(self.ui.temp_infos20_l.text())
        continous_trq_target     = int(self.ui.temp_infos21_l.text())
        corner_speed_at_max_volt = int(self.ui.temp_infos30_l.text())
        rpm_step                 = int(self.ui.temp_infos31_l.text())
        rpm_begin                = int(self.ui.temp_infos40_l.text())
        rpm_end                  = int(self.ui.temp_infos41_l.text())
        trq_breakpoints          = [int(t) for t in self.ui.temp_infos50_l.text().split(',')]

        print(motor)

        BG = BigGridVerifyPrerequisiteData(motor = motor,
                                           regen = regen,
                                           volt_breakpoints = volt_breakpoints,
                                           corner_speeds = corner_speeds,
                                           max_volt = max_volt,
                                           back_emf_cte = back_emf_cte,
                                           peak_trq = peak_trq,
                                           continous_trq_target = continous_trq_target,
                                           corner_speed_at_max_volt = corner_speed_at_max_volt)
        
        BG.generate_excel(RPM_breakpoints = [rpm_step*i for i in range(int(rpm_begin/rpm_step), int(rpm_end/rpm_step)+1)],
                          trq_breakpoints = trq_breakpoints,
                          filename        = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_temp.xlsx'
                           )
        
        df = pd.read_excel(shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_temp.xlsx', 'Prerequisite Data')

        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.ui.temp_view.setRowCount(df.shape[0])
        self.ui.temp_view.setColumnCount(df.shape[1])
        self.ui.temp_view.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.ui.temp_view.setItem(row[0], col_index, tableItem)

        self.ui.temp_view.setColumnWidth(2, 300)


        # print(self.ui.temp_infos00_l.text())




# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///                                                                                                                                                ///
# ///                                                                       DDI                                                                      ///
# ///                                                                                                                                                ///
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    def ddi_search_file_button_function(self): 

        self.file_data_match = QFileDialog.getExistingDirectory(self, "Select directory", "/home") + '/'
        self.ui.ddi_qline_files.setText(self.file_data_match)


    def ddi_read_file_button_function(self):

        print(self.ui.ddi_qline_files.text())

        self.files = [self.ui.ddi_qline_files.text() + f for f in os.listdir(self.ui.ddi_qline_files.text())]
        dates = [f.split('_')[0] for f in os.listdir(self.ui.ddi_qline_files.text())]
        dates = [d.split('-') for d in dates]
        self.dates = [d[0]+'/'+d[1]+'/'+d[2]+' '+d[3]+':'+d[4]+'' for d in dates]
        print(dates)

        actual_data_match = self.data_match_df[[self.ui.ddi_combo_ptc.currentText(), 'BASE']]
        actual_data_match = actual_data_match.dropna().reset_index(drop=True)
        data_match        = {v:k for k, v in zip(actual_data_match[self.ui.ddi_combo_ptc.currentText()], actual_data_match['BASE'])}

        print(data_match)

        data   = pd.read_csv(self.files[0])
        df_simi = word_similarity_ddi(data, list(data_match.values()))

        self.ui.ddi_infos00_l.addItems(df_simi.sort_values(by=data_match['Back-Emf'], ascending=False).index)
        self.ui.ddi_infos01_l.addItems(df_simi.sort_values(by=data_match['Speed'], ascending=False).index)
        self.ui.ddi_infos02_l.addItems(df_simi.sort_values(by=data_match['Drag Torque'], ascending=False).index)

        self.ui.ddi_infos10_l.addItems(df_simi.sort_values(by=data_match['Vibration_1'], ascending=False).index)
        self.ui.ddi_infos11_l.addItems(df_simi.sort_values(by=data_match['Vibration_2'], ascending=False).index)
        self.ui.ddi_infos12_l.addItems(df_simi.sort_values(by=data_match['Vibration_3'], ascending=False).index)
        # self.ui.ddi_infos13_l.addItems(df_simi.sort_values(by=data_match['Vibration_4'], ascending=False).index)

        self.ui.ddi_infos20_l.addItems(df_simi.sort_values(by=data_match['Vibration_4'], ascending=False).index)
        self.ui.ddi_infos21_l.addItems(df_simi.sort_values(by=data_match['Vibration_5'], ascending=False).index)
        self.ui.ddi_infos22_l.addItems(df_simi.sort_values(by=data_match['Vibration_6'], ascending=False).index)
        # self.ui.ddi_infos23_l.addItems(df_simi.sort_values(by=data_match['Vibration_8'], ascending=False).index)

        vol_types = ['Vrms_lineline/mech_rpm',
                     'Vpk_lineline/mech_rpm',
                    'Vpk_phase/mech_rpm',
                    'Vpk_phase/mech_radps',
                    'Vpk_phase/elec_radps',
                    'Vrms_phase/elec_radps']

        self.ui.ddi_infos_actual_l.addItems(vol_types)
        self.ui.ddi_infos_target_l.addItems(vol_types)

        


    def run_ddi_function(self):

        vibr = [self.ui.ddi_infos10_l.currentText(), self.ui.ddi_infos11_l.currentText(), self.ui.ddi_infos12_l.currentText(), 
                self.ui.ddi_infos20_l.currentText(), self.ui.ddi_infos21_l.currentText(), self.ui.ddi_infos22_l.currentText()]

        DDI = DailyDataIntegrity(self.files, self.dates, 
                                 self.ui.ddi_infos00_l.currentText(), 
                                 vibr, 
                                 self.ui.ddi_infos02_l.currentText(), 
                                 self.ui.ddi_infos01_l.currentText(),
                                 self.ui.ddi_infos_actual_l.currentText(), 
                                 self.ui.ddi_infos_target_l.currentText())
        DDI.fit()


        PDF = DDI_PDFGenerator(name='DDI', fig=DDI.infos)
        pdf = PDF.fit()
        save_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_ddi.pdf'
        pdf.output(save_path) 


        self.ui.m_document_ddi.load(save_path)

    def actionSave_ddi_function(self):

        start_path = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/')
        file_path  = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0).replace('\\', '/') + '/temp_ddi.pdf'

        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", start_path, "Files (*.pdf);;All files(*.*)")
        save_path    = save_path.split('.')[0]

        shutil.copyfile(file_path, save_path + '.pdf')

        # print(save_path.split('/')[:-1])

        # n = ''
        # for a in save_path.split('/')[:-1]:
        #     n += a + '/'

        # self.DP.excel(n, names=[path.split('/')[-1].split('.')[0] for path in self.file_names_dvp])


    def actionZoom_In_ddi_function(self):

        factor = self.ui.pdfView_ddi.zoomFactor() * 2
        self.ui.pdfView_ddi.setZoomFactor(factor)

    
    def actionZoom_Out_ddi_function(self):

        factor = self.ui.pdfView_ddi.zoomFactor() / 2
        self.ui.pdfView_ddi.setZoomFactor(factor)

    def actionPage_down_ddi_function(self):

        nav = self.ui.pdfView_ddi.pageNavigator()
        nav.jump(nav.currentPage() - 1, QPoint(), nav.currentZoom())

    def actionPage_up_ddi_function(self):

        nav = self.ui.pdfView_ddi.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())



    def ddi_search_data_match_ddi_function(self): 

        self.file_data_match_ddi, _ = QFileDialog.getOpenFileNames(self, "Open File", "/home", "Excel (*.xlsx);;All files(*.*)")

        file_str = ''
        for idx, f in enumerate(self.file_data_match_ddi):
            file_str += '\"' + f + '\"'

            if idx != len(self.file_data_match_ddi)-1: file_str += ', '

        self.ui.data_match_ddi_qline_files.setText(file_str)

    def data_match_ddi_read_file_button_function(self):

        print(self.file_data_match_ddi) 
        print(self.ui.ddi_combo_ptc.currentText())

        self.data_match_df = pd.read_excel(self.file_data_match_ddi[0], sheet_name='DDI DataMatch')
        self.ui.ddi_combo_ptc.clear()
        self.ui.ddi_combo_ptc.addItems(self.data_match_df.drop('BASE', axis=1).columns)

        


    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # MAXIMIZE/RESTORE
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # IMPORT THEMES FILES QSS/CSS
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # START - GUI DEFINITIONS
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if True:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if GLOBAL_STATE:
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if True:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # TOGGLE MENU
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = 210
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # /////////////////////////////////////////////////////////////////////////////////////////////////
    # SELECT/DESELECT MENU

    # SELECT
    def selectMenu(getStyle):
        MENU_SELECTED_STYLESHEET = """
                border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
                background-color: rgb(40, 44, 52);
                """
        
        select = getStyle + MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        MENU_SELECTED_STYLESHEET = """
                border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
                background-color: rgb(40, 44, 52);
                """
        
        deselect = getStyle.replace(MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))
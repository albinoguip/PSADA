import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import colorcet as cc

class PlotterMainStatic():

    def __init__(self, path=None, ui=None, plot=None, selectplot=None, variable_y=None, variable_x = None, variable_z = None ,df=None):
        
        self.plot = plot
        self.ui = ui
        self.pathtosave = ''
        self.path = path #Toma como parametro o path do arquivo
        self.selectplot = selectplot #Toma como parametro o tipo de plot como string: "Lineplot" e "Boxplot"
        self.variable_y = variable_y
        self.variable_x = variable_x
        self.variable_z = variable_z

        plt.rcParams["font.family"] = "Times New Roman"
        self.paletadcolor = sns.color_palette()
        self.intense_palette = sns.color_palette(cc.glasbey, n_colors=12)  # You can adjust the number of colors as

        print(self.plot)
        print(self.path)
        print(self.selectplot)
        print(self.variable_y)
        # self.readData()
        # self.handeldataplot()



    def update(self):

        self.ui.STATIC_sc.axes.cla()
        self.ui.STATIC_sc.fig.clf()

        self.ui.STATIC_sc.axes = self.ui.STATIC_sc.fig.add_subplot(111)

        # print('entrei no update')
        self.readData()
        self.handeldataplot()

        # self.ui.STATIC_sc.axes.grid(True)

        # # temp = self.data.copy()


        # # Plot the data
        # self.handeldataplot()

        # elif self.plot['plot'] == 'Line':
        #     self.line(temp, self.plot, self.ui) 

        # elif self.plot['plot'] == 'Boxplot':
        #     self.boxplot(temp, self.plot, self.ui, self.labels, self.title, self.xlabel, self.ylabel, self.limites, self.vert, self.rotation, self.text, self.nbarra)   


        # Features

        # self.ui.STATIC_sc.axes.set_xlabel(self.plot['x_label'] if self.plot['x_label'] is not None else self.plot['x'])
        # self.ui.STATIC_sc.axes.set_ylabel(self.plot['y_label'] if self.plot['y_label'] is not None else self.plot['y'])

        # if self.plot['plot'] == 'Line':
        #     unique_y = temp[self.plot['y']].unique()

        #     try:
        #         if np.array_equal(temp[self.plot['y']], temp[self.plot['y']].astype(int)) and len(unique_y) <= 30:            
        #             self.ui.STATIC_sc.axes.set_yticks([i for i in unique_y], [i for i in unique_y])       
        #     except:
        #         pass         

        
        #     y, x, c = self.plot['y'], self.plot['x'], self.plot['c']

        #     if self.plot['c'] is not None and self.plot['c'] != '':
        #         self.ui.STATIC_sc.axes.set_title(f'{y} x {x} per {c}')
        #     else:
        #         self.ui.STATIC_sc.axes.set_title(f'{y} x {x}')


        self.ui.STATIC_sc.figure.tight_layout()
        self.ui.STATIC_sc.draw()



    def readData (self):
        self.df = pd.read_csv(self.path)
        self.selectdata = self.path.split('/')[-1].replace('.csv', '')
        # print(self.selectdata)



    def handeldataplot (self):

        # print('entrei no handle')

        if 'Df_ger' in self.selectdata or 'Df_nt' in self.selectdata:


            def boxplot_barrasGeracao(Df_VF, groupflag):

                if groupflag:
                    grouped_Reg = Df_VF.groupby('REG').agg({'BUS_ID': 'unique', 'MODV_PU': list})
                    data_Reg = [grouped_Reg.at[region, 'MODV_PU'] for region in ['Norte', 'Nordeste', 'Sudeste-Centro-Oeste', 'Sul', 'AC-RO']]
                    Nbarras_Reg = [grouped_Reg.at[region, 'BUS_ID'] for region in ['Norte', 'Nordeste', 'Sudeste-Centro-Oeste', 'Sul', 'AC-RO']]
                    labels_Reg = ['North', 'Northeast', 'SE-CW', 'South', 'AC-RO']
                    self.plot_boxplot(data_Reg, labels_Reg, 'Bus Voltage Distribution by Region for PV Buses', 'Region', 'Voltage (pu)', text=True, nbarra=Nbarras_Reg, pathtosave=None)
                else:
                    grouped_UF = Df_VF.groupby('Gen_Type').agg({'BUS_ID': 'unique', 'MODV_PU': list})
                    data_UF = [grouped_UF.at[gen_type, 'MODV_PU'] for gen_type in ['UHE', 'UTE', 'PCH', 'EOL', 'UFV', 'BIO','SIN']]
                    Nbarras_UF = [grouped_UF.at[gen_type, 'BUS_ID'] for gen_type in ['UHE', 'UTE', 'PCH', 'EOL', 'UFV', 'BIO','SIN']]
                    labels_UF = ['Hydro', 'Thermal', 'SHP', 'Wind', 'Solar', 'Bio','Sync. Comp']
                    self.plot_boxplot(data_UF, labels_UF, 'Bus Voltage Distribution by Type of Generation','Type of Generation', 'Voltage (pu)', text=True, nbarra=Nbarras_UF,pathtosave=None)

            def boxplot_barrasCarga(Df_Vfpt, groupflag):

                if groupflag:
                    grouped_Reg = Df_Vfpt.groupby('REG').agg({'BUS_ID': 'unique', 'MODV_PU': list})
                    data_Reg = [grouped_Reg.at[region, 'MODV_PU'] for region in ['Norte', 'Nordeste', 'Sudeste-Centro-Oeste', 'Sul', 'AC-RO']]
                    Nbarras_Reg = [grouped_Reg.at[region, 'BUS_ID'] for region in ['Norte', 'Nordeste', 'Sudeste-Centro-Oeste', 'Sul', 'AC-RO']]
                    labels_Reg = ['North', 'Northeast', 'SE-CW', 'South', 'AC-RO']
                    self.plot_boxplot(data_Reg, labels_Reg, 'Bus Voltage Distribution by Region for PQ Buses', 'Region', 'Voltage (pu)', text=True, nbarra=Nbarras_Reg, pathtosave=None)
                else:
                    grouped_VBASEKV = Df_Vfpt.groupby('VBASEKV').agg({'BUS_ID': 'unique', 'MODV_PU': list})
                    voltage_levels = [230, 345, 440, 500, 525, 765]
                    data_VBASEKV = [grouped_VBASEKV.at[level, 'MODV_PU'] for level in voltage_levels]
                    Nbarras_VBASEKV = [grouped_VBASEKV.at[level, 'BUS_ID'] for level in voltage_levels]
                    labels_VBASEKV = ['230', '345', '440', '500', '525', '765']
                    self.plot_boxplot(data_VBASEKV, labels_VBASEKV, 'Bus Voltage Distribution by Voltage Level', 'Voltage Level (kV)', 'Voltage (pu)', text=True, nbarra=Nbarras_VBASEKV, pathtosave=None)

            # PARAMETROS A SER ESCOLHIDOS NA INTERFAZ ANTES DE PLOTAS ***
            # self.groupbyreg = False  # parametro que agrupa por região se for TRUE, se for FALSE agrupa por tipo de barra
            self.groupbyreg = self.plot['groupbyreg']

            # print('acessei aqui no boxplot')
            # print(self.selectplot)
            # print(self.selectdata)

            if self.selectplot == 'Boxplot':
                if self.selectdata == 'Df_ger':
                    boxplot_barrasGeracao(self.df, self.groupbyreg) 
                else: # Caso a data venha de Df_nt
                    boxplot_barrasCarga(self.df, self.groupbyreg)               

        elif 'Df_PQ_DPI_S1' in self.selectdata or 'Df_PV_DPI_S1' in self.selectdata:

            # print('consegui entrar nos indices')
            self.all_sameplot  = self.plot['all same plot']
            self.REG = self.plot['region_selected']
            # self.busgroup = 230
            # self.busgroup = int(self.plot['checked_voltages'])
            # self.busgroup = [int(item) for item in self.plot['checked_voltages']]
            self.busgroup = [int(item) for item in self.plot['checked_voltages']] if 'Df_PQ_DPI_S1' in self.selectdata else self.plot['checked_voltages']

            print(self.busgroup)

            if self.selectdata == 'Df_PQ_DPI_S1':
                BusGroup = 'VBASEKV'
            else:
                BusGroup = 'Gen_Type'

            y_var = self.plot['y']
            df = self.df.set_index(['Dia','Hora','REG',BusGroup])


            if self.selectplot == 'Line':
                if self.all_sameplot:
                    self.plot_line(df.loc[:,:, self.REG, :], y_var, 'Pontos de Operação', '(p.u)', f'{y_var} para {self.REG}', '', byClass = True, clase=BusGroup, order=False, month = False)
                else:
                    self.plot_line(df.loc[:,:,self.REG, :], y_var, 'Pontos de Operação', '(p.u)', f'{y_var} por Região - {self.REG}/{str(self.busgroup)}', '', order=False, month = False, busgroup=self.busgroup)

            elif self.selectplot == 'Persistence Curve':
                if self.all_sameplot:
                    self.plot_line(df.loc[:,:, self.REG, :], y_var, 'Porcentagem de meias horas em um mês (%)', '(p.u)', f'{y_var} para {self.REG}', '',  byClass = True, clase=BusGroup, order=True, month = False)
                else:
                    self.plot_line(df.loc[:,:,self.REG, :], y_var, 'Porcentagem de meias horas em um mês (%)', '(p.u)', f'{y_var} por Região - {self.REG}/{str(self.busgroup)}', '', order=True, month = False, busgroup=self.busgroup)

        elif 'Df_DPI_S2' in self.selectdata:

            self.all_sameplot  = self.plot['all same plot']
            self.REG = self.plot['checked_voltages']
            self.BusType = 'PQ' if 'PQ' in self.plot['region_selected'] else 'PV'
            y_var = self.plot['y']
            print(y_var)

            df = self.df.set_index(['level_0','Dia','Hora','REG'])

            if self.selectplot == 'Line':
                if self.all_sameplot:
                    self.plot_line(df.loc[f'DPI_{self.BusType}',:,:,:], y_var, 'Pontos de Operação', '(p.u)', f'{y_var} por Região', '', byClass = True, clase='REG', order=False, month = False)
                else:
                    self.plot_line(df.loc[f'DPI_{self.BusType}',:,:,:], y_var, 'Pontos de Operação', '(p.u)', f'{y_var} por Região - {self.REG}', '', order=False, month = False, busgroup=self.REG)

            elif self.selectplot == 'Persistence Curve':
                if self.all_sameplot:
                    self.plot_line(df.loc[f'DPI_{self.BusType}',:,:,:], y_var, 'Porcentagem de meias horas em um mês (%)', '(p.u)', f'{y_var} por Região', '',  byClass = True, clase='REG', order=True, month = False)
                else:
                    self.plot_line(df.loc[f'DPI_{self.BusType}',:,:,:], y_var, 'Porcentagem de meias horas em um mês (%)', '(p.u)', f'{y_var} por Região - {self.REG}', '', order=True, month = False, busgroup=self.REG)

        elif 'Df_DPI_S3' in self.selectdata or 'Df_DPI_S4' in self.selectdata:
        
            # y_var = self.variable_y
            y_var = self.plot['y']
            df = self.df

            if self.selectplot == 'Line':
                self.plot_line(df, y_var, 'Pontos de Operação', '(p.u)', f'{y_var} por Ponto de Operação', '', order=False, month = False, S3_or_S4=True)
            elif self.selectplot == 'Persistence Curve':
                self.plot_line(df, y_var, 'Porcentagem de meias horas em um mês (%)', '(p.u)', f'{y_var}', '', order=True, month = False, S3_or_S4=True)
                 
        elif 'DF_POT_Reg' in self.selectdata or 'Df_Reserva_REG_MW' in self.selectdata:

            self.all_sameplot  = self.plot['all same plot']
            self.REG = self.plot['checked_voltages']
            y_var = self.plot['y']

            df = self.df.set_index(['Dia','Hora','REG'])

            if self.selectplot == 'Line':
                if self.all_sameplot:
                    self.plot_line(df, y_var, 'Pontos de Operação', '(MW)', f'{y_var} por Região', '', byClass = True, clase='REG', order=False, month = False)
                else:
                    self.plot_line(df.loc[:,:,:], y_var, 'Pontos de Operação', '(MW)', f'{y_var} por Região - {self.REG}', '', order=False, month = False, busgroup=self.REG)

            elif self.selectplot == 'Persistence Curve':
                if self.all_sameplot:
                    self.plot_line(df, y_var, 'Porcentagem de meias horas em um mês (%)', '(MW)', f'{y_var} por Região', '', byClass = True, clase='REG', order=True, month = False)
                else:
                    self.plot_line(df.loc[:,:,:], y_var, 'Porcentagem de meias horas em um mês (%)', '(MW)', f'{y_var} por Região - {self.REG}', '', order=True, month = False, busgroup=self.REG)

        elif 'Df_MW-MVAR_PO' in self.selectdata or 'Df_Reserva_PO_MW' in self.selectdata:

            # y_var = self.variable_y
            y_var = self.plot['y']
            df = self.df
            
            if self.selectplot == 'Line':
                self.plot_line(df, y_var, 'Pontos de Operação', '(MW)', f'{y_var} por Ponto de Operação', '', order=False, month = False, S3_or_S4=True)
            elif self.selectplot == 'Persistence Curve':
                self.plot_line(df, y_var, 'Porcentagem de meias horas em um mês (%)', '(MW)', f'{y_var}', '', order=True, month = False, S3_or_S4=True)

    def plot_line (self, df_data, column, xlbl, ylbl, title, pathsave = None, clase=None, xlimites=None, ylimites=None, order = False, byClass = False, month = False, busgroup=None, S3_or_S4=False):

        # fig, axs = plt.subplots(1, 1, figsize=(20, 10), sharex=False)

        if byClass:
            for idx, clase in enumerate(df_data.index.get_level_values(clase).unique().values):
                if order:
                    data = df_data.loc[:, :, clase].sort_values(column, ascending=False)
                    self.ui.STATIC_sc.axes.plot(data[column].values, color=self.intense_palette[idx], label=clase, lw=2.5, linestyle='-', alpha=1)
                    num = data.shape[0]
                    data_points_xaxis = 10
                    num_days = num*data_points_xaxis/100
                    self.ui.STATIC_sc.axes.set_xticks([round(i * num_days) for i in range(data_points_xaxis+1)])
                    self.ui.STATIC_sc.axes.set_xticklabels([f'{i*10}' for i in range(data_points_xaxis+1)], fontsize=12, rotation=0, ha='center')
                else:
                    data = df_data.loc[:, :, clase]
                    self.ui.STATIC_sc.axes.plot(data['key'], data[column], color=self.intense_palette[idx], label=clase, lw=2.5, linestyle='-', alpha=1)
                    self.ui.STATIC_sc.axes.xaxis.set_major_locator(plt.MaxNLocator(data.shape[0]/48))
                self.ui.STATIC_sc.axes.legend(loc='upper right', fontsize=18)
        else:
            if not S3_or_S4:
                for idx, voltage in enumerate(busgroup):
                    if order:
                        data = df_data.loc[:, :, voltage].sort_values(column, ascending=False)
                        self.ui.STATIC_sc.axes.plot(data[column].values, color=self.intense_palette[idx % len(self.intense_palette)], label=f'{voltage}', lw=2.5, linestyle='-', alpha=1)
                        num = data.shape[0]
                        data_points_xaxis = 10
                        num_days = num*data_points_xaxis/100
                        self.ui.STATIC_sc.axes.set_xticks([round(i * num_days) for i in range(data_points_xaxis+1)])
                        self.ui.STATIC_sc.axes.set_xticklabels([f'{i*10}' for i in range(data_points_xaxis+1)], fontsize=12, rotation=0, ha='center')
                    else:
                        data = df_data.loc[:, :, voltage]
                        self.ui.STATIC_sc.axes.plot(data['key'], data[column], color=self.intense_palette[idx % len(self.intense_palette)], label=f'{voltage}', lw=2.5, linestyle='-', alpha=1)
                        self.ui.STATIC_sc.axes.xaxis.set_major_locator(plt.MaxNLocator(int(data.shape[0]/48)))
                    self.ui.STATIC_sc.axes.legend(loc='upper right', fontsize=18)
            else:
                if order:
                    data = df_data.sort_values(column, ascending=False)
                    self.ui.STATIC_sc.axes.plot(data[column].values, color=self.intense_palette[0], lw=2.5, linestyle='-', alpha=1)
                    num = data.shape[0]
                    data_points_xaxis = 10
                    num_days = num*data_points_xaxis/100
                    self.ui.STATIC_sc.axes.set_xticks([round(i * num_days) for i in range(data_points_xaxis+1)])
                    self.ui.STATIC_sc.axes.set_xticklabels([f'{i*10}' for i in range(data_points_xaxis+1)], fontsize=12, rotation=0, ha='center')
                else:
                    self.ui.STATIC_sc.axes.plot(df_data['key'], df_data[column], color=self.intense_palette[0], lw=2.5, linestyle='-', alpha=1)
                    self.ui.STATIC_sc.axes.xaxis.set_major_locator(plt.MaxNLocator(int(df_data.shape[0]/48)))

            # if order:
            #     data = df_data.sort_values(column, ascending=False)
            #     self.ui.STATIC_sc.axes.plot(data[column].values, color=self.intense_palette[0], lw=2.5, linestyle='-', alpha=1)
            #     num = data.shape[0]
            #     data_points_xaxis = 10
            #     num_days = num*data_points_xaxis/100
            #     self.ui.STATIC_sc.axes.set_xticks([round(i * num_days) for i in range(data_points_xaxis+1)])
            #     self.ui.STATIC_sc.axes.set_xticklabels([f'{i*10}' for i in range(data_points_xaxis+1)], fontsize=12, rotation=0, ha='center')
            # else:
            #     self.ui.STATIC_sc.axes.plot(df_data['key'], df_data[column], color=self.intense_palette[0], lw=2.5, linestyle='-', alpha=1)
            #     self.ui.STATIC_sc.axes.xaxis.set_major_locator(plt.MaxNLocator(28))

        self.ui.STATIC_sc.axes.tick_params(axis='y', labelsize=24)
        self.ui.STATIC_sc.axes.tick_params(axis='x', labelsize=15, rotation = 45)
        self.ui.STATIC_sc.axes.set_xlabel(xlbl, fontsize=18)
        self.ui.STATIC_sc.axes.set_ylabel(ylbl, fontsize=22)
        self.ui.STATIC_sc.axes.set_title(title, fontsize=22)
        
        if month:
            days = ['Oct {}'.format(i+1) for i in range(int(df_data.shape[0]/48))]
            self.ui.STATIC_sc.axes.set_xticks(ticks=[i*48 for i in range(int(df_data.shape[0]/48))], labels=days, rotation=45)
            self.ui.STATIC_sc.axes.set_xlabel('',fontsize=10)

        if xlimites != None:
            self.ui.STATIC_sc.axes.set_xlim(xlimites)
        if ylimites != None:
            self.ui.STATIC_sc.axes.set_ylim(ylimites)
            
        self.ui.STATIC_sc.axes.grid(True, linestyle='-', linewidth=1.2, alpha=0.4)
        # self.ui.STATIC_sc.axes.tight_layout()
        # self.ui.STATIC_sc.draw()
        # ui.STATIC_sc.axes.show()
        # nome = pathsave
        # plt.savefig(nome, bbox_inches = 'tight')
        # plt.close()

    # def plot_line(self, df_data, column, xlbl, ylbl, title, pathsave=None, clase=None, xlimites=None, ylimites=None, order=False, byClass=False, month=False):
    #     ax = self.ui.STATIC_sc.axes  # Utilize o eixo fornecido

    #     if byClass:
    #         unique_classes = df_data.index.get_level_values(clase).unique().values
    #         for idx, clase in enumerate(unique_classes):
    #             color = self.intense_palette[idx % len(self.intense_palette)]  # Utilize a paleta de cores
    #             if order:
    #                 data = df_data.loc[:, :, clase].sort_values(column, ascending=False)
    #                 ax.plot(data[column].values, color=color, label=clase, lw=2.5, linestyle='-', alpha=1)
    #                 num = data.shape[0]
    #                 data_points_xaxis = 10
    #                 num_days = num * data_points_xaxis / 100
    #                 ax.set_xticks([round(i * num_days) for i in range(data_points_xaxis+1)])
    #                 ax.set_xticklabels([f'{i*10}' for i in range(data_points_xaxis+1)], fontsize=12, rotation=0, ha='center')
    #             else:
    #                 data = df_data.loc[:, :, clase]
    #                 ax.plot(data['key'], data[column], color=color, label=clase, lw=2.5, linestyle='-', alpha=1)
    #                 ax.xaxis.set_major_locator(plt.MaxNLocator(28))
    #         ax.legend(loc='upper right', fontsize=18)
    #     else:
    #         color = self.intense_palette[0]  # Utilize a primeira cor da paleta
    #         if order:
    #             data = df_data.sort_values(column, ascending=False)
    #             ax.plot(data[column].values, color=color, lw=2.5, linestyle='-', alpha=1)
    #             num = data.shape[0]
    #             data_points_xaxis = 10
    #             num_days = num * data_points_xaxis / 100
    #             ax.set_xticks([round(i * num_days) for i in range(data_points_xaxis+1)])
    #             ax.set_xticklabels([f'{i*10}' for i in range(data_points_xaxis+1)], fontsize=12, rotation=0, ha='center')
    #         else:
    #             ax.plot(df_data['key'], df_data[column], color=color, lw=2.5, linestyle='-', alpha=1)
    #             ax.xaxis.set_major_locator(plt.MaxNLocator(28))

    #     ax.tick_params(axis='y', labelsize=24)
    #     ax.tick_params(axis='x', labelsize=15, rotation=45)
    #     ax.set_xlabel(xlbl, fontsize=18)
    #     ax.set_ylabel(ylbl, fontsize=22)
    #     ax.set_title(title, fontsize=22)

    #     if month:
    #         days = ['Oct {}'.format(i+1) for i in range(28)]
    #         ax.set_xticks(ticks=[i*48 for i in range(28)], labels=days, rotation=45)
    #         ax.set_xlabel('', fontsize=10)

    #     if xlimites is not None:
    #         ax.set_xlim(xlimites)
    #     if ylimites is not None:
    #         ax.set_ylim(ylimites)

    #     ax.grid(True, linestyle='-', linewidth=1.2, alpha=0.4)


    def plot_boxplot(self, data, labels, title, xlabel, ylabel, pathtosave = None, limites=None, vert = True, rotation = 0, text = True, nbarra = None):
        
        markerfacecolor = dict(markerfacecolor='gray', marker='o')  # El diccionario que define el color y marcador

        # fig1, axs = plt.subplots(figsize=(25, 20))
        if vert:
            self.ui.STATIC_sc.axes.boxplot(data, flierprops=markerfacecolor)
            self.ui.STATIC_sc.axes.tick_params(bottom=False, left=False)
            self.ui.STATIC_sc.axes.set_axisbelow(True)

            if text:
                for i, data_item in enumerate(data):
                    num_muestras = len(data_item)
                    if num_muestras > 0:

                        Q1 = np.quantile(data_item, q=0.25) 
                        Q3 = np.quantile(data_item, q=0.75)
                        max_value = np.quantile(data_item, q=1)
                        min_value = np.quantile(data_item, q=0)
                        IQR = Q3 - Q1
                        lower_whisker = max(min_value, Q1 - 1.5 * IQR)
                        upper_whisker = min(max_value, Q3 + 1.5 * IQR)

                        try:
                            self.ui.STATIC_sc.axes.text(i+1, np.max(data_item)+0.005, f'Buses = {nbarra[i].size} ', ha='center', va='bottom',size=15)
                            self.ui.STATIC_sc.axes.text(i+1, np.median(data_item), f' {np.mean(data_item):.3f} ', ha='center', va='bottom',size=15)
                            self.ui.STATIC_sc.axes.text(i+1.35, lower_whisker, f' {lower_whisker:.3f} ', ha='center', va='bottom',size=15)
                            self.ui.STATIC_sc.axes.text(i+1.35, upper_whisker, f' {upper_whisker:.3f} ', ha='center', va='bottom',size=15)
                        except:
                            self.ui.STATIC_sc.axes.text(i+1.35, np.mean(data_item), f'{num_muestras}', ha='center', va='bottom',size=25)
            if limites != None:
                self.ui.STATIC_sc.axes.set_ylim(limites)
            self.ui.STATIC_sc.axes.set_xticks(range(1, len(labels)+1), labels, fontsize=15)
            
        else:
            self.ui.STATIC_sc.axes.boxplot(data, vert=False, flierprops=markerfacecolor)
            if limites != None:
                self.ui.STATIC_sc.axes.set_xlim(limites)
                self.ui.STATIC_sc.axes.set_xticks(np.linspace(limites[0],limites[1],20))
            if text:
                    self.ui.STATIC_sc.axes.text(np.median(data), 1.1 , f' {np.mean(data):.3f} ', ha='center', va='bottom',size=18)

        self.ui.STATIC_sc.axes.set_xlabel(xlabel, fontsize=22)
        self.ui.STATIC_sc.axes.set_ylabel(ylabel, fontsize=22)
        self.ui.STATIC_sc.axes.set_title(title, fontsize=25)
        # self.ui.STATIC_sc.axes.set_xticks(fontsize=20, rotation = rotation)

        self.ui.STATIC_sc.axes.set_xticks(range(1, len(labels) + 1))  # Define a posição dos ticks
        self.ui.STATIC_sc.axes.set_xticklabels(labels, fontsize=20, rotation=rotation)  # Define os rótulos e formata

        # self.ui.STATIC_sc.axes.set_yticks(fontsize=25)

        # Achar o mínimo e máximo em todos os dados para o eixo Y
        flat_data = np.concatenate(data)  # Combina todas as listas de dados
        self.ui.STATIC_sc.axes.set_yticks(np.arange(min(flat_data), max(flat_data), step=0.1))  # Define os ticks no eixo Y
        self.ui.STATIC_sc.axes.set_yticklabels([f'{tick:.2f}' for tick in np.arange(min(flat_data), max(flat_data), step=0.1)], fontsize=25)
        # self.ui.STATIC_sc.axes.set_yticks(np.arange(min(data), max(data), step=0.1))  # Define as posições dos ticks no eixo Y
        # self.ui.STATIC_sc.axes.set_yticklabels([f'{tick:.2f}' for tick in np.arange(min(data), max(data), step=0.1)], fontsize=25)  # Formata os rótulos

        self.ui.STATIC_sc.axes.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
        self.ui.STATIC_sc.axes.xaxis.grid(False)
        # ui.STATIC_sc.axes.show()
        # nome = pathtosave + title + '.png'
        # plt.savefig(nome, bbox_inches = 'tight')
        # if self.svg:
        #     nome = pathtosave + title + '.svg'
        #     plt.savefig(nome)
        # plt.close()



# PlotterMainStatic('C:/Users/David/OneDrive/Documents/FERV_documentos/RESULTS/V1A1F2_rev5/StaticAnalysis/Data/Geral/Df_ger.csv','Boxplot', 'CSI_INF')
from . RST_Reader import *
import pandas as pd
import numpy as np
from itertools import product
from shutil import copy

from scipy.stats import pearsonr

from sklearn.cluster import *
from sklearn.metrics import *
from operator import itemgetter

from sklearn.linear_model import LinearRegression

pd.set_option('mode.chained_assignment', None)

class RST_Plot():

    def __init__(self, report_path, eol=None, sol=None, save_path=None):

        self.save_path = save_path
        self.data      = pd.read_csv(report_path)

        PO = []
        with open('D:/PowerSystems/Sistemas/SIN/MEDIA/PO_Indice_inseguro.txt') as f:
            for line in f:
                lin        = line.strip().replace('\'', '').replace('(', '').replace(')', '').replace(' ', '').split(',')[:2]
                day, hour  = int(lin[0]), lin[1]
                PO.append(f'D_{day}_H_{hour}')

        self.data = self.data[~self.data['OP'].isin(PO)]
 
        self.codigo   = self.data[self.data['A_RCFC'].isna()].reset_index(drop=True)
        self.estavel  = self.data[~self.data['A_RCFC'].isna()].reset_index(drop=True)
        self.instavel = self.data[self.data['A_STAB'] == 1].reset_index(drop=True)
        self.instavel = self.instavel[self.instavel['A_CODE'].isin([2, 3])].reset_index(drop=True)

        # self.instavel = self.instavel[~self.instavel['OP'].isin(['D_27_H_08-00', 'D_17_H_23-30'])].reset_index(drop=True)
        # self.instavel = self.instavel[self.instavel['A_CODE'] == 3].reset_index(drop=True)
        # self.instavel = self.instavel[self.instavel['B_STAB'] == 614].reset_index(drop=True)

        # print(self.instavel)

        horas = {'00-00', '00-30', '01-00', '01-30', '02-00', '02-30', '03-00', '03-30', '04-00', '04-30', '05-00', '05-30', '06-00', '06-30',
                 '07-00', '07-30', '08-00', '08-30', '09-00', '09-30', '10-00', '10-30', '11-00', '11-30', '12-00', '12-30', '13-00', '13-30', 
                 '14-00', '14-30', '15-00', '15-30', '16-00', '16-30', '17-00', '17-30', '18-00', '18-30', '19-00', '19-30', '20-00', '20-30',
                 '21-00', '21-30', '22-00', '22-30', '23-00', '23-30'}
        
        # print(f" +--------------------+-----------+")
        # print(f" | PONTOS DE OPERAÇÃO |   {len(self.data['OP'].unique())}    |")
        # print(f" +--------------------+-----------+")
        # print(f" | CONTINGÊNCIAS      |   {len(self.data['Contigence'].unique())}      |")
        # print(f" +--------------------+-----------+")        
        # print(f" | CENARIOS           |   {len(self.data)}   |")
        # print(f" +--------------------+-----------+")
        # print(f" | CODIGOS (6 & 8)    |   {len(self.codigo[self.codigo['A_CODE'].isin([6,8])])}       |")
        # print(f" +--------------------+-----------+")
        # print(f" | ESTÁVEIS           |   {len(self.estavel)}   |")
        # print(f" +--------------------+-----------+")
        # print(f" | INSTÁVEIS          |   {len(self.instavel)}     |")
        # print(f" +--------------------+-----------+")

        # for dia in self.data['Dia'].unique():

        #     df_dia = self.data[self.data['Dia'] == dia]

        #     # print(dia, len(df_dia['Hora'].unique()))

        #     if len(df_dia['Hora'].unique()) < 48:
        #         print(dia, horas - set(df_dia['Hora'].unique()))

        # print(len(self.data['OP'].unique()))

        # COLORS

        # colors    = ['lightsteelblue', 'royalblue', 'lightgreen', 'green', 'tan', 'darkgoldenrod', 'thistle', 'purple', 'lightcoral', 'red']
        colors    = ['royalblue', 'navy', 'lightgreen', 'green', 'tan', 'darkgoldenrod', 'thistle', 'purple', 'lightcoral', 'red']
        cmap_name = 'my_list'
        self.cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=len(colors))

        # RENOVAVEIS

        if eol is not None:
            self.demanda_eol = pd.read_csv(eol, sep=';')

        if sol is not None:
            self.demanda_sol = pd.read_csv(sol, sep=';')

        if (sol is not None) and (eol is not None):
            self.renovaveis = self.demanda_eol.merge(self.demanda_sol, on=['periodo', 'hora'], how='outer')

            self.renovaveis['Dia']  = [int(OP.split('/')[0])     for OP in self.renovaveis['periodo'].values]
            self.renovaveis['Hora'] = [OP.replace(':', '-') for OP in self.renovaveis['hora'].values]
            self.renovaveis['%MW']  = self.renovaveis[['MW_x', 'MW_y']].sum(axis=1)*100

            self.renovaveis['%MW_r']  = [round(mw, 0) for mw in self.renovaveis['%MW'].values]

            self.estavel = self.estavel.merge(self.renovaveis[['Dia', 'Hora', '%MW', '%MW_r']], on=['Dia', 'Hora'], how='left')

    # ================================================================================================================================= #

    def scatter_hist(self, x, y, ax, ax_histx, ax_histy, n_bins=20):
        # no labels
        ax_histx.tick_params(axis="x", labelbottom=False)
        ax_histy.tick_params(axis="y", labelleft=False)

        # the scatter plot:
        ax.scatter(x, y)

        # now determine nice limits by hand:
        

        xmax, xmin = np.max(np.abs(x)), np.min(np.abs(x))
        binwidth = (xmax - xmin)/n_bins
        lim_max, lim_min = (int(xmax/binwidth) + 1) * binwidth, (int(xmin/binwidth)) * binwidth
        xbins = np.arange(lim_min, lim_max + binwidth, binwidth)
        ax_histx.hist(x, bins=xbins)

        ymax, ymin = np.max(np.abs(y)), np.min(np.abs(y))
        binwidth = (ymax - ymin)/n_bins
        lim_max, lim_min = (int(ymax/binwidth) + 1) * binwidth, (int(ymin/binwidth)) * binwidth
        ybins = np.arange(lim_min, lim_max + binwidth, binwidth)
        ax_histy.hist(y, bins=ybins, orientation='horizontal')

    def scatter_hist3d(self, x, y, z, ax, ax_histx, ax_histy, n_bins=20):
        # no labels
        ax_histx.tick_params(axis="x", labelbottom=False)
        ax_histy.tick_params(axis="y", labelleft=False)

        # the scatter plot:
        points = ax.scatter(x, y, c=z, cmap=self.cmap)

        # now determine nice limits by hand:
        

        xmax, xmin = np.max(np.abs(x)), np.min(np.abs(x))
        binwidth = (xmax - xmin)/n_bins
        lim_max, lim_min = (int(xmax/binwidth) + 1) * binwidth, (int(xmin/binwidth)) * binwidth
        xbins = np.arange(lim_min, lim_max + binwidth, binwidth)
        ax_histx.hist(x, bins=xbins)

        ymax, ymin = np.max(np.abs(y)), np.min(np.abs(y))
        binwidth = (ymax - ymin)/n_bins
        lim_max, lim_min = (int(ymax/binwidth) + 1) * binwidth, (int(ymin/binwidth)) * binwidth
        ybins = np.arange(lim_min, lim_max + binwidth, binwidth)
        ax_histy.hist(y, bins=ybins, orientation='horizontal')

        return points

    # ================================================================================================================================= #

    def _fix(self, x, y, _x='A', _y='A'):
        
        xkey, ykey = x['key'].values, y['key'].values

        x = x[x['key'].isin(xkey)].reset_index(drop=True).rename(columns={_x:'x'})
        y = y[y['key'].isin(ykey)].reset_index(drop=True).rename(columns={_y:'y'})

        data = x[['key', 'x']].merge(y[['key', 'y']], on='key', how='inner')

        return data['x'].values, data['y'].values











''' 
*****************************************************************************************************************************************************************

    RST_Plot_instavel -> RST_Plot
    
*****************************************************************************************************************************************************************
''' 


class RST_Plot_nao(RST_Plot):

    # ===================================================================================================================================================== #

    def plot_inst_days_hours(self, show=False):

        print(self.data_c)

        inst      = self.data_c[self.data_c['SIGLA'] == 'CODE']
        inst['A'] = 1
        inst = inst.groupby(['Day', 'Day_int', 'Hour'])['A'].sum().reset_index(drop=False)
        inst = inst.sort_values(by=['Hour', 'Day_int'])

        x, y, z = inst['Hour'], inst['Day_int'], inst['A']

        plt.figure(figsize=(14, 6))

        points = plt.scatter(x, y, c=z, s=110, cmap=self.cmap)

        plt.colorbar(points, ticks=[i*5 for i in range(1, 11)])
        plt.xticks(rotation=75)
        plt.yticks([i for i in range(1, 29)], [str(i) for i in range(1, 29)])
        plt.title('Numero de Contingências com Código 6 e 8')
        plt.xlabel('Hora')
        plt.ylabel('Dia')

        # plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        plt.savefig(self.save_path + 'plot_inst_days_hours_6e8.png', bbox_inches="tight", dpi=300)













''' 
*****************************************************************************************************************************************************************

    RST_Plot_instavel -> RST_Plot
    
*****************************************************************************************************************************************************************
''' 


class RST_Plot_instavel(RST_Plot):

    def infos(self, bus_info, gen_info):

        # inst = self.instavel[['OP', 'Contigence', 'A_STAB', 'B_STAB']].sort_values(by='OP', ascending=False)
        # inst = inst[inst['B_STAB'].isin([253, 614])].reset_index(drop=True)
        # inst = inst[inst['Contigence'] == 13].reset_index(drop=True)
        # print(gen_info.columns)

        # gen_info = gen_info.astype({'PMAX_MW':'float'})
        # gen_info = gen_info.groupby(['BUS_ID'])['PMAX_MW'].sum().reset_index(drop=False)


        # teste = inst.groupby(['OP', 'Contigence', 'B_STAB']).count().reset_index(drop=False) #.rename(columns={'OP':'Count', 'B_STAB':'BUS_ID'})
        # teste = inst[['OP', 'Contigence', 'B_STAB']].drop_duplicates().reset_index(drop=True).rename(columns={'B_STAB':'BUS_ID'})
        # teste = teste.merge(bus_info[['BUS_ID', 'BUS_NAME']], on='BUS_ID', how='left').reset_index(drop=True)
        # teste = teste.merge(gen_info[['BUS_ID', 'PMAX_MW']], on='BUS_ID', how='left').sort_values(by='PMAX_MW', ascending=False).reset_index(drop=True)
        # teste = teste[['BUS_ID', 'BUS_NAME', 'Count', 'PMAX_MW']]

        # for file in self.instavel[['OP', 'Contigence']]['OP'].unique():

        #     PATH_S = 'Data/PTOPER_A2V2F2_rev4/NTWS/'
        #     PATH_D = 'Data/PTOPER_A2V2F2_rev4/TESTE/'
        #     PATR_S = 'Data/PTOPER_A2V2F2_rev4/RST/'
        #     PATR_D = 'Data/PTOPER_A2V2F2_rev4/TESTE/RST/'

            
        #     copy(PATH_S + file + '.ntw', PATH_D + file + '.ntw')
        #     copy(PATR_S + file.replace('D', 'Dia').replace('_H_', '_') + '.rst', PATR_D + file.replace('D', 'Dia').replace('_H_', '_')  + '.rst')

        # print(self.instavel[['OP', 'Contigence']]) #['OP'].unique()

        inst           = self.instavel[['OP', 'Contigence', 'B_STAB']]
        inst['B_STAB'] = inst['B_STAB'].astype('int')
        inst           = inst.merge(bus_info[['BUS_ID', 'BUS_NAME']], left_on='B_STAB', right_on='BUS_ID', how='left')

        inst.loc[inst['BUS_NAME'].str.contains('UTE'), 'TIPO'] = 'UTE'
        inst.loc[inst['BUS_NAME'].str.contains('UHE'), 'TIPO'] = 'UHE'
        inst['TIPO'].fillna('OUTROS')



        return inst

    # ===================================================================================================================================================== #

    def plot_inst_days_hours(self, show=False):

        data         = self.data[['Dia', 'Hora', 'DCIM_I1', 'DCIM_I2', 'DCIM_I3', 'TGEN_I1', 'TGEN_I2', 'TGEN_I3']]
        data['DCIM'] = data[['DCIM_I1', 'DCIM_I2', 'DCIM_I3']].sum(axis=1)
        data['TGEN'] = data[['TGEN_I1', 'TGEN_I2', 'TGEN_I3']].sum(axis=1)
        data['VAR']  = data['DCIM_I1'] #/data['TGEN']
        data['Dia']  = data['Dia'].astype('str').str.zfill(2)
        data         = data[['Dia', 'Hora', 'VAR']]

        inst = self.instavel[['Dia', 'Hora', 'Contigence']]
        inst['Dia']  = inst['Dia'].astype('str').str.zfill(2)
        secs = pd.DataFrame(list(product(inst['Dia'], inst['Hora'])), columns=['Dia', 'Hora']).drop_duplicates().reset_index(drop=True)
        inst = inst.groupby(['Dia', 'Hora']).count().reset_index(drop=False)
        inst = inst[inst['Contigence'] != 0].reset_index(drop=True)
        inst = secs.merge(inst, on=['Dia', 'Hora'], how='left')
        inst = inst.sort_values(by=['Hora', 'Dia']).reset_index(drop=True)
        inst = data.merge(inst, on=['Dia', 'Hora'], how='left')

        inst['Dia'] = inst['Dia'].astype('int')
        inst['VAR'] = inst['VAR'].fillna(0)

        x, y, z, a = inst['Hora'], inst['Dia'], inst['Contigence'], inst['VAR']

        plt.figure(figsize=(14, 6))

        # points = plt.scatter(x, y, c=a, s=150, cmap='gist_yarg', marker='s')

        colors    = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']
        # ['royalblue', 'navy', 'lightgreen', 'green', 'tan', 'darkgoldenrod', 'thistle', 'purple', 'lightcoral', 'red']
        cmap_name = 'my_list'
        cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=len(colors))


        points = plt.scatter(x, y, c=z, s=90, cmap=cmap, marker='s')

        plt.colorbar(points, ticks=[i*1 for i in range(0, 6)])
        plt.xticks(rotation=75)
        plt.yticks([i for i in range(1, 29)], [str(i) for i in range(1, 29)])
        plt.title('Number of Contingencies with Instability', fontsize = 18)
        plt.xlabel('Hour', fontsize = 18)
        plt.ylabel('Day', fontsize = 18)
        plt.grid(alpha=0.2)
        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_days_hours.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()

    # ===================================================================================================================================================== #

    def plot_inst_contigence_bus(self, show=False):

        inst = self.instavel[['OP', 'Contigence', 'B_STAB']]
        print(len(inst['OP'].unique()))
        secs = pd.DataFrame(list(product(inst['Contigence'], inst['B_STAB'])), columns=['Contigence', 'B_STAB']).drop_duplicates().reset_index(drop=True)
        inst = inst.groupby(['Contigence', 'B_STAB']).count().reset_index(drop=False)
        inst = inst[inst['OP'] != 0].reset_index(drop=True)
        inst = secs.merge(inst, on=['Contigence', 'B_STAB'], how='left') #.fillna(0)
        # inst = inst[inst['OP'] > 30]
        inst = inst.sort_values(by=['B_STAB', 'Contigence']).reset_index(drop=True)

        x, y, z = inst['B_STAB'].astype('int').astype('str'), inst['Contigence'].astype('str'), inst['OP']

        plt.figure(figsize=(16, 8))

        points = plt.scatter(x, y, c=z, s=450, cmap=self.cmap, marker='s')

        plt.colorbar(points, ticks=[i*6 for i in range(1, 11)])
        plt.xticks(rotation=90)
        plt.title('Number of Contingencies with Instability', fontsize = 18)
        plt.xlabel('Bus', fontsize = 18)
        plt.ylabel('Contingency', fontsize = 18)
        plt.grid(alpha=0.2)

        if not show:
            plt.savefig(self.save_path + 'plot_inst_contigence_bus.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()

    # ===================================================================================================================================================== #

    def plot_inst_OP_bus(self, show=False):

        inst = self.instavel[['OP', 'Contigence', 'B_STAB']]


        teste = inst.groupby(['B_STAB']).count().reset_index(drop=False).rename(columns={'OP':'Count'})
        inst = inst.merge(teste[['B_STAB', 'Count']], on='B_STAB', how='left').sort_values(by='Count', ascending=False).reset_index(drop=True)

        print(inst)





        inst = inst.groupby(['OP', 'B_STAB']).count().reset_index(drop=False)
        inst = inst.sort_values(by=['B_STAB', 'OP']).reset_index(drop=True)
        inst = inst[inst['Contigence'] > 5].reset_index(drop=True)

        # print(inst['OP'])

        x, y, z = inst['B_STAB'].astype('int').astype('str'), inst['OP'].astype('str'), inst['Contigence']

        plt.figure(figsize=(16, 8))

        points = plt.scatter(x, y, c=z, s=60, cmap=self.cmap)

        plt.colorbar(points, ticks=[i*4 for i in range(1, 11)])
        plt.xticks(rotation=90)
        # plt.yticks([i for i in range(1, 52)], [str(i) for i in range(1, 52)])
        plt.title('Numero Contingências com Instabilidades Transitórias', fontsize = 18)
        plt.xlabel('Barra', fontsize = 18)
        plt.ylabel('Número da Contingência', fontsize = 18)

        plt.grid(axis='y')

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        # if not show:
        #     plt.savefig(self.save_path + 'plot_inst_OP_bus.png', bbox_inches="tight", dpi=300)
        
        # else:
        #     plt.show()

    # ===================================================================================================================================================== #

    def plot_inst_contigence_op(self, show=False):

        inst = self.instavel[['OP', 'Contigence', 'B_STAB', 'Hora', 'Dia']]
        test = inst.groupby(['OP']).count().reset_index(drop=False)
        test = test.sort_values(by='Contigence')
        test = test[test['Contigence'] > 30]
        inst = inst[inst['OP'].isin(test['OP'].values)].reset_index(drop=True)
    
        inst['Nome'] = inst['Dia'].astype('str') + ' - ' + inst['Hora']

        x, y = inst['Contigence'], inst['Nome']

        plt.figure(figsize=(14, 6))
        plt.grid()

        plt.scatter(x, y, s=100)

        plt.xticks([i for i in range(1, 52)], [str(i) for i in range(1, 52)], rotation=90)
        plt.title('Pontos de Operação com Instabilidades Transitórias\nPontos de Operação com mais de 25 contingências com instabilidade', fontsize = 18)
        plt.xlabel('Número da Contingência', fontsize = 18)
        plt.ylabel('Ponto de Operação', fontsize = 18)
        
        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_contigence_op.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()
        

    # ===================================================================================================================================================== #

    def plot_inst_histogram_contingence(self, show=False):

        inst = self.instavel[['OP', 'Contigence', 'B_STAB', 'Hora', 'Dia']]
        inst = inst.groupby(['Contigence']).count().reset_index(drop=False)
        inst = inst.sort_values(by='Contigence')

        x, y = inst['Contigence'].astype('str'), inst['OP']

        plt.figure(figsize=(14, 8))

        bar_container = plt.bar(x, y)
        plt.bar_label(bar_container)

        plt.ylabel('Number of Operating Points with Instability', fontsize = 18)
        plt.xlabel('Contingency', fontsize = 18)
        plt.title('Number of Contingencies with Instabilities', fontsize = 18)

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_histogram_contingence.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()
        

    # ===================================================================================================================================================== #

    def plot_inst_histogram_operation_points(self, show=False):

        inst = self.instavel[['OP', 'Contigence', 'B_STAB', 'Hora', 'Dia']]

        inst['Nome'] = inst['Dia'].astype('str') + ' - ' + inst['Hora']

        inst = inst.groupby(['Nome']).count().reset_index(drop=False)
        inst = inst.sort_values(by='Nome')
        inst = inst[inst['OP'] > 30].reset_index(drop=True)

        print(inst['Nome'])

        x, y = inst['Nome'], inst['OP']

        plt.figure(figsize=(14, 8))

        bar_container = plt.barh(x, y)
        plt.bar_label(bar_container)

        plt.xticks(rotation=0)
        plt.ylabel('Ponto de Operação')
        plt.xlabel('Número de Contingências com Instabilidade')
        plt.title('Número Contingências com Instabilidades Transitórias')

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_histogram_operation_points.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()
        

    # ===================================================================================================================================================== #

    def plot_inst_histogram_day(self, show=False):

        inst         = self.instavel[['OP', 'Contigence', 'B_STAB', 'Hora', 'Dia', 'DCIM_I1', 'DCIM_I2', 'DCIM_I3']]
        inst['Dia']  = inst['Dia'].astype('str').str.zfill(2)
        inst['DCIM'] = inst[['DCIM_I1', 'DCIM_I2', 'DCIM_I3']].sum(axis=1)
        inst         = inst[['DCIM', 'Contigence', 'OP', 'Dia']].drop_duplicates().reset_index(drop=False)


        teste = inst[['DCIM', 'Dia']].drop_duplicates()
        teste = teste[teste['Dia'] == 1].reset_index(drop=True)

        print(teste)



        inst1 = inst.groupby(['Dia']).count().reset_index(drop=False)  
        inst2 = inst[['DCIM', 'Dia']].groupby(['Dia']).mean().reset_index(drop=False)   

        inst = inst1[['OP', 'Dia']].merge(inst2[['DCIM', 'Dia']], on='Dia', how='left')
        print(inst)
        inst = inst.sort_values(by='Dia')
        # inst = inst[inst['A'] > 15]

        x, y   = inst['Dia'], inst['OP']
        x1, y1 = inst['Dia'], inst['DCIM']

        # plt.figure(figsize=(14, 8))
        fig, ax1 = plt.subplots(figsize=(14, 8))
        # ax2      = ax1.twinx()

        bar_container = ax1.bar(x, y)
        ax1.bar_label(bar_container)
        # ax2.plot(x1, y1, color='r')

        # plt.xticks([i for i in range(1, 29)], [str(i) for i in range(1, 29)], rotation=0)
        plt.ylabel('Number of Contingencies with Instability')
        plt.xlabel('Day')
        plt.title('Number of Contingencies with Instability')

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_histogram_day.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()
        

    # ===================================================================================================================================================== #

    def plot_inst_histogram_hour(self, show=False):

        inst = self.instavel[['OP', 'Contigence', 'B_STAB', 'Hora', 'Dia']]
        inst = inst.groupby(['Hora']).count().reset_index(drop=False)   
        inst = inst.sort_values(by='Hora')
        # inst = inst[inst['OP'] > 15]

        x, y = inst['Hora'], inst['OP']

        plt.figure(figsize=(14, 8))

        bar_container = plt.bar(x, y)
        plt.bar_label(bar_container)

        plt.xticks(rotation=90)
        plt.ylabel('Number of Contingencies with Instability')
        plt.xlabel('Hour')
        plt.title('Number of Contingencies with Instability')

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_histogram_hour.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()
        

    # ===================================================================================================================================================== #

    def plot_inst_histogram_bus(self, show=False, gen_info=None):

        inst = self.instavel[['OP', 'Contigence', 'B_STAB', 'Hora', 'Dia']]

        print(inst[(inst['Contigence'] == 8) & (inst['B_STAB'] == 5061)])

        inst = inst.groupby(['B_STAB']).count().reset_index(drop=False)   
        inst = inst.sort_values(by='B_STAB')
        # inst = inst[inst['OP'] > 15]

        

        x, y = inst['B_STAB'].astype('int').astype('str'), inst['OP']

        # print(gen_info.columns)
        # print(gen_info.dtypes)
        # print(type(x.unique()[0]))
        a = [str(int(gen_info[gen_info['BUS_ID'] == int(i)]['PMAX_MW'].astype('float').sum())) + ' MW' for i in x.unique()]
        # print(a)

        plt.figure(figsize=(14, 8))

        bar_container = plt.bar(x, y)
        plt.bar_label(bar_container, labels=a, rotation='vertical', padding=10)

        plt.xticks(rotation=90)
        plt.ylabel('Número de Contingências com Instabilidade')
        plt.xlabel('Barra')
        plt.title('Número Contingências com Instabilidades')
        plt.grid(axis='y')
        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_histogram_bus.png', bbox_inches="tight", dpi=300) 
        
        else:
            plt.show()
               
    
    # ===================================================================================================================================================== #

    def plot_inst_histogram_CODE(self, show=False):

        # inst = self.data_i[self.data_i['SIGLA'] == 'CODE'].reset_index(drop=True)
        inst = self.instavel[['OP', 'Contigence', 'A_CODE', 'Hora', 'Dia']]

        # inst = inst[inst['Contigence'] == 5]

        print(len(inst))
        print(inst['A_CODE'].value_counts().reset_index(drop=False))

        codes = inst['A_CODE'].value_counts().reset_index(drop=False)
        codes = codes.sort_values(by='A_CODE', ascending=True)

        x, y = codes['A_CODE'].astype('int').astype('str'), codes['count']

        plt.figure(figsize=(14, 8))

        bar_container = plt.bar(x, y)
        plt.bar_label(bar_container)

        plt.ylabel('Número de Apariações')
        plt.xlabel('Código')
        plt.title('Número de Apariações de cada Código')

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_inst_histogram_CODE.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()
        

     # ===================================================================================================================================================== #

    def plot_code_histogram_CODE(self, show=False):

        # inst = self.codigo[self.codigo['SIGLA'] == 'CODE'].reset_index(drop=True)
        inst = self.codigo[['OP', 'Contigence', 'A_CODE', 'Hora', 'Dia']]

        print(len(inst))
        print(inst['A_CODE'].value_counts().reset_index(drop=False))

        codes = inst['A_CODE'].value_counts().reset_index(drop=False)
        codes = codes.sort_values(by='A_CODE', ascending=True)

        x, y = codes['A_CODE'].astype('int').astype('str'), codes['count']

        plt.figure(figsize=(14, 8))

        bar_container = plt.bar(x, y)
        plt.bar_label(bar_container)

        plt.ylabel('Número de Apariações')
        plt.xlabel('Código')
        plt.title('Número de Apariações de cada Código')

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if not show:
            plt.savefig(self.save_path + 'plot_code_histogram_CODE.png', bbox_inches="tight", dpi=300)
        
        else:
            plt.show()
        


























''' 
*****************************************************************************************************************************************************************

    RST_Plot_estavel -> RST_Plot

*****************************************************************************************************************************************************************
''' 


class RST_Plot_estavel(RST_Plot):

    def infos(self):
        
        tipos = {'CC e Abertura de Linha'                       : [2, 3, 4, 5, 6, 7, 10], #1, 8, 9
                'Perda de Geração'                             : [11, 12, 13, 14, 15],
                'Bloqueio de Polo'                             : [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                'Falha de comutação nos elos HVDC'             : [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 46, 47],
                'Perda dupla de linha'                         : [44, 45],
                'Curto na LT CC seguido do bloqueio do bipolo' : [48, 49],
                'Bloqueio (ESOF) do bipolo com FCB'            : [50, 51],}
        
        est         = self.estavel
        
        est = est[est['Contigence'].isin(tipos['Perda de Geração'])]

        print(est[['%MW', '%MW_r']])

        print(est.columns)
        
        # est         = est[['Contigence', 'GMAX_I1', 'TGEN_I1', 'GIRS_I1', 'A_NDRC']]
        # est['DIFF'] = est['GMAX_I1'] - est['TGEN_I1']

        est['TINR'] = est[['TINR_I1', 'TINR_I2', 'TINR_I3']].sum(axis=1)


        fig = plt.figure(figsize=(10, 6))

        for con in est['Contigence'].unique():

            a = est[est['Contigence'] == con]
        
            x, y = a['TINR'], 60 - a['A_NDRC'] 

            z = np.polyfit(x, y, 1)
            p = np.poly1d(z)

            res = pearsonr(x, y)

            print(con, z)
            print(con, res)

            

            plt.plot(x, p(x), label='Cont.  ' + str(con)) #, color='red'
            plt.scatter(x, y, label='C ' + str(con))

        plt.ylabel('GMAX - TGEN [MW]')
        plt.xlabel('GIRS [MW]')
        plt.title('(GMAX - TGEN) x GIRS')
        plt.grid()
        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        plt.savefig(self.save_path + 'test' + '.png', bbox_inches="tight", dpi=300)
        # plt.show()
        print(est.columns)

        # if islands is not None:
        #     est_raw[x_variable] = est_raw[[x_variable + '_I' + str(i) for i in islands]].sum(axis=1)

        # if round is not None:
        #     est_raw[x_variable] = est_raw[x_variable].round(round)

        # if mean:
        #     est_raw = est_raw.groupby(['Contigence', x_variable])['A_RCFC'].mean().reset_index(drop=False)

        # if contigence is not None:
        #     est_raw = est_raw[est_raw['Contigence'].isin(contigence)]

        
        # if not single:

        #     x, y = est_raw[x_variable], est_raw['A_RCFC']

        #     fig = plt.figure(figsize=(10, 6))
        #     gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4), left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.05, hspace=0.05)

        #     ax       = fig.add_subplot(gs[1, 0])
        #     ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
        #     ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

        #     self.scatter_hist(x, y, ax, ax_histx, ax_histy)

        #     ax.set_ylabel('RoCoF [Hz/s]')
        #     ax.set_xlabel(xlabel)
        #     plt.suptitle(title)

        # else:
        #     fig = plt.figure(figsize=(10, 6))

        #     for cont in est_raw['Contigence'].unique():

        #         est_single = est_raw[est_raw['Contigence'] == cont]
        #         x, y       = est_single[x_variable], est_single['A_RCFC']

        #         plt.plot(x, y, label='Cont. ' + str(cont))
        #         plt.scatter(x, y)
        #         plt.legend()

        #     plt.ylabel('RoCoF [Hz/s]')
        #     plt.xlabel(xlabel)
        #     plt.title(title)

        # if show:
        #     plt.show()

        # else:
        #     plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        #     plt.savefig(self.save_path + title + '.png', bbox_inches="tight", dpi=300)


    # ===================================================================================================================================================== #

    def plot_est_violin_rocof(self, show=False):    

        est_raw = self.estavel[['Contigence', 'A_RCFC']]

        _rocofs, _labels, _colors = [], [], []
        rocofs , labels ,  colors = [], [], []

        # est_raw['Contigence_Number_int'] = est_raw['Contigence_Number'].astype('int')

        # t = (est_raw['SIGLA'] == 'RCFC') & (est_raw['Contigence_Number'] != '10')

        # print(est_raw[t][['Operational Point', 'Contigence', 'Contigence_Number', 'A']].sort_values(by='A', ascending=False).head(25))

        for idx, cont in enumerate(sorted(est_raw['Contigence'].unique())):

            est    = est_raw[est_raw['Contigence'] == cont]
            cor    = 'red' if any((est['A_RCFC'] > 2.5)) else 'lightskyblue'
            filt_y = (est['A_RCFC'] < 2.5)

            _rocofs.append(est[filt_y]['A_RCFC'].values)
            _labels.append(cont)
            _colors.append(cor)            

            if (idx+1)%9 == 0 or idx+1 == len(est_raw['Contigence'].unique()):
                rocofs.append(_rocofs)
                labels.append(_labels)
                colors.append(_colors)
                _rocofs, _labels, _colors = [], [], []

        

        fig, axs = plt.subplots(2, 3, figsize=(30, 13), sharey=True)
        x, y     = 0, 0 
        for r, l, c in zip(rocofs, labels, colors):

            vio = axs[y, x].violinplot(r, showmeans=True, showmedians=True)

            vio['cmeans'].set_color(['red' for i in range(len(r))])
            for pc, color in zip(vio['bodies'], c): pc.set_facecolor(color)

            axs[y, x].set_xticks([i for i in range(1, len(l)+1)], l, rotation=45)

            fig.suptitle('Gráfico Violino: RoCoF x Contingência')

            if x == 0: axs[y, x].set_ylabel('Distrubuição do RoCoF')
            if y == 1: axs[y, x].set_xlabel('Contingências')

            axs[y, x].grid(True, axis='y')

            y = 1 if x == 2 else y
            x = 0 if x == 2 else x+1

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        if show:
            plt.show()
        else:
            plt.savefig(self.save_path + 'plot_est_violin_rocof.png', bbox_inches="tight", dpi=300)

    # ===================================================================================================================================================== #

    def plot_est_violin_nadir(self, show=False):

        est_raw = self.estavel[['Contigence', 'A_NDRC']]
        est_raw['A_NDRC'] = 60 - est_raw['A_NDRC']
        est_raw = est_raw.sort_values(by='Contigence').reset_index(drop=True)

        _rocofs, _labels, _colors = [], [], []
        rocofs , labels ,  colors = [], [], []

        # t = (est_raw['SIGLA'] == 'NDRC')
        # est_raw['Nadir'] = 60  -est_raw['A']

        # print(est_raw[t][['Operational Point', 'Contigence', 'Contigence_Number', 'Nadir']].sort_values(by='Nadir', ascending=True).head(25))

        for idx, cont in enumerate(est_raw['Contigence'].unique()):

            est    = est_raw[est_raw['Contigence'] == cont]
            cor    = 'red' if any((est['A_NDRC'] < 58)) else 'lightskyblue'
            filt_y = (est['A_NDRC'] > 58)

            _rocofs.append(est[filt_y]['A_NDRC'].values)
            _labels.append(cont)
            _colors.append(cor)            

            if (idx+1)%9 == 0 or idx+1 == len(est_raw['Contigence'].unique()):
                rocofs.append(_rocofs)
                labels.append(_labels)
                colors.append(_colors)
                _rocofs, _labels, _colors = [], [], []

        fig, axs = plt.subplots(2, 3, figsize=(30, 13), sharey=True)
        x, y     = 0, 0 
        for r, l, c in zip(rocofs, labels, colors):

            bp  = axs[y, x].violinplot(r, showmeans=True, showmedians=True)

            bp['cmeans'].set_color(['red' for i in range(len(r))])
            for pc, color in zip(bp['bodies'], c):
                pc.set_facecolor(color)

            axs[y, x].set_xticks([i for i in range(1, len(l)+1)], l, rotation=45)

            fig.suptitle('Gráfico Violino: Frequência de Nadir  x Contingência')

            if x == 0: axs[y, x].set_ylabel('Distrubuição da Frequência de Nadir')
            if y == 1: axs[y, x].set_xlabel('Contingências')

            axs[y, x].grid(True, axis='y')

            y = 1 if x == 2 else y
            x = 0 if x == 2 else x+1

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        plt.savefig(self.save_path + 'plot_est_violin_nadir.png', bbox_inches="tight", dpi=300)

    # ===================================================================================================================================================== #

    def plot_est_violin_damping(self, show=False):

        bad_key = self.data[(self.data['A'] == 1)]['key'].unique()
        est_raw = self.data_e

        

        _rocofs, _labels, _colors = [], [], []
        rocofs , labels ,  colors = [], [], []

        est_raw['Contigence_Number_int'] = est_raw['Contigence_Number'].astype('int')

        t = (est_raw['SIGLA'] == 'DAMP') #& (est_raw['Contigence_Number'] != '10')

        print(est_raw[t][['Operational Point', 'Contigence', 'Contigence_Number', 'A']].sort_values(by='A', ascending=False).head(25))
        print(len(est_raw[(est_raw['SIGLA'] == 'DAMP')]))
        print(len(est_raw[(est_raw['SIGLA'] == 'DAMP') & (est_raw['A'] > 0)]))
        print(len(est_raw[(est_raw['SIGLA'] == 'DAMP') & (est_raw['A'] < 0)]))

        for idx, cont in enumerate(sorted(est_raw['Contigence_Number_int'].unique())):

            est    = est_raw[est_raw['Contigence_Number_int'] == cont]

            if any(((est['SIGLA'] == 'DAMP') & (est['A'] < -10) & (est['A'] > 10))):
                
                cor = 'gray'

            elif any(((est['SIGLA'] == 'DAMP') & (est['A'] < -10))):
                
                cor = 'red'

            elif any(((est['SIGLA'] == 'DAMP') & (est['A'] > 10))):

                cor = 'green'
            
            else:

                cor = 'lightskyblue'

            filt_y = (est['SIGLA'] == 'DAMP') & (est['A'] > -10) & (est['A'] < 10)

            _rocofs.append(est[filt_y]['A'].values)
            _labels.append(cont)
            _colors.append(cor)        

            if (idx+1)%9 == 0 or idx+1 == len(est_raw['Contigence_Number'].unique()):
                rocofs.append(_rocofs)
                labels.append(_labels)
                colors.append(_colors)
                _rocofs, _labels, _colors = [], [], []

        fig, axs = plt.subplots(2, 3, figsize=(30, 13), sharey=True)
        x, y     = 0, 0 
        for r, l, c in zip(rocofs, labels, colors):

            bp  = axs[y, x].violinplot(r, showmeans=True, showmedians=True)

            bp['cmeans'].set_color(['red' for i in range(len(r))])
            for pc, color in zip(bp['bodies'], c):
                pc.set_facecolor(color)

            axs[y, x].set_xticks([i for i in range(1, len(l)+1)], l, rotation=45)

            fig.suptitle('Gráfico Violino: Amortecimento  x Contingência')

            if x == 0: axs[y, x].set_ylabel('Distrubuição da Amortecimento')
            if y == 1: axs[y, x].set_xlabel('Contingências')

            axs[y, x].grid(True, axis='y')
            # axs[y, x].set_yticklabels(fontsize=20)

            y = 1 if x == 2 else y
            x = 0 if x == 2 else x+1

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        plt.savefig(self.save_path + 'plot_est_violin_damping.png', bbox_inches="tight", dpi=300)   

    # ===================================================================================================================================================== #


    def RCFC_comparation(self, x_variable, xlabel, title, contigence=None, mean=False, round=None, islands=None, single=False, show=False, line=True):

        est_raw = self.estavel

        

        if islands is not None:
            if x_variable == 'Reserva':
                est_raw['Reserva']  = est_raw[[v + '_I' + str(i) for i in islands for v in ['HRSV', 'TRSV']]].sum(axis=1)
            else:
                est_raw[x_variable] = est_raw[[x_variable + '_I' + str(i) for i in islands]].sum(axis=1)

        if round is not None:
            est_raw[x_variable] = est_raw[x_variable].round(round)

        if mean:
            est_raw = est_raw.groupby(['Contigence', x_variable])['A_RCFC'].mean().reset_index(drop=False)

        if contigence is not None:
            est_raw = est_raw[est_raw['Contigence'].isin(contigence)]

        
        if not single:

            x, y = est_raw[x_variable], est_raw['A_RCFC']

            fig = plt.figure(figsize=(10, 6))
            gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4), left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.05, hspace=0.05)

            ax       = fig.add_subplot(gs[1, 0])
            ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
            ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

            self.scatter_hist(x, y, ax, ax_histx, ax_histy)

            ax.set_ylabel('RoCoF [Hz/s]')
            ax.set_xlabel(xlabel)
            plt.suptitle(title)

        else:
            fig = plt.figure(figsize=(10, 6))

            

            for cont in est_raw['Contigence'].unique():

                est_single = est_raw[est_raw['Contigence'] == cont]
                x, y       = est_single[x_variable], est_single['A_RCFC']

                reg  = LinearRegression().fit(est_single[x_variable].to_numpy().reshape(-1, 1), est_single['A_RCFC'].to_numpy().reshape(-1, 1))
                pred = reg.predict(est_single[x_variable].unique().reshape(-1, 1))

                if line:
                    plt.plot(x, y)

                plt.plot(est_single[x_variable].unique(), pred, color='red')
                plt.scatter(x, y, label='Cont. ' + str(cont))
                # plt.legend(loc='best', bbox_to_anchor=(1.15, 0.9))

            plt.ylabel('RoCoF [Hz/s]', fontsize=18)
            plt.xlabel(xlabel, fontsize=18)
            plt.title(title, fontsize=18) # + f'\nRoCoF = {x_variable}*{reg.coef_[0][0]:.5f} + {reg.intercept_[0]:.5f}')

        if show:
            plt.show()

        else:
            # plt.legend(loc='best', bbox_to_anchor=(1.15, 1))
            plt.savefig(self.save_path + title + '.png', bbox_inches="tight", dpi=300)

        plt.close()




    # ===================================================================================================================================================== #
    
    
    # 

    def RCFC_Clustering(self, x_variable, xlabel, title, contigence=None, mean=False, round=None, islands=None, single=False, show=False, line=True):
        
        est_raw = self.estavel

        if islands is not None:
            est_raw[x_variable] = est_raw[[x_variable + '_I' + str(i) for i in islands]].sum(axis=1)

        if round is not None:
            est_raw[x_variable] = est_raw[x_variable].round(round)

        if mean:
            est_raw = est_raw.groupby(['Contigence', x_variable])['A_RCFC'].mean().reset_index(drop=False)

        if contigence is not None:
            est_raw = est_raw[est_raw['Contigence'].isin(contigence)]


        min_clusters, max_clusters = 2, 10
        silhouette, davies, calinski, distorsions = [], [], [], []
        datas = []

        tester = est_raw.copy()

        tester['A_RCFC']   = (tester['A_RCFC']-tester['A_RCFC'].min(axis=0))/(tester['A_RCFC'].max(axis=0)-tester['A_RCFC'].min(axis=0))
        tester[x_variable] = (tester[x_variable]-tester[x_variable].min(axis=0))/(tester[x_variable].max(axis=0)-tester[x_variable].min(axis=0))

        for n_clusters in tqdm(range(min_clusters, max_clusters)):

            cluster = BisectingKMeans(n_clusters   = n_clusters,
                                # init         = 'k-means++', 
                                # random_state = 0, 
                                # n_init       = 'auto', 
                                # max_iter     = 100, 
                                tol          = 0.0000000000000005, 
                                # algorithm    = 'lloyd'
                                ).fit(tester[['A_RCFC', x_variable]])
            
            # cluster = AgglomerativeClustering(n_clusters   = n_clusters).fit(tester[['A_RCFC', x_variable]])HDBSCAN
            # cluster = DBSCAN(eps=0.0000000000000005, 
            #                  algorithm='kd_tree',
            #                  min_samples=50).fit(tester[['A_RCFC', x_variable]])
    
            est_raw['LABEL'] = cluster.labels_ 

            # print(est_raw['LABEL'].unique())

            datas.append(est_raw.copy())

            d = davies_bouldin_score(est_raw[['A_RCFC', x_variable]], est_raw['LABEL'])
            c = calinski_harabasz_score(est_raw[['A_RCFC', x_variable]], est_raw['LABEL'])
            
            davies.append(d)

        print(davies)
        plt.figure(figsize=(8,6))
        plt.plot([idx for idx in range(min_clusters, max_clusters)], davies)
        plt.title('Davies-Bouldin Score')
        plt.ylabel('Davies-Bouldin Score')
        plt.xlabel('Número de Clusters')
        # plt.grid()
        plt.show()
        index, element = min(enumerate(davies), key=itemgetter(1))

        est_raw = datas[0]
        
        est_raw = est_raw.sort_values(by='LABEL')

        est_raw['TESTE'] = est_raw['A_RCFC'] > (est_raw[x_variable]*(-0.00018) + 1.83)

        if not single:

            pred = est_raw[x_variable].unique()*(-0.00018) + 1.83

            fig = plt.figure(figsize=(10, 6))
            for idx, lb in enumerate(est_raw['TESTE'].unique()):

                est_single = est_raw[est_raw['TESTE'] == lb]

                x, y = est_single[x_variable], est_single['A_RCFC']

                reg  = LinearRegression().fit(est_single[x_variable].to_numpy().reshape(-1, 1), est_single['A_RCFC'].to_numpy().reshape(-1, 1))
                pred = reg.predict(est_single[x_variable].unique().reshape(-1, 1))
                

                plt.plot(est_single[x_variable].unique(), pred, color='black')
                plt.scatter(x, y, label='Cluster ' + str(idx))

            # for lb in est_raw[x_variable].unique():

            #     est_single = est_raw[est_raw['A_RCFC'] < (lb*(-0.00018) + 1.83)]

            #     x, y = est_single[x_variable], est_single['A_RCFC']

                

            #     plt.scatter(x, y, color='orange')




            # pred = est_raw[x_variable].unique()*(-0.00018) + 1.83
            # plt.plot(est_raw[x_variable].unique(), pred, color='red')
                
                # gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4), left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.05, hspace=0.05)

                # ax       = fig.add_subplot(gs[1, 0])
                # ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
                # ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

                # self.scatter_hist(x, y, ax, ax_histx, ax_histy)

            plt.legend(loc='best', bbox_to_anchor=(1.15, 0.9))
            plt.ylabel('RoCoF [Hz/s]')
            plt.xlabel(xlabel)
            plt.tight_layout()
            # plt.grid()
            plt.suptitle(title)

        else:
            fig = plt.figure(figsize=(10, 6))

            for cont in est_raw['Contigence'].unique():

                est_single = est_raw[est_raw['Contigence'] == cont]
                x, y       = est_single[x_variable], est_single['A_RCFC']

                if line:
                    plt.plot(x, y)
                plt.scatter(x, y, label='Cont. ' + str(cont))
                plt.legend(loc='best', bbox_to_anchor=(1.15, 0.9))

            plt.ylabel('RoCoF [Hz/s]', fontsize=18)
            plt.xlabel(xlabel, fontsize=18)
            plt.title(title, fontsize=18)

        if show:
            plt.show()

        else:
            plt.legend(loc='best', bbox_to_anchor=(1.15, 1))
            plt.savefig(self.save_path + title + '.png', bbox_inches="tight", dpi=300)

        plt.close()


    # ===================================================================================================================================================== #


    def NDRC_comparation(self, x_variable, xlabel, title, contigence=None, mean=False, round=None, islands=None, single=False, show=False, line=True):

        est_raw = self.estavel
        est_raw['nadir'] = 60 - est_raw['A_NDRC']

        # if islands is not None:
        #     est_raw[x_variable] = est_raw[[x_variable + '_I' + str(i) for i in islands]].sum(axis=1)

        if islands is not None:
            if x_variable == 'Reserva':
                est_raw['Reserva']  = est_raw[[v + '_I' + str(i) for i in islands for v in ['HRSV', 'TRSV']]].sum(axis=1)
            else:
                est_raw[x_variable] = est_raw[[x_variable + '_I' + str(i) for i in islands]].sum(axis=1)

        if round is not None:
            est_raw[x_variable] = est_raw[x_variable].round(round)

        if mean:
            est_raw = est_raw.groupby(['Contigence', x_variable])['nadir'].mean().reset_index(drop=False)

        if contigence is not None:
            est_raw = est_raw[est_raw['Contigence'].isin(contigence)]

        
        if not single:

            x, y = est_raw[x_variable], est_raw['nadir']

            fig = plt.figure(figsize=(10, 6))
            gs = fig.add_gridspec(2, 2, width_ratios=(4, 1), height_ratios=(1, 4), left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.05, hspace=0.05)

            ax       = fig.add_subplot(gs[1, 0])
            ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
            ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

            self.scatter_hist(x, y, ax, ax_histx, ax_histy)

            ax.set_ylabel('Frequency Nadir [Hz]', fontsize=18)
            ax.set_xlabel(xlabel, fontsize=18)
            plt.suptitle(title, fontsize=18)

        else:
            fig = plt.figure(figsize=(10, 6))

            for cont in est_raw['Contigence'].unique():

                est_single = est_raw[est_raw['Contigence'] == cont]
                x, y       = est_single[x_variable], est_single['nadir']

                reg  = LinearRegression().fit(est_single[x_variable].to_numpy().reshape(-1, 1), est_single['nadir'].to_numpy().reshape(-1, 1))
                pred = reg.predict(est_single[x_variable].unique().reshape(-1, 1))

                if line:
                    plt.plot(x, y)

                plt.plot(est_single[x_variable].unique(), pred, color='red')
                plt.scatter(x, y, label='Cont. ' + str(cont))
                # plt.legend()

            plt.ylabel('Frequency Nadir [Hz]', fontsize=18)
            plt.xlabel(xlabel, fontsize=18)
            plt.title(title, fontsize=18)# + f'\nNadir = {x_variable}*{reg.coef_[0][0]:.5f} + {reg.coef_[0][0]:.5f}')

        if show:
            plt.show()

        else:
            # plt.legend(loc='best', bbox_to_anchor=(1.2, 1.1))
            plt.savefig(self.save_path + title + '.png', bbox_inches="tight", dpi=300)

        plt.close()




















    def plot_est_duplo_hist_RCFC_NDRC(self, show=False):

        print(self.estavel.columns)



        est_raw = self.estavel[['Dia', 'Hora', 'OP', 'Contigence', '%MW_r', 'A_RCFC', 'A_INRT', 'B_INRT', 'DCIM_I1', 'DCIM_I2', 'DCIM_I3', 'DCIM_I1']]
        est_raw['DCIM'] = est_raw[['DCIM_I2', 'DCIM_I3']].sum(axis=1)
        est_raw['INER'] = est_raw['B_INRT'] - est_raw['DCIM']

        print(est_raw[est_raw['OP'] == 'D_18_H_06-00'])

        # est_raw['DCIM_I1'] = est_raw['DCIM_I1'].round(-3)

        # est_raw = est_raw.groupby(['Contigence', 'DCIM_I1'])['A_RCFC'].mean().reset_index(drop=False)

        # est_raw = est_raw[est_raw['Contigence'].isin([11, 12, 13, 14, 15])]

        a = est_raw.sort_values(by='A_RCFC', ascending=False).reset_index(drop=True)
        print(a[a['A_RCFC'] > 0.5][['OP', 'Contigence', 'A_RCFC']])
        a[a['A_RCFC'] > 0.5][['OP', 'Contigence', 'A_RCFC']].to_excel(self.save_path + 'ROCOF.xlsx')

        x, y = est_raw['INER'], est_raw['A_RCFC']

        # Start with a square Figure.
        fig = plt.figure(figsize=(10, 6))
        gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                            left=0.1, right=0.9, bottom=0.1, top=0.9,
                            wspace=0.05, hspace=0.05)
        # Create the Axes.
        ax = fig.add_subplot(gs[1, 0])
        ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
        ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
        # Draw the scatter plot and marginals.
        self.scatter_hist(x, y, ax, ax_histx, ax_histy)

        
        ax.set_ylabel('RoCoF [Hz/s]')
        ax.set_xlabel('Inercia [MW.s]')
        plt.suptitle('RoCoF x Inercia')

        # est_raw['Line']  = [(5500 - b)/7500 + 0.7 for b in x]
        # est_raw['Above'] = est_raw['A_RCFC'] > est_raw['Line'] 


        # for a in est_raw['Above'].unique():

        #     temp = est_raw[est_raw['Above'] == a]

        #     day  = temp['Dia'].unique()
        #     hour = temp['Hora'].unique()
        #     cont = temp['Contigence'].unique()

        #     print(f'\n\n ---------------- {a} ---------------- \n\n')
        #     print(f'Day:  {day}')
        #     print(f'Hour: {hour}')
        #     print(f'Cont: {cont}')

            

        #     temp.to_excel(f'{self.save_path}_{a}.xlsx')

        #     x, y = temp['INER'], temp['A_RCFC']

            

        #     plt.scatter(x, y)
        #     # plt.plot(x.unique(), a)

        # plt.ylabel('RoCoF [Hz/s]', fontsize = 18)
        # plt.xlabel('Inertia [MW.s]', fontsize = 18)
        # plt.title('RoCoF x Inertia', fontsize = 18)

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        plt.savefig(self.save_path + 'rocof.png', bbox_inches="tight", dpi=300)

        # plt.show()


    # ===================================================================================================================================================== #

    def plot_est_duplo_hist_NDRC_NDRC(self, show=False):

        est_raw = self.estavel[['OP', 'Contigence', '%MW_r', 'A_NDRC', 'A_INRT', 'B_INRT', 'DCIM_I1', 'DCIM_I2', 'DCIM_I3', 'DCIM_I1']]

        est_raw['DCIM']    = est_raw[['DCIM_I2', 'DCIM_I3']].sum(axis=1)
        est_raw['INER']    = est_raw['B_INRT'] - est_raw['DCIM']
        est_raw['NADIR'] = 60 - est_raw['A_NDRC']

        # est_raw['INER'] = est_raw['INER'].round(-2)

        # est_raw = est_raw.groupby(['Contigence', 'INER'])['INERCIA'].mean().reset_index(drop=False)

        # est_raw = est_raw[est_raw['Contigence'].isin([11, 12, 13, 14, 15])]

        x, y = est_raw['INER'], est_raw['NADIR']

        a = est_raw.sort_values(by='NADIR', ascending=True).reset_index(drop=True)
        print(a.head(100)[['OP', 'Contigence', 'NADIR']])
        a.head(100)[['OP', 'Contigence', 'NADIR']].to_excel(self.save_path + 'INERCIA.xlsx')


        # Start with a square Figure.
        fig = plt.figure(figsize=(10, 6))
        gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                            left=0.1, right=0.9, bottom=0.1, top=0.9,
                            wspace=0.05, hspace=0.05)
        # Create the Axes.
        ax = fig.add_subplot(gs[1, 0])
        ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
        ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
        # Draw the scatter plot and marginals.
        self.scatter_hist(x, y, ax, ax_histx, ax_histy)

        ax.set_ylabel('Frequency Nadir [Hz]', fontsize = 18)
        ax.set_xlabel('Inertia [MW.s]', fontsize = 18)
        plt.suptitle('Frequency Nadir x Inertia', fontsize = 18)

        # plt.scatter(x, y)

        # plt.ylabel('Frequency Nadir [Hz]', fontsize = 18)
        # plt.xlabel('Inertia [MW.s]', fontsize = 18)
        # plt.title('Frequency Nadir x Inertia', fontsize = 18)

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        plt.savefig(self.save_path + 'nadir.png', bbox_inches="tight", dpi=300)


    # ===================================================================================================================================================== #

    def plot_est_duplo_hist_DAMP_NDRC(self, show=False):

        est_raw = self.data_e#[~(self.data_e['Contigence_Number'] == '10')]
        # est_raw = est_raw[~(est_raw['Contigence_Number'] == '3')]
        # est_raw = est_raw[~(est_raw['Contigence_Number'] == '4')] #& (self.data_e['Contigence_Number'] == '9')

        filt_x = ((est_raw['SIGLA'] == 'NDRC') & (est_raw['C'] > 0))
        filt_y = ((est_raw['SIGLA'] == 'DAMP') ) #& (est_raw['A'] < 10) & (est_raw['A'] > -10)

        x, y = self._fix(est_raw[filt_x], est_raw[filt_y], _x='C')

        print(est_raw[filt_y].sort_values(by='A', ascending=False).head(25)[['Day', 'Hour', 'Contigence', 'A', 'B']])
        print(est_raw[filt_y].sort_values(by='A', ascending=True).head(25)[['Day', 'Hour', 'Contigence', 'A', 'B']])


        # Start with a square Figure.
        fig = plt.figure(figsize=(10, 6))
        gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                            left=0.1, right=0.9, bottom=0.1, top=0.9,
                            wspace=0.05, hspace=0.05)
        # Create the Axes.
        ax = fig.add_subplot(gs[1, 0])
        ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
        ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
        # Draw the scatter plot and marginals.
        self.scatter_hist(x, y, ax, ax_histx, ax_histy)

        ax.set_ylabel('Amortecimento')
        ax.set_xlabel('Inércia [MW/s]')
        plt.suptitle('Amortecimento x Inércia')

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        plt.savefig(self.save_path + 'plot_est_duplo_hist_DAMP_NDRC.png', bbox_inches="tight", dpi=300)

    # ===================================================================================================================================================== #

    def plot_inst_histogram_bus_DAMP(self, negativo=False, zero=False):

        est = self.data_e[self.data_e['SIGLA'] == 'DAMP'].reset_index(drop=True)

        if negativo:
            est = est[est['A'] < 0].reset_index(drop=True)

        if zero:
            est = est[est['A'] == 0].reset_index(drop=True)

        est = est['B'].value_counts(dropna=False).reset_index(drop=False)
        est = est.sort_values(by='index')

        title = 'Histograma da Frequência de Ocorrência das Barras (Amortecimento) '

        if not negativo and not zero:
            est = est[est['B'] > 600]
            title = 'Histograma da Frequência de Ocorrência das Barras (Amortecimento) \nFrequência > 600'

        print(est)

        x, y = est['index'].astype('int').astype('str'), est['B']

        plt.figure(figsize=(14, 8))

        bar_container = plt.bar(x, y)
        plt.bar_label(bar_container)

        plt.ylabel('Frequência de Ocorrência')
        plt.xlabel('Barra')
        plt.title(title)

        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))

        if negativo:
            plt.savefig(self.save_path + 'plot_inst_histogram_bus_DAMP_negativo.png', bbox_inches="tight", dpi=300)
        elif zero:
            plt.savefig(self.save_path + 'plot_inst_histogram_bus_DAMP_zero.png', bbox_inches="tight", dpi=300)
        else:
            plt.savefig(self.save_path + 'plot_inst_histogram_bus_DAMP.png', bbox_inches="tight", dpi=300)



''' 
*****************************************************************************************************************************************************************

    RST_Plot_renovaveis -> RST_Plot

*****************************************************************************************************************************************************************
''' 


class RST_Plot_renovaveis(RST_Plot):

    # ===================================================================================================================================================== #

    def histograma_Pene_NDRC_NDRC(self, show=False):

        for i in range(1, 52):

            est_raw = self.data_n[self.data_n['Contigence_Number'].isin([str(i)])]

            # est_raw = self.data_n[self.data_n['Contigence_Number'].isin([str(i) for i in range(16, 30)])]

            filt_x = est_raw['SIGLA'] == 'NDRC'
            filt_y = est_raw['SIGLA'] == 'NDRC'
            filt_z = est_raw['SIGLA'] == 'NDRC'

            x, y = self._fix(est_raw[filt_x], est_raw[filt_y], _x='C', _y='%MW')
            x, z = self._fix(est_raw[filt_x], est_raw[filt_z], _x='C', _y='A')
            z, y = self._fix(est_raw[filt_z], est_raw[filt_y], _x='A', _y='%MW')

            # Start with a square Figure.
            fig = plt.figure(figsize=(10, 6))
            gs  = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4), left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.05, hspace=0.05)

            # Create the Axes.
            ax       = fig.add_subplot(gs[1, 0])
            ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
            ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

            # Draw the scatter plot and marginals.
            points = self.scatter_hist3d(x, y, z, ax, ax_histx, ax_histy)

            plt.colorbar(points, location='left')

            plt.title(str(i))
            ax.set_ylabel('Penetração [%]')
            ax.set_xlabel('Inércia [s]')
  
            plt.savefig(self.save_path + 'NADIR/' + str(i) + '.png', bbox_inches="tight", dpi=300)

    # ===================================================================================================================================================== #

    def histograma_Pene_NDRC_RCFC(self, show=False):

        for i in range(1, 52):

            est_raw = self.data_n[self.data_n['Contigence_Number'].isin([str(i)])]

            filt_x = est_raw['SIGLA'] == 'NDRC'
            filt_y = est_raw['SIGLA'] == 'NDRC'
            filt_z = est_raw['SIGLA'] == 'RCFC'

            x, y = self._fix(est_raw[filt_x], est_raw[filt_y], _x='C', _y='%MW')
            x, z = self._fix(est_raw[filt_x], est_raw[filt_z], _x='C', _y='A')
            z, y = self._fix(est_raw[filt_z], est_raw[filt_y], _x='A', _y='%MW')

            # Start with a square Figure.
            fig = plt.figure(figsize=(10, 6))
            gs  = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4), left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.05, hspace=0.05)

            # Create the Axes.
            ax       = fig.add_subplot(gs[1, 0])
            ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
            ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

            # Draw the scatter plot and marginals.
            points = self.scatter_hist3d(x, y, z, ax, ax_histx, ax_histy)

            # plt.colorbar(points, location='left')

            plt.title(str(i))
            ax.set_ylabel('Penetração [%]')
            ax.set_xlabel('Inércia [s]')

            # plt.show()
            plt.savefig(self.save_path + 'ROCOF/' + str(i) + '.png', bbox_inches="tight", dpi=300)

    # ===================================================================================================================================================== #

    def histograma_RCFC_NDRC_Pene(self, show=False):

        for i in range(1, 52):

            est_raw = self.data_n[self.data_n['Contigence_Number'].isin([str(i)])]

            filt_x = est_raw['SIGLA'] == 'RCFC'
            filt_y = est_raw['SIGLA'] == 'NDRC'
            filt_z = est_raw['SIGLA'] == 'NDRC'

            x, y = self._fix(est_raw[filt_x], est_raw[filt_y], _x='A',   _y='A')
            x, z = self._fix(est_raw[filt_x], est_raw[filt_z], _x='A',   _y='%MW')
            z, y = self._fix(est_raw[filt_z], est_raw[filt_y], _x='%MW', _y='A')

            # Start with a square Figure.
            fig = plt.figure(figsize=(10, 6))
            gs  = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4), left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.05, hspace=0.05)

            # Create the Axes.
            ax       = fig.add_subplot(gs[1, 0])
            ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
            ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

            # Draw the scatter plot and marginals.
            points = self.scatter_hist3d(x, 60-y, z, ax, ax_histx, ax_histy)

            # plt.colorbar(points, location='left')

            # plt.title(str(i))

            plt.savefig(self.save_path + 'ROCOF_NADIR/' + str(i) + '.png', bbox_inches="tight", dpi=300)



if __name__ == '__main__':

    '''INSTAVEL'''

    RP = RST_Plot(report_path = 'Data/PTOPER_A2V2F2_rev3/OUT/vars.csv',
                  eol         = 'Data/EOL.csv',
                  sol         = 'Data/SOL.csv',
                  save_path   = 'Data/PTOPER_A2V2F2_rev2/IMAGENS/')

    # RP = RST_Plot_nao(repots_path      = 'Data/PTOPER_A2V2F2_rev2/RenovaveisDefault/PTOPER_A2V2F2_rev2.json',
    #                        contigences_path = 'Data/PTOPER_A2V2F2_rev2/RenovaveisDefault/PTOPER_A2V2F2_rev2_cont.json',
    #                        eol              = 'Data/EOL.csv',
    #                        sol              = 'Data/SOL.csv',
    #                        save_path        = 'Data/PTOPER_A2V2F2_rev2/RenovaveisDefault/imagens/')
    
    # RP.plot_inst_days_hours()

    '''INSTAVEL'''

    # RP = RST_Plot_instavel(report_path = 'Data/PTOPER_A2V2F2_rev3/OUT/vars.csv',
    #                        eol         = 'Data/EOL.csv',
    #                        sol         = 'Data/SOL.csv',
    #                        save_path   = 'Data/PTOPER_A2V2F2_rev3/IMAGENS/')
    
    # RP.plot_inst_days_hours(show=False)
    # RP.plot_inst_contigence_bus(show=False)
    # RP.plot_inst_contigence_op(show=False)
    # RP.plot_inst_histogram_contingence(show=False)
    # RP.plot_inst_histogram_operation_points(show=False)
    # RP.plot_inst_histogram_day(show=False)
    # RP.plot_inst_histogram_hour(show=False)
    # RP.plot_inst_histogram_bus(show=False)
    # RP.plot_inst_histogram_CODE(show=False)
    # RP.plot_code_histogram_CODE(show=True)

    '''ESTAVEL'''

    RP = RST_Plot_estavel(report_path = 'Data/PTOPER_A2V2F2_rev3/OUT/vars.csv',
                          eol         = 'Data/EOL.csv',
                          sol         = 'Data/SOL.csv',
                          save_path   = 'Data/PTOPER_A2V2F2_rev3/IMAGENS/')

    # RP.plot_est_violin_rocof()
    # RP.plot_est_violin_nadir()
    # RP.plot_est_violin_damping()
    RP.plot_est_duplo_hist_RCFC_NDRC()
    RP.plot_est_duplo_hist_NDRC_NDRC()
    # RP.plot_est_duplo_hist_DAMP_NDRC()
    # RP.plot_inst_histogram_bus_DAMP(negativo=False, zero=False)
    # RP.plot_inst_histogram_bus_DAMP(negativo=True,  zero=False)
    # RP.plot_inst_histogram_bus_DAMP(negativo=False, zero=True)

    '''RENOVAVEIS'''

    # RP = RST_Plot_renovaveis(repots_path      = 'C:/Users/Scarlet/Desktop/Data/PTOPER_V3A3F2_rev1/PTOPER_V3A3F2_rev1/PTOPER_V3A3F2_rev1.json',
    #                          contigences_path = 'C:/Users/Scarlet/Desktop/Data/PTOPER_V3A3F2_rev1/PTOPER_V3A3F2_rev1/PTOPER_V3A3F2_rev1_cont.json',
    #                          eol              = 'C:/Users/Scarlet/Desktop/Data/EOL.csv',
    #                          sol              = 'C:/Users/Scarlet/Desktop/Data/SOL.csv',
    #                          save_path        = 'C:/Users/Scarlet/Desktop/Data/PTOPER_V3A3F2_rev1/imagens/')


    # RP.histograma_Pene_NDRC_NDRC()
    # RP.histograma_Pene_NDRC_RCFC()
    # RP.histograma_RCFC_NDRC_Pene()
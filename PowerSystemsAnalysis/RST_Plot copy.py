from  RST_Reader import *
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
 
        self.codigo   = self.data[self.data['A_RCFC'].isna()].reset_index(drop=True)
        self.estavel  = self.data[~self.data['A_RCFC'].isna()].reset_index(drop=True)
        self.instavel = self.data[self.data['A_STAB'] == 1].reset_index(drop=True)
        self.instavel = self.instavel[self.instavel['A_CODE'].isin([2, 3])].reset_index(drop=True)

        horas = {'00-00', '00-30', '01-00', '01-30', '02-00', '02-30', '03-00', '03-30', '04-00', '04-30', '05-00', '05-30', '06-00', '06-30',
                 '07-00', '07-30', '08-00', '08-30', '09-00', '09-30', '10-00', '10-30', '11-00', '11-30', '12-00', '12-30', '13-00', '13-30', 
                 '14-00', '14-30', '15-00', '15-30', '16-00', '16-30', '17-00', '17-30', '18-00', '18-30', '19-00', '19-30', '20-00', '20-30',
                 '21-00', '21-30', '22-00', '22-30', '23-00', '23-30'}
        

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


    def plot_est_duplo_hist_NDRC_NDRC(self, show=False):

        est_raw = self.estavel[['OP', 'Contigence', 'Dia', 'Hora', '%MW_r', 'A_NDRC', 'A_INRT', 'B_INRT', 'DCIM_I1', 'DCIM_I2', 'DCIM_I3', 'DCIM_I1']]

        est_raw['DCIM']    = est_raw[['DCIM_I2', 'DCIM_I3']].sum(axis=1)
        est_raw['INER']    = est_raw['B_INRT'] - est_raw['DCIM']
        est_raw['NADIR'] = 60 - est_raw['A_NDRC']


        x, y = est_raw['INER'], est_raw['NADIR']

        a = est_raw.sort_values(by='NADIR', ascending=True).reset_index(drop=True)
        print(a.head(100)[['OP', 'Contigence', 'NADIR']])
        a.head(100)[['OP', 'Contigence', 'NADIR']].to_excel(self.save_path + 'INERCIA.xlsx')

        est_raw['Line']  = 59.5 #[(b-5500)/17500 + 59.6 for b in x]
        est_raw['Above'] = est_raw['NADIR'] > est_raw['Line'] 

        fig = plt.figure(figsize=(10, 6))

        for a in est_raw['Above'].unique():

            temp = est_raw[est_raw['Above'] == a]

            day  = temp['Dia'].unique()
            hour = temp['Hora'].unique()
            OP   = temp['OP'].unique()
            cont = temp['Contigence'].unique()

            print(f'\n\n ---------------- {a} ---------------- \n\n')
            print(f'Day:  {day}')
            print(f'Hour: {hour}')
            print(f'Cont: {cont}')
            print(f'OP:   {OP}')

            temp.to_excel(f'{self.save_path}_{a}.xlsx')

            x, y = temp['INER'], temp['NADIR']

            

            plt.scatter(x, y)

        # plt.scatter(x, y)
        # plt.plot(x, est_raw['Line'], color='red')

        plt.ylabel('Frequência de Nadir [Hz]')
        plt.xlabel('Inercia [MW.s]')
        plt.title('Frequência de Nadir x Inercia')



        plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        plt.show()
        # plt.savefig(self.save_path + 'nadir.png', bbox_inches="tight", dpi=300)

    def plot_est_duplo_hist_RCFC_NDRC(self, show=False):

        print(self.estavel.columns)

        est_raw = self.estavel[['Dia', 'Hora', 'OP', 'Contigence', '%MW_r', 'A_RCFC', 'A_INRT', 'B_INRT', 'DCIM_I1', 'DCIM_I2', 'DCIM_I3', 'DCIM_I1']]
        est_raw['DCIM'] = est_raw[['DCIM_I2', 'DCIM_I3']].sum(axis=1)
        est_raw['INER'] = est_raw['B_INRT'] - est_raw['DCIM']

        est_raw = est_raw[est_raw['Contigence'] != 9]

        # est_raw['DCIM_I1'] = est_raw['DCIM_I1'].round(-3)

        # est_raw = est_raw.groupby(['Contigence', 'DCIM_I1'])['A_RCFC'].mean().reset_index(drop=False)

        # est_raw = est_raw[est_raw['Contigence'].isin([11, 12, 13, 14, 15])]

        a = est_raw.sort_values(by='A_RCFC', ascending=False).reset_index(drop=True)
        print(a[a['A_RCFC'] > 0.5][['OP', 'Contigence', 'A_RCFC']])
        a[a['A_RCFC'] > 0.5][['OP', 'Contigence', 'A_RCFC']].to_excel(self.save_path + 'ROCOF.xlsx')

        x, y = est_raw['INER'], est_raw['A_RCFC']

        # Start with a square Figure.
        fig = plt.figure(figsize=(10, 6))
        # gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
        #                     left=0.1, right=0.9, bottom=0.1, top=0.9,
        #                     wspace=0.05, hspace=0.05)
        # # Create the Axes.
        # ax = fig.add_subplot(gs[1, 0])
        # ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
        # ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
        # # Draw the scatter plot and marginals.
        # self.scatter_hist(x, y, ax, ax_histx, ax_histy)

        
        # ax.set_ylabel('RoCoF [Hz/s]')
        # ax.set_xlabel('Inercia [MW.s]')
        # plt.suptitle('RoCoF x Inercia')

        est_raw['Line']  = [(5500 - b)/7500 + 0.7 for b in x]
        est_raw['Above'] = est_raw['A_RCFC'] > est_raw['Line'] 


        for a in est_raw['Above'].unique():

            temp = est_raw[est_raw['Above'] == a]

            day  = temp['Dia'].unique()
            hour = temp['Hora'].unique()
            cont = temp['Contigence'].unique()

            print(f'\n\n ---------------- {a} ---------------- \n\n')
            print(f'Day:  {day}')
            print(f'Hour: {hour}')
            print(f'Cont: {cont}')

            

            temp.to_excel(f'{self.save_path}_{a}.xlsx')

            x, y = temp['INER'], temp['A_RCFC']

            

            plt.scatter(x, y)
            # plt.plot(x.unique(), a)

        plt.ylabel('RoCoF [Hz/s]')
        plt.xlabel('Inercia [MW.s]')
        plt.title('RoCoF x Inercia')

        # plt.legend(loc='best', bbox_to_anchor=(1, 1.1))
        # plt.savefig(self.save_path + 'rocof.png', bbox_inches="tight", dpi=300)

        plt.show()




    def RCFC_comparation(self, x_variable, xlabel, title, contigence=None, mean=False, round=None, islands=None, single=False, show=False, line=True):



        path = 'D:/PowerSystems/Sistemas/SIN/MEDIA/MODV_PU.csv'
        # path = 'D:/PowerSystems/Sistemas/SIN/MEDIA/PG_MW.csv'
        # path = 'D:/PowerSystems/Sistemas/SIN/MEDIA/B0_MVAR.csv'
        data = pd.read_csv(path)

        OP = data.columns[2:]
        # VO = data[(data['BUS_ID'] == 8313)].values[0][2:]

        print(data[(data['BUS_ID'] > 8310)])
        # print(VO)
        # DF = pd.DataFrame({'OP':OP, 'MODV_PU':VO})

        # est_raw = self.estavel
        # est_raw = est_raw.merge(DF, on='OP', how='left')

        # if islands is not None:
        #     if x_variable == 'Reserva':
        #         est_raw['Reserva']  = est_raw[[v + '_I' + str(i) for i in islands for v in ['HRSV', 'TRSV']]].sum(axis=1)
        #     else:
        #         est_raw[x_variable] = est_raw[[x_variable + '_I' + str(i) for i in islands]].sum(axis=1)

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
        #     fig = plt.figure(figsize=(12, 6))

            

        #     for cont in est_raw['Contigence'].unique():

        #         est_single = est_raw[est_raw['Contigence'] == cont]
        #         x, y, z    = est_single[x_variable], est_single['A_RCFC'], est_single['MODV_PU']

        #         reg  = LinearRegression().fit(est_single[x_variable].to_numpy().reshape(-1, 1), est_single['A_RCFC'].to_numpy().reshape(-1, 1))
        #         pred = reg.predict(est_single[x_variable].unique().reshape(-1, 1))

        #         if line:
        #             plt.plot(x, y)

        #         plt.plot(est_single[x_variable].unique(), pred, color='red')
        #         plt.scatter(x, y, c=z, label='Cont. ' + str(cont))
        #         plt.colorbar()
        #         # plt.legend(loc='best', bbox_to_anchor=(1.15, 0.9))

        #     plt.ylabel('RoCoF [Hz/s]')
        #     plt.xlabel(xlabel)
        #     plt.title(title + f'\nRoCoF = {x_variable}*{reg.coef_[0][0]:.5f} + {reg.intercept_[0]:.5f}')

        # if show:
        #     plt.show()

        # else:
        #     plt.legend(loc='best', bbox_to_anchor=(1.15, 1))
        #     plt.savefig(self.save_path + title + '.png', bbox_inches="tight", dpi=300)

        # plt.close()










caso = 'MEDIA'
RP = RST_Plot(report_path = f'D:/PowerSystems/Sistemas/SIN/{caso}/vars.csv',
                       eol        = f'D:/PowerSystems/Sistemas/SIN/{caso}/EOL.csv',
                       sol        = f'D:/PowerSystems/Sistemas/SIN/{caso}/SOL.csv',
                       save_path  = f'D:/PowerSystems/Sistemas/SIN/{caso}/IMAGENS/ESTAVEL/')


RP.RCFC_comparation(x_variable='TINR', xlabel='TINR', title='RoCoF x TINR', contigence=[9], mean=False , round=None  , islands=[1], single=True , show=True, line=False)
# RP.plot_est_duplo_hist_RCFC_NDRC(show=True)

# temp = RP.estavel#[RP.estavel]

# print(temp.head())








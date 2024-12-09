import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go 
from matplotlib.colors import TwoSlopeNorm
import matplotlib.colors as mcolors
import matplotlib


import warnings
warnings.filterwarnings('ignore')

class CreatePlots:
    def __init__(self, ui, fluxo=None, indice=None):
        self.ui = ui
        self.fluxo = fluxo
        self.indice = indice
        pass

    def persistency_curve(self, dataset, col, ui, fluxo, indice, path=None, ax_fontsize=None):
        df_pwf_elos   = dataset['Nome Elo'].unique()
        print(df_pwf_elos)
        self.ui.STATIC_sc.axes.cla()
        self.ui.STATIC_sc.fig.clf()
        self.ui.STATIC_sc.axes = self.ui.STATIC_sc.fig.add_subplot(111)

        k = self.indice
        # for k in range(len(df_pwf_elos)):
        df_elos = dataset

        if k == 0:
            frm = df_pwf_elos[k][-2:]
            to = 'T'
        elif k == 5:
            frm = df_pwf_elos[k].split('_')[1]
            to  = 'T'
        else:
            splt1 = df_pwf_elos[k].split('_')
            splt2 = splt1[1].split('-')
            frm = splt2[0]
            to = splt2[1]
        
        # print(k, frm, '->', to)
        
        df_elos = pd.DataFrame(df_elos[df_elos['Nome Elo'] == df_pwf_elos[k]][col])

        # fig, ax = self.ui.STATIC_sc.subplots(figsize=(12, 6))

        x = np.sort(np.array(df_elos[col]))
        N = len(x)
        y = np.linspace(1, N, N)

        import_values = len(df_elos[df_elos[col] < 0])
        export_values = len(df_elos[df_elos[col] > 0])
        
        total_import = round((import_values / N) * 100, 2)
        total_export = round((export_values / N) * 100, 2)


        self.ui.STATIC_sc.axes.plot(y[:import_values], x[:import_values], lw=3, c='red', label=f'Import: {total_import}% (-)')
        self.ui.STATIC_sc.axes.plot(y[import_values:export_values], x[import_values:export_values], lw=3, c='blue', label=f'Export: {total_export}% (+)')
        self.ui.STATIC_sc.axes.set_ylabel(f'{col}', weight='bold', fontsize=14) 
        self.ui.STATIC_sc.axes.set_title(fr'Persistency Curve {frm}$\rightarrow${to}', weight='bold', fontsize=20)
        self.ui.STATIC_sc.axes.set_xlabel('# Operation Points', weight='bold', fontsize=14)

        self.ui.STATIC_sc.axes.axhline(y=0, color='k', ls='--', alpha=0.3)
        self.ui.STATIC_sc.axes.tick_params(color='black', labelcolor='black')
        self.ui.STATIC_sc.axes.grid(visible=True, alpha=0.3)

        if ax_fontsize != None:
            self.ui.STATIC_sc.axes.tick_params(axis='both', which='major', labelsize=ax_fontsize)
            self.ui.STATIC_sc.axes.tick_params(axis='both', which='minor', labelsize=ax_fontsize)

        self.ui.STATIC_sc.axes.legend(bbox_to_anchor=(0.01, 1.00), fontsize=13, loc='upper left', fancybox=True, shadow=True)

        self.ui.STATIC_sc.figure.tight_layout()

        self.ui.STATIC_sc.draw()

        # self.ui.STATIC_sc.axes.legend(bbox_to_anchor=(0.01, 1.00), fontsize=13, loc='upper left', fancybox=True, shadow=True)

            # if path != None:
            #     plt.savefig(f'{path}/PC_{df_pwf_elos[k]}')

            # plt.show()

    
    # def box_plots(self, dataset, col, ui, split_flows=None, 
    #           path=None, ax_fontsize=None, scenario=None):
    
    #     widths = 0.5
    #     self.ui.STATIC_sc.axes.clear() 
        
    #     if split_flows == False:
    #         # Criar a figura e os eixos
    #         # fig, ax = plt.subplots(1, 1, figsize=(15, 6))

    #         # # Limpa eixos anteriores, se necessário
    #         # self.ui.STATIC_sc.axes.clear()
    #         # self.ui.STATIC_sc.axes = ax  # Define o eixo do canvas no objeto da UI
            

    #         # Cria o boxplot usando apenas Matplotlib
    #         self.ui.STATIC_sc.axes.boxplot(
    #             [dataset[dataset['Nome Elo'] == val][col] for val in dataset['Nome Elo'].unique()],
    #             widths=widths,
    #             flierprops={"marker": "x"},
    #             labels=dataset['Nome Elo'].unique()
    #         )

    #         # Configurações adicionais do gráfico
    #         if scenario is not None:
    #             self.ui.STATIC_sc.axes.set_title(scenario, weight='bold', fontsize=18)

    #         self.ui.STATIC_sc.axes.set_ylabel(f'{col}', weight='bold', fontsize=13)
    #         self.ui.STATIC_sc.axes.set_xlabel('Nome Elo', weight='bold', fontsize=13)
    #         self.ui.STATIC_sc.axes.grid(True, alpha=0.3)

    #         legend = self.ui.STATIC_sc.axes.get_legend()
    #         if legend:
    #             legend.set_visible(False)

    #         if ax_fontsize is not None:
    #             self.ui.STATIC_sc.axes.tick_params(axis='both', which='major', labelsize=ax_fontsize)
    #             self.ui.STATIC_sc.axes.tick_params(axis='both', which='minor', labelsize=ax_fontsize)

    #         self.ui.STATIC_sc.axes.tick_params(axis='x', rotation=30)

    #         # self.ui.STATIC_sc.axes.set_xticks(range(1, len(labels) + 1))  # Define a posição dos ticks
    #         # self.ui.STATIC_sc.axes.set_xticklabels(labels, fontsize=20, rotation=rotation)  # Define os rótulos e formata

    #         # Mostra o gráfico
    #         self.ui.STATIC_sc.draw()

    #     else:
    #         # Criar a figura e os eixos para múltiplos boxplots
    #         fig, ax = plt.subplots(2, 1, figsize=(12, 8))
    #         self.ui.STATIC_sc.axes.clear()  # Limpa eixos anteriores, se necessário
    #         self.ui.STATIC_sc.axes = ax  # Define o eixo do canvas no objeto da UI

    #         # Divida o dataset
    #         dataset1 = dataset.iloc[:int(dataset.shape[0]/2+1344), :]
    #         dataset2 = dataset.iloc[int(dataset.shape[0]/2)+1344:, :]

    #         # Cria o primeiro boxplot
    #         box1 = self.ui.STATIC_sc.axes[0].boxplot(
    #             [dataset1[dataset1['Nome Elo'] == val][col] for val in dataset1['Nome Elo'].unique()],
    #             widths=widths,
    #             flierprops={"marker": "x"},
    #             labels=dataset1['Nome Elo'].unique()
    #         )

    #         # Cria o segundo boxplot
    #         box2 = self.ui.STATIC_sc.axes[1].boxplot(
    #             [dataset2[dataset2['Nome Elo'] == val][col] for val in dataset2['Nome Elo'].unique()],
    #             widths=widths,
    #             flierprops={"marker": "x"},
    #             labels=dataset2['Nome Elo'].unique()
    #         )

    #         for i in range(2):
    #             self.ui.STATIC_sc.axes[i].set_ylabel(f'{col}', weight='bold', fontsize=13)
    #             self.ui.STATIC_sc.axes[i].set_xlabel('Nome Elo', weight='bold', fontsize=13)
    #             self.ui.STATIC_sc.axes[i].grid(True, alpha=0.5)
    #             if ax_fontsize is not None:
    #                 self.ui.STATIC_sc.axes[i].tick_params(axis='both', which='major', labelsize=ax_fontsize)
    #                 self.ui.STATIC_sc.axes[i].tick_params(axis='both', which='minor', labelsize=ax_fontsize)

    #         self.ui.STATIC_sc.axes.tick_params(axis='x', rotation=30)

    #         # Mostra o gráfico
    #         self.ui.STATIC_sc.draw()





    def box_plots(self, dataset, col, ui, split_flows=None, 
                  path=None, ax_fontsize=None, scenario=None):
        
        widths = 0.5
        
        if split_flows == False:
            # fig, ax = plt.subplots(1, 1, figsize=(15, 6))

            # Referenciar o eixos do MplCanvas para o eixo gerado
            self.ui.STATIC_sc.axes.cla()
            self.ui.STATIC_sc.fig.clf()
            self.ui.STATIC_sc.axes = self.ui.STATIC_sc.fig.add_subplot(111)  # Limpa eixos anteriores, se necessário
            ax = self.ui.STATIC_sc.axes

            sns.boxplot(
                data=dataset, 
                x="Nome Elo", 
                y=col, 
                dodge=False,
                width=widths,
                flierprops={"marker": "x"}, 
                hue=dataset['Nome Elo'],
                palette=sns.color_palette("hls", 8),
                ax=ax
            )

            if scenario != None:
                self.ui.STATIC_sc.axes.set_title(f'{scenario}')

            self.ui.STATIC_sc.axes.set_ylabel(f'{col}', weight='bold', fontsize=13)
            self.ui.STATIC_sc.axes.set_xlabel('Nome Elo', weight='bold', fontsize=13)
            self.ui.STATIC_sc.axes.grid(True, alpha=0.3)
            self.ui.STATIC_sc.axes.set_xticklabels(dataset['Nome Elo'].unique(), rotation=30)

            legend = self.ui.STATIC_sc.axes.get_legend()
            if legend:
                legend.set_visible(False)

            if scenario != None:
                self.ui.STATIC_sc.axes.set_title(f'{scenario}', weight='bold', fontsize=18)

            if ax_fontsize != None:
                self.ui.STATIC_sc.axes.tick_params(axis='both', which='major', labelsize=ax_fontsize)
                self.ui.STATIC_sc.axes.tick_params(axis='both', which='minor', labelsize=ax_fontsize)

            self.ui.STATIC_sc.figure.tight_layout()
            self.ui.STATIC_sc.draw()

            # plt.tight_layout()

            # if path != None:
            #     plt.savefig(f'{path}/BoxPlot_{col}_NSplit_1')

            # plt.show()
        else:
            fig, ax = plt.subplots(2, 1, figsize=(12, 8))
            self.ui.STATIC_sc.axes.clear()  # Limpa eixos anteriores, se necessário
            self.ui.STATIC_sc.axes = ax  # Define o eixo do canvas no objeto da UI

            dataset1 = dataset.iloc[:int(dataset.shape[0]/2+1344), :]
            sns.boxplot(
                data=dataset1, 
                x="Nome Elo", 
                y=col, 
                width=widths,
                dodge=False,
                flierprops={"marker": "x"}, 
                hue=dataset1['Nome Elo'],
                ax=self.ui.STATIC_sc.axes[0]
            )
            dataset2 = dataset.iloc[int(dataset.shape[0]/2)+1344:, :]
            sns.boxplot(
                data=dataset2, 
                x="Nome Elo", 
                y=col, 
                width=widths,    
                dodge=False,  
                flierprops={"marker": "x"}, 
                hue=dataset2['Nome Elo'],
                palette=sns.color_palette("hls", 4),
                ax=self.ui.STATIC_sc.axes[0]
            )
            legend1 = self.ui.STATIC_sc.axes[0].get_legend()
            legend2 = self.ui.STATIC_sc.axes[1].get_legend()
            if legend1 or legend2:
                legend1.set_visible(False)
                legend2.set_visible(False)
            # ax[0].get_legend().set_visible(False) 
            # ax[1].get_legend().set_visible(False) 

            for i in range(0, 2):
                self.ui.STATIC_sc.axes[i].set_ylabel(f'{col}', weight='bold', fontsize=13)
                self.ui.STATIC_sc.axes[i].set_xlabel('Nome Elo', weight='bold', fontsize=13)
                self.ui.STATIC_sc.axes[i].grid(True, alpha=0.5)
                self.ui.STATIC_sc.axes[i].tick_params(axis='both', which='major', labelsize=ax_fontsize)
                self.ui.STATIC_sc.axes[i].tick_params(axis='both', which='minor', labelsize=ax_fontsize)
            
            # if scenario != None:
            #     plt.suptitle(f'{scenario}', weight='bold', fontsize=20)

            # # plt.tight_layout()

            # if path != None:
            #     plt.savefig(f'{path}/BoxPlot_{col}_Split_2') 
            # plt.show()

    def violin_plots(self, dataset, col, ui, split_flows=None, 
                  path=None, ax_fontsize=None, scenario=None):
        widths = 0.5

        self.ui.STATIC_sc.axes.cla()
        self.ui.STATIC_sc.fig.clf()
        self.ui.STATIC_sc.axes = self.ui.STATIC_sc.fig.add_subplot(111)

        if split_flows == False:
            # fig, ax = plt.subplots(1, 1, figsize=(15, 6))
            ax = self.ui.STATIC_sc.axes
            sns.violinplot(
                data=dataset, 
                x="Nome Elo", 
                y=col, 
                dodge=False,
                width=widths,
                cut=0,
                hue=dataset['Nome Elo'],
                palette=sns.color_palette("hls", 8),
                ax = ax
            )

            if scenario != None:
                ax.set_title(f'{scenario}')

            ax.set_ylabel(f'{col}', weight='bold', fontsize=13)
            ax.set_xlabel('Nome Elo', weight='bold', fontsize=13)
            ax.grid(True, alpha=0.3)
            ax.set_xticklabels(dataset['Nome Elo'].unique(), rotation=30)

            legend = ax.get_legend()
            if legend:
                legend.set_visible(False)
            # ax.get_legend().set_visible(False) 

            if scenario != None:
                ax.set_title(f'{scenario}', weight='bold', fontsize=18)

            if ax_fontsize != None:
                ax.tick_params(axis='both', which='major', labelsize=ax_fontsize)
                ax.tick_params(axis='both', which='minor', labelsize=ax_fontsize)


            self.ui.STATIC_sc.figure.tight_layout()
            self.ui.STATIC_sc.draw()

            # plt.tight_layout()      

            # if path != None:
            #     plt.savefig(f'{path}/ViolinPlot_{col}_NSplit_1')
            # plt.show()
        else:
            fig, ax = plt.subplots(2, 1, figsize=(12, 8))

            dataset1 = dataset.iloc[:int(dataset.shape[0]/2+1344), :]
            sns.violinplot(
                data=dataset1, 
                x="Nome Elo", 
                y=col, 
                dodge=False,
                cut=0,
                width=widths,
                hue=dataset1['Nome Elo'],
                ax=ax[0]
            )
            dataset2 = dataset.iloc[int(dataset.shape[0]/2)+1344:, :]
            sns.violinplot(
                data=dataset2, 
                x="Nome Elo", 
                y=col, 
                cut=0,
                dodge=False,
                width=widths,
                hue=dataset2['Nome Elo'],
                palette=sns.color_palette("hls", 4),
                ax=ax[1]
            )
            legend1 = ax[0].get_legend()
            legend2 = ax[1].get_legend()
            if legend1 or legend2:
                legend1.set_visible(False)
                legend2.set_visible(False)
            # ax[0].get_legend().set_visible(False) 
            # ax[1].get_legend().set_visible(False)   

            for i in range(0, 2):
                ax[i].set_ylabel(f'{col}', weight='bold', fontsize=13)
                ax[i].set_xlabel('Nome Elo', weight='bold', fontsize=13)
                ax[i].grid(True, alpha=0.5)

                if ax_fontsize != None:
                    ax[i].tick_params(axis='both', which='major', labelsize=ax_fontsize)
                    ax[i].tick_params(axis='both', which='minor', labelsize=ax_fontsize)

            if scenario != None:
                plt.suptitle(f'{scenario}', weight='bold', fontsize=20)

            plt.tight_layout()

            if path != None:
                plt.savefig(f'{path}/ViolinPlot_{col}_Split_2') 
            # plt.show()


    # def violin_plots(self, dataset, col, ui, split_flows=None, 
    #                 path=None, ax_fontsize=None, scenario=None):
    #     widths = 0.5

    #     self.ui.STATIC_sc.axes.clear()

    #     # Função para gerar dados no formato adequado para violinplot
    #     def prepare_violin_data(dataset, col):
    #         categories = dataset['Nome Elo'].unique()
    #         data_by_category = [dataset[dataset['Nome Elo'] == cat][col].values for cat in categories]
    #         return categories, data_by_category

    #     if split_flows == False:
    #         fig, ax = plt.subplots(1, 1, figsize=(15, 6))
    #         ax = self.ui.STATIC_sc.axes

    #         categories, data_by_category = prepare_violin_data(dataset, col)

    #         # Gerando violin plot com matplotlib
    #         ax.violinplot(data_by_category, showmeans=False, showmedians=True, widths=widths)

    #         ax.set_ylabel(f'{col}', weight='bold', fontsize=13)
    #         ax.set_xlabel('Nome Elo', weight='bold', fontsize=13)
    #         ax.grid(True, alpha=0.3)
    #         ax.set_xticks(np.arange(1, len(categories) + 1))
    #         ax.set_xticklabels(categories, rotation=30)

    #         if scenario != None:
    #             ax.set_title(f'{scenario}', weight='bold', fontsize=18)

    #         if ax_fontsize != None:
    #             ax.tick_params(axis='both', which='major', labelsize=ax_fontsize)
    #             ax.tick_params(axis='both', which='minor', labelsize=ax_fontsize)

    #         # plt.tight_layout()

    #         if path != None:
    #             plt.savefig(f'{path}/ViolinPlot_{col}_NSplit_1')
    #         # plt.show()
    #         self.ui.STATIC_sc.draw()

    #     else:
    #         fig, ax = plt.subplots(2, 1, figsize=(12, 8))
    #         # ax = self.ui.STATIC_sc.axes
    #         ax[0] = self.ui.STATIC_sc.axes

    #         # Split dataset in two parts
    #         dataset1 = dataset.iloc[:int(dataset.shape[0]/2 + 1344), :]
    #         dataset2 = dataset.iloc[int(dataset.shape[0]/2) + 1344:, :]

    #         categories1, data_by_category1 = prepare_violin_data(dataset1, col)
    #         categories2, data_by_category2 = prepare_violin_data(dataset2, col)

    #         # Primeiro violin plot (parte superior)
    #         ax[0].violinplot(data_by_category1, showmeans=False, showmedians=True, widths=widths)
    #         ax[0].set_xticks(np.arange(1, len(categories1) + 1))
    #         ax[0].set_xticklabels(categories1, rotation=30)

    #         # Segundo violin plot (parte inferior)
    #         ax[1].violinplot(data_by_category2, showmeans=False, showmedians=True, widths=widths)
    #         ax[1].set_xticks(np.arange(1, len(categories2) + 1))
    #         ax[1].set_xticklabels(categories2, rotation=30)

    #         for i in range(2):
    #             ax[i].set_ylabel(f'{col}', weight='bold', fontsize=13)
    #             ax[i].set_xlabel('Nome Elo', weight='bold', fontsize=13)
    #             ax[i].grid(True, alpha=0.5)

    #             if ax_fontsize != None:
    #                 ax[i].tick_params(axis='both', which='major', labelsize=ax_fontsize)
    #                 ax[i].tick_params(axis='both', which='minor', labelsize=ax_fontsize)

    #         if scenario != None:
    #             plt.suptitle(f'{scenario}', weight='bold', fontsize=20)

    #         # plt.tight_layout()

    #         if path != None:
    #             plt.savefig(f'{path}/ViolinPlot_{col}_Split_2')
    #         # plt.show()
    #         self.ui.STATIC_sc.draw()


    # def create_heatmap(self, dataset, col, ui, path=None, ax_fontsize=None):
    #     df_pwf_elos = dataset['Nome Elo'].unique()

    #     for k in range(len(df_pwf_elos)):
    #         df_elos = dataset

    #         if k == 0:
    #             frm = df_pwf_elos[k][-2:]
    #             to = 'T'
    #         elif k == 5:
    #             frm = df_pwf_elos[k].split('_')[1]
    #             to = 'T'
    #         else:
    #             splt1 = df_pwf_elos[k].split('_')
    #             splt2 = splt1[1].split('-')
    #             frm = splt2[0]
    #             to = splt2[1]

    #         max_day = max(sorted(list(set(df_elos['Dia']))))
    #         min_day = min(sorted(list(set(df_elos['Dia']))))
    #         n_days = len(sorted(list(set(df_elos['Dia']))))
    #         half_hour_list = sorted(list(set(df_elos['Hora'])))
    #         n_half_hour = len(half_hour_list)
    #         half_hour_periods = pd.date_range(start='2023-10-17',
    #                                         periods=n_half_hour, freq='30T').strftime('%H:%M')

    #         elo_dataset = df_elos[df_elos['Nome Elo'] == df_pwf_elos[k]]

    #         active_power = np.array(elo_dataset[col]).reshape(n_days, -1)
    #         heatmap_data = pd.DataFrame(active_power[::-1],
    #                                     index=range(max_day, min_day-1, -1),
    #                                     columns=half_hour_periods)

    #         vmax = elo_dataset[col].max()
    #         vmin = elo_dataset[col].min()

    #         neg_values = len(elo_dataset[elo_dataset[col] < 0])

    #         if vmin >= 0 or (vmin <= 0 and vmax <= 0) or neg_values < 30:
    #             cmap = plt.cm.RdYlGn
    #         else:
    #             cmap = plt.cm.seismic

    #         # Create the heatmap
    #         # fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    #         # ax = self.ui.STATIC_sc.axes

    #         # Garantindo que vmin < vcenter < vmax
    #         vcenter = 0
    #         if vmax < vcenter:
    #             vmax = vcenter + 1  # ajusta o vmax para que seja maior que vcenter
    #         if vmin > vcenter:
    #             vmin = vcenter - 1  # ajusta o vmin para que seja menor que vcenter

    #         # Create the heatmap
    #         fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    #         ax = self.ui.STATIC_sc.axes

    #         # Custom normalization to center the colormap
    #         norm = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)

    #         heatmap = ax.imshow(heatmap_data, aspect='auto', cmap=cmap, norm=norm)

    #         # Add colorbar
    #         cbar = fig.colorbar(heatmap, ax=ax)
    #         cbar.ax.tick_params(labelsize=11)
    #         cbar.ax.set_ylabel(col, size=12, weight='bold')

    #         # Set the ticks and labels
    #         ax.set_xticks(np.arange(len(half_hour_periods)))
    #         ax.set_xticklabels(half_hour_periods, rotation=45, ha="right")
    #         ax.set_yticks(np.arange(n_days))
    #         ax.set_yticklabels(range(max_day, min_day-1, -1))

    #         ax.set_xlabel('Half Hour Period', weight='bold', fontsize=12)
    #         ax.set_ylabel('Day of the Month', weight='bold', fontsize=12)
    #         ax.set_title(fr'Fluxo {frm}$\rightarrow${to}', weight='bold', fontsize=18)

    #         if ax_fontsize != None:
    #             ax.tick_params(axis='both', which='major', labelsize=ax_fontsize)
    #             ax.tick_params(axis='both', which='minor', labelsize=ax_fontsize)

    #         # plt.tight_layout()

    #         if path != None:
    #             plt.savefig(f'{path}/Heatmap_{frm}_{to}')
    #         # plt.show()



    
    # def create_heatmap(self, dataset, col, ui, path=None, ax_fontsize=None):
    #     df_pwf_elos   = dataset['Nome Elo'].unique()
    #     print(df_pwf_elos)
    #     self.ui.STATIC_sc.axes.clear()

    #     k = 0

    #     # for k in range(len(df_pwf_elos)):
    #     if k == 0:
    #         df_elos = dataset

    #         if k == 0:
    #             frm = df_pwf_elos[k][-2:]
    #             to = 'T'
    #         elif k == 5:
    #             frm = df_pwf_elos[k].split('_')[1]
    #             to  = 'T'
    #         else:
    #             splt1 = df_pwf_elos[k].split('_')
    #             splt2 = splt1[1].split('-')
    #             frm = splt2[0]
    #             to = splt2[1]
    #         print(k, frm, '->', to)

    #         max_day = max(sorted(list(set(df_elos['Dia']))))
    #         min_day = min(sorted(list(set(df_elos['Dia']))))
    #         n_days = len(sorted(list(set(df_elos['Dia']))))
    #         half_hour_list = sorted(list(set(df_elos['Hora'])))
    #         n_half_hour = len(half_hour_list)
    #         half_hour_periods = pd.date_range(start='2023-10-17', 
    #                                         periods=n_half_hour, freq='30T').strftime('%H:%M')

    #         elo_dataset = df_elos[df_elos['Nome Elo'] == df_pwf_elos[k]]

    #         active_power = np.array(elo_dataset[col]).reshape(n_days, -1)
    #         heatmap_data = pd.DataFrame(active_power[::-1], 
    #                                     index=range(max_day, min_day-1, -1), 
    #                                     columns=half_hour_periods) 

    #         vmax = elo_dataset[col].max()
    #         vmin = elo_dataset[col].min()

    #         neg_values = len(elo_dataset[elo_dataset[col] < 0])

    #         if vmin >= 0 or (vmin <= 0 and vmax <= 0) or neg_values < 30:
    #             cmap = sns.diverging_palette(230, 10, as_cmap=False)
    #         else:
    #             cmap = 'seismic'

    #         ax = self.ui.STATIC_sc.axes
    #         ax.clear()

    #         for c in ax.get_children():
    #             if isinstance(c, matplotlib.colorbar.Colorbar):
    #                 c.remove()

    #         # Verifique se o eixo já tem coleções, se sim, remova o colorbar associado
    #         if ax.collections:
    #             while ax.collections:
    #                 ax.collections[0].remove() 

    #         # Atualizar a interface de desenho para garantir que o eixo foi limpo
    #         self.ui.STATIC_sc.figure.canvas.flush_events()
    #         self.ui.STATIC_sc.figure.canvas.draw_idle() 


    #         sns.heatmap(heatmap_data, cmap=cmap, center=0, 
    #                     xticklabels=2, cbar_kws={'label': col}, 
    #                     linewidths=0.1, linecolor="white", mask=heatmap_data == 0.0, ax=ax)  
    #         cbar = ax.collections[0].colorbar
    #         cbar.ax.tick_params(labelsize=11)
    #         cbar.ax.set_ylabel(col, size=12, weight='bold')

    #         # # Defina as posições dos ticks na lista de índices desejados
    #         # ticks_positions = self.ui.STATIC_sc.axes.get_xticks()

    #         # # Ajuste os ticks na posição correta
    #         # self.ui.STATIC_sc.axes.set_xticks(ticks_positions)

    #         # # Defina a rotação dos labels dos ticks
    #         # self.ui.STATIC_sc.axes.set_xticklabels(self.ui.STATIC_sc.axes.get_xticklabels(), rotation=45)


    #         ax.set_xlabel('Half Hour Period', weight='bold', fontsize=12)
    #         ax.set_ylabel('Day of the Month', weight='bold', fontsize=12)
    #         ax.set_title(fr'Fluxo {frm}$\rightarrow${to}', weight='bold', fontsize=18)

    #         if ax_fontsize != None:
    #             ax.tick_params(axis='both', which='major', labelsize=ax_fontsize)
    #             ax.tick_params(axis='both', which='minor', labelsize=ax_fontsize)
            
    #     self.ui.STATIC_sc.draw()

    #         # plt.tight_layout()
    #         # if path != None:
    #         #     plt.savefig(f'{path}/Heatmap_{frm}_{to}')
    #         # plt.show()


    # import matplotlib.pyplot as plt

    def create_heatmap(self, dataset, col, ui, indice, path=None, ax_fontsize=None):
        df_pwf_elos = dataset['Nome Elo'].unique()
        self.ui.STATIC_sc.axes.cla()
        self.ui.STATIC_sc.fig.clf()
        self.ui.STATIC_sc.axes = self.ui.STATIC_sc.fig.add_subplot(111)

        k = indice

        df_elos = dataset

        if k == 0:
            frm = df_pwf_elos[k][-2:]
            to = 'T'
        elif k == 5:
            frm = df_pwf_elos[k].split('_')[1]
            to = 'T'
        else:
            splt1 = df_pwf_elos[k].split('_')
            splt2 = splt1[1].split('-')
            frm = splt2[0]
            to = splt2[1]
        # print(k, frm, '->', to)

        max_day = max(sorted(list(set(df_elos['Dia']))))
        min_day = min(sorted(list(set(df_elos['Dia']))))
        n_days = len(sorted(list(set(df_elos['Dia']))))
        half_hour_list = sorted(list(set(df_elos['Hora'])))
        n_half_hour = len(half_hour_list)
        half_hour_periods = pd.date_range(start='2023-10-17',
                                        periods=n_half_hour, freq='30T').strftime('%H:%M')

        elo_dataset = df_elos[df_elos['Nome Elo'] == df_pwf_elos[k]]

        active_power = np.array(elo_dataset[col]).reshape(n_days, -1)
        heatmap_data = pd.DataFrame(active_power[::-1],
                                    index=range(max_day, min_day - 1, -1),
                                    columns=half_hour_periods)

        vmax = elo_dataset[col].max()
        vmin = elo_dataset[col].min()

        neg_values = len(elo_dataset[elo_dataset[col] < 0])

        if vmin >= 0 or (vmin <= 0 and vmax <= 0) or neg_values < 30:
            cmap = sns.diverging_palette(230, 10, as_cmap=False)
        else:
            cmap = 'seismic'

        # Limpa o eixo e remove a colorbar existente
        ax = self.ui.STATIC_sc.axes

        # Gera o heatmap e armazena a referência da colorbar
        heatmap = sns.heatmap(heatmap_data, cmap=cmap, center=0,
                            xticklabels=2, cbar_kws={'label': col},
                            linewidths=0.1, linecolor="white", mask=heatmap_data == 0.0, ax=ax)

        # Armazena a referência da colorbar em um atributo da classe
        self.colorbar = heatmap.collections[0].colorbar  # Salva a referência da colorbar

        if self.colorbar is not None:
            self.colorbar.ax.tick_params(labelsize=11)
            self.colorbar.ax.set_ylabel(col, size=12, weight='bold')

        ax.set_xlabel('Half Hour Period', weight='bold', fontsize=12)
        ax.set_ylabel('Day of the Month', weight='bold', fontsize=12)
        ax.set_title(fr'Fluxo {frm}$\rightarrow${to}', weight='bold', fontsize=18)

        if ax_fontsize is not None:
            ax.tick_params(axis='both', which='major', labelsize=ax_fontsize)
            ax.tick_params(axis='both', which='minor', labelsize=ax_fontsize)


        self.ui.STATIC_sc.figure.tight_layout()
        self.ui.STATIC_sc.draw()




    def flow_profiles(self, dataset, col, scenario, path=None):
        df_pwf_elos = dataset['Nome Elo'].unique()
        fig = go.Figure(
            data=[
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[0]][col]/1000, 
                           name=df_pwf_elos[0], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[1]][col]/1000, 
                           name=df_pwf_elos[1], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[2]][col]/1000, 
                           name=df_pwf_elos[2], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[3]][col]/1000, 
                           name=df_pwf_elos[3], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[4]][col]/1000, 
                           name=df_pwf_elos[4], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[5]][col]/1000, 
                           name=df_pwf_elos[5], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[6]][col]/1000, 
                           name=df_pwf_elos[6], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[7]][col]/1000, 
                           name=df_pwf_elos[7], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[8]][col]/1000, 
                           name=df_pwf_elos[8], legend="legend"),
                go.Scatter(x=dataset.index, 
                           y=dataset[dataset['Nome Elo'] == df_pwf_elos[9]][col]/1000, 
                           name=df_pwf_elos[9], legend="legend"),
            ],   
            layout=dict(
                legend={
                    "title": f"<b>{scenario}</b>",
                    "xref": "container",
                    "yref": "container",
                    "x": 1.2,
                    "y": 0.8,
                    "orientation": "v",
                },
                
            ),
        )

        fig.update_layout(legend=dict(font=dict(family="Courier", size=20, color="black")),
                        legend_title=dict(font=dict(family="Courier", size=25, color="black")))
        fig.update_traces(visible="legendonly")
        fig.for_each_trace(lambda t: t.update(name='<b>'+ t.name +'</b>'))

        fig.update_layout(
            title_x=0.5,
            autosize=False,
            width=1800,
            height=800,
            font_family="Courier",
            xaxis_title=dict(text='<b># Operation Points</b>', font=dict(size=20, color='black')),
            yaxis_title=dict(text=f'<b>{col[0]}(GW)</b>', font=dict(size=20, color='black')),
            font_color="black",
            title=dict(text=f"<b>Flow Profiles</b>", font=dict(size=45), yref='paper')
        )

        fig.update_xaxes(ticks="outside", 
                    tickwidth=2, 
                    tickcolor='black', 
                    ticklen=5,
                    tickfont_family="Arial Black"
                    )

        fig.update_yaxes(ticks="outside", 
                    tickwidth=2, 
                    tickcolor='black', 
                    ticklen=5, 
                    tickfont_family="Arial Black"
                    )
        
        if path != None:
            fig.write_html(f"{path}/plot_flow_profiles.html")
            
        fig.show()

    def create_contourplot(self, dataset, col, ui, path=None, ax_fontsize=12):
        df_pwf_elos   = dataset['Nome Elo'].unique()

        self.ui.STATIC_sc.axes.clear()

        Dia           = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[0]]['Dia'])
        Hora          = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[0]]['Hora'])
        Fluxo_NE      = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[0]][col])
        Fluxo_NESE    = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[1]][col])
        Fluxo_NS      = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[2]][col])
        Fluxo_SULSECO = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[3]][col])
        Fluxo_NEN     = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[4]][col])
        Fluxo_RSUL    = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[5]][col])
        Elo_FOZIBIUNA = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[6]][col])
        Elo_PVELARARQ = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[7]][col])
        Elo_CPVBPVEL  = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[8]][col])
        Elo_XINGUSE   = np.array(dataset[dataset['Nome Elo'] == df_pwf_elos[9]][col])

        df_dict = {'Dia': Dia, 'Hora': Hora, df_pwf_elos[0]: Fluxo_NE, df_pwf_elos[1]: Fluxo_NESE, 
                df_pwf_elos[2]: Fluxo_NS, df_pwf_elos[3]: Fluxo_SULSECO, df_pwf_elos[4]: Fluxo_NEN,
                df_pwf_elos[5]: Fluxo_RSUL, df_pwf_elos[6]: Elo_FOZIBIUNA, df_pwf_elos[7]: Elo_PVELARARQ,
                df_pwf_elos[8]: Elo_CPVBPVEL, df_pwf_elos[9]: Elo_XINGUSE}
        df_pwf_total = pd.DataFrame(df_dict)
        df_pwf_hour = df_pwf_total[::2].reset_index().drop('index', axis=1)

        dia = np.unique(df_pwf_hour['Dia'])
        hora = np.unique(df_pwf_hour['Hora'])

        z_flows = []
        vals = []
        flow_cols = list(df_pwf_hour.columns[2:])

        for j in range(0, len(flow_cols)):
            lst = []
            for i in range(0, 673):
                if i % 24 == 0 and i != 0:
                    lst.append(vals)
                    vals = []
                
                if i == 672:
                    break
                vals.append(df_pwf_hour[flow_cols[j]][i])
            z_flows.append(lst)


        for k in range(len(df_pwf_elos)):

            if k == 0:
                frm = df_pwf_elos[k][-2:]
                to = 'T'
            elif k == 5:
                frm = df_pwf_elos[k].split('_')[1]
                to  = 'T'
            else:
                splt1 = df_pwf_elos[k].split('_')
                splt2 = splt1[1].split('-')
                frm = splt2[0]
                to = splt2[1]

            fig, ax = plt.subplots(1, 1, figsize=(12, 6))
            ax = self.ui.STATIC_sc.axes

            norm   = TwoSlopeNorm(0)
            contour = ax.contourf(hora, dia[::-1], np.array(z_flows[k][::-1]), 20, 
                                cmap='RdBu_r', 
                                extend='max', 
                                norm=norm)

            cbar1 = plt.colorbar(contour, ax=ax)
            cbar1.formatter.set_powerlimits((3, 3))
            cbar1.formatter.set_useMathText(True)
            cbar1.ax.set_ylabel(f'{col}', rotation=90, weight='bold', size=12)

            ax.set_xlabel("Hour", weight='bold', fontsize=ax_fontsize)
            ax.set_ylabel("Day", weight='bold', fontsize=ax_fontsize)
            ax.set_yticks(np.arange(min(dia), max(dia)+1))
            ax.set_xticks(np.arange(0, 24))
            ax.set_xticklabels(hora, rotation=45)
            ax.set_title(fr'Fluxo {frm}$\rightarrow${to}', weight='bold', fontsize=18)

            if ax_fontsize != None:
                ax.tick_params(axis='both', which='major', labelsize=ax_fontsize)
                ax.tick_params(axis='both', which='minor', labelsize=ax_fontsize)

            self.ui.STATIC_sc.draw()

            # plt.tight_layout()

            # if path != None:
            #     plt.savefig(f'{path}/ContourPlot_{frm}_{to}')
            # plt.show()  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap



class GUI_Plotter():
    def __init__(self, data, plot, ui):

        self.data = data
        self.plot = plot
        self.ui   = ui


    def update(self):

        self.ui.DYNAMIC_sc.axes.cla()
        self.ui.DYNAMIC_sc.fig.clf()

        self.ui.DYNAMIC_sc.axes = self.ui.DYNAMIC_sc.fig.add_subplot(111)

        

        temp = self.data.copy()


        # Change the Data to Plot

        if self.plot['filter'] is not None:
            temp = self.filter_data(temp, self.plot)

        if self.plot['round'] is not None and self.plot['round'] != '':
            temp[self.plot['x']] = temp[self.plot['x']].round(int(self.plot['round']))    

        if self.plot['stat'] is not None and self.plot['stat'] != '':
            temp = self.select_group_by(temp, self.plot)


        # Plot the data

        if self.plot['plot'] == 'Scatter':
            self.scatter(temp, self.plot, self.ui)


        elif self.plot['plot'] == 'Line':
            self.line(temp, self.plot, self.ui)   


        # Features

        self.ui.DYNAMIC_sc.axes.set_xlabel(self.plot['x_label'] if self.plot['x_label'] is not None else self.plot['x'])
        self.ui.DYNAMIC_sc.axes.set_ylabel(self.plot['y_label'] if self.plot['y_label'] is not None else self.plot['y'])

        
        unique_y = temp[self.plot['y']].unique()

        try:
            if np.array_equal(temp[self.plot['y']], temp[self.plot['y']].astype(int)) and len(unique_y) <= 30:            
                self.ui.DYNAMIC_sc.axes.set_yticks([i for i in unique_y], [i for i in unique_y])       
        except:
            pass         

        
        y, x, c = self.plot['y'], self.plot['x'], self.plot['c']

        if self.plot['c'] is not None and self.plot['c'] != '':
            self.ui.DYNAMIC_sc.axes.set_title(f'{y} x {x} per {c}')
        else:
            self.ui.DYNAMIC_sc.axes.set_title(f'{y} x {x}')


        self.ui.DYNAMIC_sc.draw()


    def select_group_by(self, data, plot):

        if plot['stat'] == 'Mean':
            if plot['c'] is not None and self.plot['c'] != '':
                return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].mean()
            else:
                return data.groupby([plot['x']], as_index=False)[plot['y']].mean()
            

        if plot['stat'] == 'Std':
            if plot['c'] is not None and self.plot['c'] != '':
                return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].std()
            else:
                return data.groupby([plot['x']], as_index=False)[plot['y']].std()
            
        if plot['stat'] == 'Sum':
            if plot['c'] is not None and self.plot['c'] != '':
                return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].sum()
            else:
                return data.groupby([plot['x']], as_index=False)[plot['y']].sum()




    def filter_data(self, data, plot):


        for var, signal, threshold in plot['filter']:

            if signal == '>':
                data = data[data[var] > threshold]

            elif signal == '>=':
                data = data[data[var] >= threshold]

            elif signal == '<':
                data = data[data[var] < threshold]

            elif signal == '<=':
                data = data[data[var] <= threshold]

            elif signal == '==':
                data = data[data[var] == threshold]

            elif signal == 'List':
                data = data[data[var].isin(threshold)]

            elif signal == 'not_NaN':
                data = data[~data[var].isna()]

            elif signal == 'NaN':
                data = data[data[var].isna()]

        return data





    def scatter(self, data, plot, ui):

        scat   = data.copy()
        colors = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']
        

        if plot['c'] is not None and self.plot['c'] != '':

            x, y, c = scat[plot['x']], scat[plot['y']], scat[plot['c']]

            try:
                inter, stringer = np.array_equal(c, c.astype(int)), False
            except:
                inter, stringer = False, True

            if (inter or stringer) and len(c.unique()) <= 20: 
            
                cmap    = LinearSegmentedColormap.from_list('my_list', colors[:len(c.unique())], N=len(c.unique()))      
                points  = ui.DYNAMIC_sc.axes.scatter(x, y, c=c, cmap=cmap)

                ui.DYNAMIC_sc.fig.colorbar(points, ticks=[c.unique()[i] for i in range(0, len(c.unique()))])     

            else:
                cmap    = LinearSegmentedColormap.from_list('my_list', colors[:10], N=10)      
                points  = ui.DYNAMIC_sc.axes.scatter(x, y, c=c, cmap=cmap)

                ui.DYNAMIC_sc.fig.colorbar(points, ticks=[i*(c.max()/10) for i in range(0, 11)])     


        else:
            x, y, c = scat[plot['x']], scat[plot['y']], None

            ui.DYNAMIC_sc.axes.scatter(x, y, c=c)



    def line(self, data, plot, ui):

        if plot['c'] is not None and self.plot['c'] != '':
            for c in data[plot['c']].unique():

                f    = data[plot['c']] == c
                x, y = data[f][plot['x']], data[f][plot['y']]

                ui.DYNAMIC_sc.axes.plot(x, y, label=c)

        else:

            x, y = data[plot['x']], data[plot['y']]

            ui.DYNAMIC_sc.axes.plot(x, y)


# class GUI_Plotter_STATIC():
#     def __init__(self, data, plot, ui, labels=None, title=None, xlabel=None, ylabel=None, limites=None, vert = True, rotation = 0, text = True, nbarra = None):

#         self.data = data
#         self.plot = plot
#         self.ui   = ui
#         self.labels = labels
#         self.title = title
#         self.xlabel = xlabel
#         self.ylabel = ylabel
#         self.limites = limites
#         self.vert = vert
#         self.rotation = rotation
#         self.text = text
#         self.nbarra = nbarra


#     def update(self):

#         self.ui.STATIC_sc.axes.cla()
#         self.ui.STATIC_sc.fig.clf()

#         self.ui.STATIC_sc.axes = self.ui.STATIC_sc.fig.add_subplot(111)

#         self.ui.STATIC_sc.axes.grid(True)

        

#         temp = self.data.copy()


#         # Change the Data to Plot

#         # if self.plot['filter'] is not None:
#         #     temp = self.filter_data(temp, self.plot)

#         # if self.plot['round'] is not None and self.plot['round'] != '':
#         #     temp[self.plot['x']] = temp[self.plot['x']].round(int(self.plot['round']))    

#         if self.plot['stat'] is not None and self.plot['stat'] != '':
#             temp = self.select_group_by(temp, self.plot)


#         # Plot the data

#         if self.plot['plot'] == 'Scatter':
#             self.scatter(temp, self.plot, self.ui)

#         elif self.plot['plot'] == 'Line':
#             self.line(temp, self.plot, self.ui) 

#         elif self.plot['plot'] == 'Boxplot':
#             self.boxplot(temp, self.plot, self.ui, self.labels, self.title, self.xlabel, self.ylabel, self.limites, self.vert, self.rotation, self.text, self.nbarra)   


#         # Features

#         self.ui.STATIC_sc.axes.set_xlabel(self.plot['x_label'] if self.plot['x_label'] is not None else self.plot['x'])
#         self.ui.STATIC_sc.axes.set_ylabel(self.plot['y_label'] if self.plot['y_label'] is not None else self.plot['y'])

#         if self.plot['plot'] == 'Line':
#             unique_y = temp[self.plot['y']].unique()

#             try:
#                 if np.array_equal(temp[self.plot['y']], temp[self.plot['y']].astype(int)) and len(unique_y) <= 30:            
#                     self.ui.STATIC_sc.axes.set_yticks([i for i in unique_y], [i for i in unique_y])       
#             except:
#                 pass         

        
#             y, x, c = self.plot['y'], self.plot['x'], self.plot['c']

#             if self.plot['c'] is not None and self.plot['c'] != '':
#                 self.ui.STATIC_sc.axes.set_title(f'{y} x {x} per {c}')
#             else:
#                 self.ui.STATIC_sc.axes.set_title(f'{y} x {x}')


#         self.ui.STATIC_sc.draw()


#     def select_group_by(self, data, plot):

#         if plot['stat'] == 'Mean':
#             if plot['c'] is not None and self.plot['c'] != '':
#                 return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].mean()
#             else:
#                 return data.groupby([plot['x']], as_index=False)[plot['y']].mean()
            

#         if plot['stat'] == 'Std':
#             if plot['c'] is not None and self.plot['c'] != '':
#                 return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].std()
#             else:
#                 return data.groupby([plot['x']], as_index=False)[plot['y']].std()
            
#         if plot['stat'] == 'Sum':
#             if plot['c'] is not None and self.plot['c'] != '':
#                 return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].sum()
#             else:
#                 return data.groupby([plot['x']], as_index=False)[plot['y']].sum()



    
#     def boxplot(self, data, plot, ui, labels, title, xlabel, ylabel, limites=None, vert=True, rotation=0, text=True, nbarra=None):
    
#         markerfacecolor = dict(markerfacecolor='gray', marker='o')
    
        
#         if vert:
#             ui.STATIC_sc.axes.boxplot(data, flierprops=markerfacecolor)
#             ui.STATIC_sc.axes.tick_params(bottom=False, left=False)
#             ui.STATIC_sc.axes.set_axisbelow(True)
            
#             if text:
#                 for i, data_item in enumerate(data):
#                     num_muestras = len(data_item)
#                     if num_muestras > 0: 
#                         try:
#                             ui.STATIC_sc.axes.text(i+1, np.max(data_item)+0.005, f'Buses = {nbarra[i].size} ', ha='center', va='bottom', size=7)
#                             ui.STATIC_sc.axes.text(i+1, np.median(data_item), f' {np.mean(data_item):.3f} ', ha='center', va='bottom', size=7)
#                             ui.STATIC_sc.axes.text(i+1.4, np.quantile(data_item, q=0.25), f' {np.quantile(data_item, q=0.25):.3f} ', ha='center', va='bottom', size=7)
#                             ui.STATIC_sc.axes.text(i+1.4, np.quantile(data_item, q=0.75), f' {np.quantile(data_item, q=0.75):.3f} ', ha='center', va='bottom', size=7)
#                         except:
#                             ui.STATIC_sc.axes.text(i+1.4, np.mean(data_item), f'{num_muestras}', ha='center', va='bottom', size=12)
            
#             if limites is not None:
#                 ui.STATIC_sc.axes.set_ylim(limites)
            
#             # Configurar os ticks e rótulos
#             ui.STATIC_sc.axes.set_xticks(range(1, len(labels) + 1))
#             ui.STATIC_sc.axes.set_xticklabels(labels, fontsize=10, rotation=rotation)

#         else:
#             ui.STATIC_sc.axes.boxplot(data, vert=False, flierprops=markerfacecolor)
#             if limites is not None:
#                 ui.STATIC_sc.axes.set_xlim(limites)
#                 ui.STATIC_sc.axes.set_xticks(np.linspace(limites[0], limites[1], 20))

#             if text:
#                 ui.STATIC_sc.axes.text(np.median(data), 1.1, f' {np.mean(data):.3f} ', ha='center', va='bottom', size=10)

#         # Reduzir tamanhos das fontes para os eixos e título
#         ui.STATIC_sc.axes.set_xlabel(xlabel, fontsize=12)
#         ui.STATIC_sc.axes.set_ylabel(ylabel, fontsize=12)
#         ui.STATIC_sc.axes.set_title(title, fontsize=14)
        
#         # Configurar o tamanho da fonte dos yticks
#         ui.STATIC_sc.axes.tick_params(axis='y', labelsize=10)
        
#         ui.STATIC_sc.axes.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
#         ui.STATIC_sc.axes.xaxis.grid(False)



#     def line(self, data, plot, ui):

#         if plot['c'] is not None and plot['c'] != '':

#             for regiao in plot['reg']:

#                 # Filtra para uma região específica e plota somente ela
#                 # f    = (data[plot['c']] == plot['reg'])
#                 f    = (data[plot['c']] == regiao)
#                 x, y = data[f][plot['x']], data[f][plot['y']]

#                 # ui.STATIC_sc.axes.plot(x, y, label=plot['reg'], lw=2.5)
#                 ui.STATIC_sc.axes.plot(x, y, label=regiao, lw=2.5)
#                 ui.STATIC_sc.axes.legend(loc='upper right', fontsize=9)

#                 if plot['x'] == 'key':
#                         data_points_per_day = 48
#                         num_days = (len(data[plot['x']]) // len(data[plot['c']].unique())) // data_points_per_day
#                         ui.STATIC_sc.axes.set_xticks([i * data_points_per_day for i in range(num_days)])
#                         ui.STATIC_sc.axes.set_xticklabels([f'Day {i+1}' for i in range(num_days)], fontsize=10, rotation=45, ha='right')


#         else:

#             # Plota sem filtrar por regiões ou categorias
#             x, y = data[plot['x']], data[plot['y']]
#             ui.STATIC_sc.axes.plot(x, y, lw=2.5)

#             if plot['x'] == 'key':
#                 data_points_per_day = 48
#                 num_days = len(data[plot['x']]) // data_points_per_day
#                 ui.STATIC_sc.axes.set_xticks([i * data_points_per_day for i in range(num_days)])
#                 ui.STATIC_sc.axes.set_xticklabels([f'Day {i+1}' for i in range(num_days)], fontsize=10, rotation=45, ha='right')





class GUI_Plotter_STATIC():
    def __init__(self, data, plot, ui, labels=None, title=None, xlabel=None, ylabel=None, limites=None, vert = True, rotation = 0, text = True, nbarra = None):

        self.data = data
        self.plot = plot
        self.ui   = ui
        self.labels = labels
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.limites = limites
        self.vert = vert
        self.rotation = rotation
        self.text = text
        self.nbarra = nbarra


    def update(self):

        self.ui.STATIC_sc.axes.cla()
        self.ui.STATIC_sc.fig.clf()

        self.ui.STATIC_sc.axes = self.ui.STATIC_sc.fig.add_subplot(111)

        self.ui.STATIC_sc.axes.grid(True)

        

        temp = self.data.copy()


        # Change the Data to Plot

        # if self.plot['filter'] is not None:
        #     temp = self.filter_data(temp, self.plot)

        # if self.plot['round'] is not None and self.plot['round'] != '':
        #     temp[self.plot['x']] = temp[self.plot['x']].round(int(self.plot['round']))    

        if self.plot['stat'] is not None and self.plot['stat'] != '':
            temp = self.select_group_by(temp, self.plot)


        # Plot the data

        if self.plot['plot'] == 'Scatter':
            self.scatter(temp, self.plot, self.ui)

        elif self.plot['plot'] == 'Line':
            self.line(temp, self.plot, self.ui) 

        elif self.plot['plot'] == 'Boxplot':
            self.boxplot(temp, self.plot, self.ui, self.labels, self.title, self.xlabel, self.ylabel, self.limites, self.vert, self.rotation, self.text, self.nbarra)   


        # Features

        self.ui.STATIC_sc.axes.set_xlabel(self.plot['x_label'] if self.plot['x_label'] is not None else self.plot['x'])
        self.ui.STATIC_sc.axes.set_ylabel(self.plot['y_label'] if self.plot['y_label'] is not None else self.plot['y'])

        if self.plot['plot'] == 'Line':
            unique_y = temp[self.plot['y']].unique()

            try:
                if np.array_equal(temp[self.plot['y']], temp[self.plot['y']].astype(int)) and len(unique_y) <= 30:            
                    self.ui.STATIC_sc.axes.set_yticks([i for i in unique_y], [i for i in unique_y])       
            except:
                pass         

        
            y, x, c = self.plot['y'], self.plot['x'], self.plot['c']

            if self.plot['c'] is not None and self.plot['c'] != '':
                self.ui.STATIC_sc.axes.set_title(f'{y} x {x} per {c}')
            else:
                self.ui.STATIC_sc.axes.set_title(f'{y} x {x}')


        self.ui.STATIC_sc.draw()


    # def select_group_by(self, data, plot):

    #     if plot['stat'] == 'Mean':
    #         if plot['c'] is not None and self.plot['c'] != '':
    #             return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].mean()
    #         else:
    #             return data.groupby([plot['x']], as_index=False)[plot['y']].mean()
            

    #     if plot['stat'] == 'Std':
    #         if plot['c'] is not None and self.plot['c'] != '':
    #             return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].std()
    #         else:
    #             return data.groupby([plot['x']], as_index=False)[plot['y']].std()
            
    #     if plot['stat'] == 'Sum':
    #         if plot['c'] is not None and self.plot['c'] != '':
    #             return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].sum()
    #         else:
    #             return data.groupby([plot['x']], as_index=False)[plot['y']].sum()



    
    def boxplot(self, data, plot, ui, labels, title, xlabel, ylabel, limites=None, vert=True, rotation=0, text=True, nbarra=None):
    
        markerfacecolor = dict(markerfacecolor='gray', marker='o')
    
        
        if vert:
            ui.STATIC_sc.axes.boxplot(data, flierprops=markerfacecolor)
            ui.STATIC_sc.axes.tick_params(bottom=False, left=False)
            ui.STATIC_sc.axes.set_axisbelow(True)
            
            if text:
                for i, data_item in enumerate(data):
                    num_muestras = len(data_item)
                    if num_muestras > 0: 
                        try:
                            ui.STATIC_sc.axes.text(i+1, np.max(data_item)+0.005, f'Buses = {nbarra[i].size} ', ha='center', va='bottom', size=7)
                            ui.STATIC_sc.axes.text(i+1, np.median(data_item), f' {np.mean(data_item):.3f} ', ha='center', va='bottom', size=7)
                            ui.STATIC_sc.axes.text(i+1.4, np.quantile(data_item, q=0.25), f' {np.quantile(data_item, q=0.25):.3f} ', ha='center', va='bottom', size=7)
                            ui.STATIC_sc.axes.text(i+1.4, np.quantile(data_item, q=0.75), f' {np.quantile(data_item, q=0.75):.3f} ', ha='center', va='bottom', size=7)
                        except:
                            ui.STATIC_sc.axes.text(i+1.4, np.mean(data_item), f'{num_muestras}', ha='center', va='bottom', size=12)
            
            if limites is not None:
                ui.STATIC_sc.axes.set_ylim(limites)
            
            # Configurar os ticks e rótulos
            ui.STATIC_sc.axes.set_xticks(range(1, len(labels) + 1))
            ui.STATIC_sc.axes.set_xticklabels(labels, fontsize=10, rotation=rotation)

        else:
            ui.STATIC_sc.axes.boxplot(data, vert=False, flierprops=markerfacecolor)
            if limites is not None:
                ui.STATIC_sc.axes.set_xlim(limites)
                ui.STATIC_sc.axes.set_xticks(np.linspace(limites[0], limites[1], 20))

            if text:
                ui.STATIC_sc.axes.text(np.median(data), 1.1, f' {np.mean(data):.3f} ', ha='center', va='bottom', size=10)

        # Reduzir tamanhos das fontes para os eixos e título
        ui.STATIC_sc.axes.set_xlabel(xlabel, fontsize=12)
        ui.STATIC_sc.axes.set_ylabel(ylabel, fontsize=12)
        ui.STATIC_sc.axes.set_title(title, fontsize=14)
        
        # Configurar o tamanho da fonte dos yticks
        ui.STATIC_sc.axes.tick_params(axis='y', labelsize=10)
        
        ui.STATIC_sc.axes.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
        ui.STATIC_sc.axes.xaxis.grid(False)



    def line(self, data, plot, ui):

        if plot['c'] is not None and plot['c'] != '':

            for regiao in plot['reg']:

                # Filtra para uma região específica e plota somente ela
                # f    = (data[plot['c']] == plot['reg'])
                f    = (data[plot['c']] == regiao)
                x, y = data[f][plot['x']], data[f][plot['y']]

                # ui.STATIC_sc.axes.plot(x, y, label=plot['reg'], lw=2.5)
                ui.STATIC_sc.axes.plot(x, y, label=regiao, lw=2.5)
                ui.STATIC_sc.axes.legend(loc='upper right', fontsize=9)

                if plot['x'] == 'key':
                        data_points_per_day = 48
                        num_days = (len(data[plot['x']]) // len(data[plot['c']].unique())) // data_points_per_day
                        ui.STATIC_sc.axes.set_xticks([i * data_points_per_day for i in range(num_days)])
                        ui.STATIC_sc.axes.set_xticklabels([f'Day {i+1}' for i in range(num_days)], fontsize=10, rotation=45, ha='right')


        else:

            # Plota sem filtrar por regiões ou categorias
            x, y = data[plot['x']], data[plot['y']]
            ui.STATIC_sc.axes.plot(x, y, lw=2.5)

            if plot['x'] == 'key':
                data_points_per_day = 48
                num_days = len(data[plot['x']]) // data_points_per_day
                ui.STATIC_sc.axes.set_xticks([i * data_points_per_day for i in range(num_days)])
                ui.STATIC_sc.axes.set_xticklabels([f'Day {i+1}' for i in range(num_days)], fontsize=10, rotation=45, ha='right')


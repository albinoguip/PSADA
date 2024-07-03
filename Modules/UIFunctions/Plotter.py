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


        elif self.plot['plot'] == 'Violin':
            self.violin(temp, self.plot, self.ui)   


        # Features

        self.ui.DYNAMIC_sc.axes.set_xlabel(self.plot['x_label'] if self.plot['x_label'] is not None else self.plot['x'])
        self.ui.DYNAMIC_sc.axes.set_ylabel(self.plot['y_label'] if self.plot['y_label'] is not None else self.plot['y'])

        
        unique_y = temp[self.plot['y']].unique()
        unique_x = temp[self.plot['x']].unique()

        try:
            if np.array_equal(temp[self.plot['y']], temp[self.plot['y']].astype(int)) and len(unique_y) <= 30:            
                self.ui.DYNAMIC_sc.axes.set_yticks([i for i in unique_y], [i for i in unique_y])       
        except:
            pass       


        try:
            if np.array_equal(temp[self.plot['x']], temp[self.plot['x']].astype(int)) and len(unique_x) <= 30:            
                self.ui.DYNAMIC_sc.axes.set_xticks([i for i in unique_x], [i for i in unique_x])       
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



    def violin(self, data, plot, ui):

        # Has Not_NaN Built-in

        x, y = data[plot['x']], data[plot['y']]

        var_list, labels = [], []
        for idx, x_unique in enumerate(sorted(x.unique())):

            est = data[data[plot['x']] == x_unique]

            var_list.append(est[~est[plot['y']].isna()][plot['y']].values)
            labels.append(x_unique)

        ui.DYNAMIC_sc.axes.violinplot(var_list, showmeans=True, showmedians=True)







if __name__ == '__main__':

    path = 'C:/Users/Scarlet/Desktop/arrumar2/rev2_Remaneja Sto Antonio e Jirau/vars.csv'
    data = pd.read_csv(path)

    plot = {'x' : 'Dia',
            'y' : 'Hora',
            'c' : 'A_RCFC',

            'plot'  : 'Scatter',
            'round' : None,
            'stat'  : None,

            'x_label' : 'Carga da Ilha 1',
            'y_label' : None,
            'legend'  : None,

            'filter' : [('Contigence', 'List', [1]),  #, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
                        ('A_RCFC', 'not_NaN', 2),
                        ('A_RCFC', '<=', 0.04)
                        ]

            }
    
    # for col in data.columns:
    #     print(col)

    
    
    plot_from_json(data, plot)
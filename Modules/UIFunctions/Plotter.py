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


        

        # Plot the data

        if self.plot['plot'] == 'Scatter':
            self.scatter(temp, self.plot, self.ui)


        elif self.plot['plot'] == 'Line':
            self.line(temp, self.plot, self.ui)  


        elif self.plot['plot'] == 'Violin':
            self.violin(temp, self.plot, self.ui)   

        elif self.plot['plot'] == 'HeatMap':
            self.heatmap(temp, self.plot, self.ui)

        elif self.plot['plot'] == 'Bar':
            self.barplot(temp, self.plot, self.ui)   


        # Features

        self.ui.DYNAMIC_sc.axes.set_xlabel(self.plot['x_label'] if self.plot['x_label'] is not None else self.plot['x'])
        self.ui.DYNAMIC_sc.axes.set_ylabel(self.plot['y_label'] if self.plot['y_label'] is not None else self.plot['y'])        


        
        y, x, c = self.plot['y'], self.plot['x'], self.plot['c']

        if self.plot['c'] is not None and self.plot['c'] != '':
            self.ui.DYNAMIC_sc.axes.set_title(f'{y} x {x} per {c}')
        else:
            self.ui.DYNAMIC_sc.axes.set_title(f'{y} x {x}')


        self.ui.DYNAMIC_sc.draw()





    def select_group_by(self, data, plot, x, y, c):

        if plot['stat'] == 'Mean':
            if c is not None and c != '':
                return data.groupby([x, c], as_index=False)[y].mean()
            else:
                return data.groupby([x], as_index=False)[y].mean()
            

        if plot['stat'] == 'Std':
            if c is not None and c != '':
                return data.groupby([x, c], as_index=False)[y].std()
            else:
                return data.groupby([x], as_index=False)[y].std()
            
        if plot['stat'] == 'Sum':
            if c is not None and c != '':
                return data.groupby([x, c], as_index=False)[y].sum()
            else:
                return data.groupby([x], as_index=False)[y].sum()
            

        if plot['stat'] == 'Count':
            if c is not None and c != '':
                return data.groupby([x, c], as_index=False)[y].count()
            else:
                return data.groupby([x], as_index=False)[y].count()




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

            elif signal == '!=':
                data = data[data[var] != threshold]

            elif signal == '==':
                data = data[data[var] == threshold]

            elif signal == 'List':
                data = data[data[var].isin(threshold)]

            elif signal == 'not_NaN':
                data = data[~data[var].isna()]

            elif signal == 'NaN':
                data = data[data[var].isna()]

        return data


    ### SCATTER
    #####################################################################################################################

    def scatter(self, data, plot, ui):


        # Change the Data to Plot

        if self.plot['filter'] is not None:
            data = self.filter_data(data, self.plot)

        if self.plot['round'] is not None and self.plot['round'] != '':
            data[self.plot['x']] = data[self.plot['x']].round(int(self.plot['round']))    

        if self.plot['stat'] is not None and self.plot['stat'] != '':
            data = self.select_group_by(data, self.plot, plot['x'], plot['y'], plot['c'])


        # Create Plot

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


        # Adjusting Labels

        unique_y = data[self.plot['y']].unique()
        unique_x = data[self.plot['x']].unique()

        try:
            if np.array_equal(data[self.plot['y']], data[self.plot['y']].astype(int)) and len(unique_y) <= 30:            
                self.ui.DYNAMIC_sc.axes.set_yticks([i for i in unique_y], [i for i in unique_y])       
        except:
            pass  

        try:
            if np.array_equal(data[self.plot['x']], data[self.plot['x']].astype(int)) and len(unique_x) <= 30:            
                self.ui.DYNAMIC_sc.axes.set_xticks([i for i in unique_x], [i for i in unique_x])       
        except:
            pass    





    ### LINE
    #####################################################################################################################

    def line(self, data, plot, ui):

        # Change the Data to Plot

        if self.plot['filter'] is not None:
            data = self.filter_data(data, self.plot)

        if self.plot['round'] is not None and self.plot['round'] != '':
            data[self.plot['x']] = data[self.plot['x']].round(int(self.plot['round']))    

        if self.plot['stat'] is not None and self.plot['stat'] != '':
            data = self.select_group_by(data, self.plot, plot['x'], plot['y'], plot['c'])


        # Create Plot

        if plot['c'] is not None and self.plot['c'] != '':
            for c in data[plot['c']].unique():

                f    = data[plot['c']] == c
                x, y = data[f][plot['x']], data[f][plot['y']]

                ui.DYNAMIC_sc.axes.plot(x, y, label=c)

        else:

            x, y = data[plot['x']], data[plot['y']]

            ui.DYNAMIC_sc.axes.plot(x, y)


        # Adjusting Labels

        unique_y = data[self.plot['y']].unique()
        unique_x = data[self.plot['x']].unique()

        try:
            if np.array_equal(data[self.plot['y']], data[self.plot['y']].astype(int)) and len(unique_y) <= 30:            
                self.ui.DYNAMIC_sc.axes.set_yticks([i for i in unique_y], [i for i in unique_y])       
        except:
            pass  

        try:
            if np.array_equal(data[self.plot['x']], data[self.plot['x']].astype(int)) and len(unique_x) <= 30:            
                self.ui.DYNAMIC_sc.axes.set_xticks([i for i in unique_x], [i for i in unique_x])       
        except:
            pass    





    ### VIOLIN
    #####################################################################################################################

    def violin(self, data, plot, ui):

        # Change the Data to Plot

        if self.plot['filter'] is not None:
            data = self.filter_data(data, self.plot)

        if self.plot['round'] is not None and self.plot['round'] != '':
            data[self.plot['x']] = data[self.plot['x']].round(int(self.plot['round']))    

        if self.plot['stat'] is not None and self.plot['stat'] != '':
            data = self.select_group_by(data, self.plot, plot['x'], plot['y'], plot['c'])


        # Create Plot
        # Has Not_NaN Built-in

        x, y = data[plot['x']], data[plot['y']]

        var_list, labels = [], []
        for idx, x_unique in enumerate(sorted(x.unique())):

            est = data[data[plot['x']] == x_unique]

            var_list.append(est[~est[plot['y']].isna()][plot['y']].values)
            labels.append(x_unique)

        ui.DYNAMIC_sc.axes.violinplot(var_list, showmeans=True, showmedians=True)


        # Adjusting Labels

        self.ui.DYNAMIC_sc.axes.set_xticks([i for i in range(1, len(labels)+1)], labels, rotation=45) 
    




    ### HEATMAP
    #####################################################################################################################

    def heatmap(self, data, plot, ui):


        # Change the Data to Plot

        if self.plot['filter'] is not None:
            data = self.filter_data(data, self.plot)

        if self.plot['round'] is not None and self.plot['round'] != '':
            data[self.plot['x']] = data[self.plot['x']].round(int(self.plot['round']))    

        if self.plot['stat'] is not None and self.plot['stat'] != '':
            data = self.select_group_by(data, self.plot, plot['x'], plot['c'], plot['y'])

        # Create Plot

        scat   = data[[plot['x'], plot['y'], plot['c']]].copy()
        colors = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']

        scat[plot['x']] = scat[plot['x']].astype('str')
        scat[plot['y']] = scat[plot['y']].astype('str')
        

        x, y, c = scat[plot['x']], scat[plot['y']], scat[plot['c']]
        
        try:
            inter, stringer = np.array_equal(c, c.astype(int)), False
        except:
            inter, stringer = False, True


        if len(c.unique()) == 1:
            points  = ui.DYNAMIC_sc.axes.scatter(x, y, marker='s')


        elif (inter or stringer) and len(c.unique()) <= 20: 
        
            cmap    = LinearSegmentedColormap.from_list('my_list', colors[:len(c.unique())], N=len(c.unique()))      
            points  = ui.DYNAMIC_sc.axes.scatter(x, y, c=c, cmap=cmap, marker='s')

            ui.DYNAMIC_sc.fig.colorbar(points, ticks=[c.unique()[i] for i in range(0, len(c.unique()))])     

        else:
            cmap    = LinearSegmentedColormap.from_list('my_list', colors[:10], N=10)      
            points  = ui.DYNAMIC_sc.axes.scatter(x, y, c=c, cmap=cmap, marker='s')

            ui.DYNAMIC_sc.fig.colorbar(points, ticks=[i*(c.max()/10) for i in range(0, 11)])  

        # Adjusting Labels

        unique_y = scat[self.plot['y']].unique()
        self.ui.DYNAMIC_sc.axes.set_yticks([i for i in range(len(unique_y))], [i for i in unique_y]) 

        unique_x = scat[self.plot['x']].unique()
        self.ui.DYNAMIC_sc.axes.set_xticks([i for i in range(len(unique_x))], [i for i in unique_x], rotation=90)    

        self.ui.DYNAMIC_sc.axes.grid()



    ### BARPLOT
    #####################################################################################################################

    def barplot(self, data, plot, ui):


        # Change the Data to Plot

        if self.plot['filter'] is not None:
            data = self.filter_data(data, self.plot)

        if self.plot['round'] is not None and self.plot['round'] != '':
            data[self.plot['x']] = data[self.plot['x']].round(int(self.plot['round']))    

        if self.plot['stat'] is not None and self.plot['stat'] != '':
            data = self.select_group_by(data, self.plot, plot['x'], plot['y'], None)

        # Create Plot


        scat   = data[[plot['x'], plot['y']]].copy()
        colors = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']

        scat[plot['x']] = scat[plot['x']].astype('str')
        # scat[plot['y']] = scat[plot['y']].astype('str')
        

        x, y = scat[plot['x']], scat[plot['y']]


        ui.DYNAMIC_sc.axes.bar(x, y)

        # Adjusting Labels

        unique_x = scat[self.plot['x']].unique()
        if len(unique_x) > 10:
            self.ui.DYNAMIC_sc.axes.set_xticks([i for i in range(len(unique_x))], [i for i in unique_x], rotation=90)    
        else:
            self.ui.DYNAMIC_sc.axes.set_xticks([i for i in range(len(unique_x))], [i for i in unique_x])







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
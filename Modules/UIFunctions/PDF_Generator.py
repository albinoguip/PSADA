import pandas as pd
import numpy  as np

import matplotlib.pyplot as plt
from   matplotlib.colors import LinearSegmentedColormap

import os, sys, tempfile, re, json

from fpdf import FPDF


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class Plotter():
    def __init__(self, data, plot):

        self.data = data
        self.plot = plot


    def plot_from_json(self, data, plot, leng):  

        temp = data.copy()

        if leng == 1:
            fig = plt.figure(figsize=(12, 6), dpi=200)

        elif leng == 2:
            fig = plt.figure(figsize=(9, 6), dpi=200)

        elif leng == 3:
            fig = plt.figure(figsize=(8, 6), dpi=200)

        

        # Plot the data

        if plot['plot'] == 'Scatter':
            self.scatter(temp, plot)


        elif plot['plot'] == 'Line':
            self.line(temp, plot) 


        elif plot['plot'] == 'Violin':
            self.violin(temp, plot)   

        elif plot['plot'] == 'HeatMap':
            self.heatmap(temp, plot)  

        elif plot['plot'] == 'Bar':
            self.barplot(temp, plot)  


        


        y, x, c = plot['y'], plot['x'], plot['c']
        s, r    = plot['stat'], plot['round']
        title   = f'{y} x {x}'

        

        if (plot['stat'] is not None and plot['stat'] != '') & (plot['round'] is not None and plot['round'] != ''):
            title = title + f' [{s}  / (Rnd: {r})]'

        if (not (plot['stat'] is not None and plot['stat'] != '')) & (plot['round'] is not None and plot['round'] != ''):
            title = title + f'(Rnd: {r})'

        if (plot['stat'] is not None and plot['stat'] != '') & (not (plot['round'] is not None and plot['round'] != '')):
            title = title + f' [{s}]'

        if plot['c'] is not None and plot['c'] != '':
            title = title + f' per {c}'

        plt.title(title)

        plt.close()

        return fig




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





    def scatter(self, data, plot):

        temp = data.copy()

        # Change the Data to Plot

        if plot['filter'] is not None:
            temp = self.filter_data(temp, plot)

        if plot['round'] is not None and plot['round'] != '':
            temp[plot['x']] = temp[plot['x']].round(int(plot['round']))    

        if plot['stat'] is not None and plot['stat'] != '':
            temp = self.select_group_by(temp, plot, plot['x'], plot['y'], plot['c'])


        # Create Plot

        scat   = temp.copy()
        colors = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']

        if plot['c'] is not None and plot['c'] != '':

            x, y, c = scat[plot['x']], scat[plot['y']], scat[plot['c']]

            try:
                inter, stringer = np.array_equal(c, c.astype(int)), False
            except:
                inter, stringer = False, True

            if (inter or stringer) and len(c.unique()) <= 20: 
            
                cmap    = LinearSegmentedColormap.from_list('my_list', colors[:len(c.unique())], N=len(c.unique()))      
                points  = plt.scatter(x, y, c=c, cmap=cmap)

                plt.colorbar(points, ticks=[c.unique()[i] for i in range(0, len(c.unique()))])     

            else:
                cmap    = LinearSegmentedColormap.from_list('my_list', colors[:10], N=10)      
                points  = plt.scatter(x, y, c=c, cmap=cmap)

                plt.colorbar(points, ticks=[i*(c.max()/10) for i in range(0, 11)])     


        else:
            x, y, c = scat[plot['x']], scat[plot['y']], None

            plt.scatter(x, y, c=c)


        # Adjusting Labels

        unique_y = scat[plot['y']].unique()
        unique_x = scat[plot['x']].unique()

        try:
            if np.array_equal(scat[plot['y']], scat[plot['y']].astype(int)) and len(unique_y) <= 30:            
                plt.yticks([i for i in unique_y], [i for i in unique_y])       
        except:
            pass  

        try:
            if np.array_equal(scat[plot['x']], scat[plot['x']].astype(int)) and len(unique_x) <= 30:            
                plt.xticks([i for i in unique_x], [i for i in unique_x])       
        except:
            pass    


    ### LINE
    #####################################################################################################################

    def line(self, data, plot):


        temp = data.copy()

        # Change the Data to Plot

        if plot['filter'] is not None:
            temp = self.filter_data(temp, plot)

        if plot['round'] is not None and plot['round'] != '':
            temp[plot['x']] = temp[plot['x']].round(int(plot['round']))    

        if plot['stat'] is not None and plot['stat'] != '':
            temp = self.select_group_by(temp, plot, plot['x'], plot['y'], plot['c'])


        # Create Plot
        
        if plot['c'] is not None and plot['c'] != '':
            for c in temp[plot['c']].unique():

                f    = temp[plot['c']] == c
                x, y = temp[f][plot['x']], temp[f][plot['y']]

                plt.plot(x, y, label=c)

        else:

            x, y = temp[plot['x']], temp[plot['y']]

            plt.plot(x, y)


        # Adjusting Labels

        unique_y = temp[plot['y']].unique()
        unique_x = temp[plot['x']].unique()

        try:
            if np.array_equal(temp[plot['y']], temp[plot['y']].astype(int)) and len(unique_y) <= 30:            
                plt.yticks([i for i in unique_y], [i for i in unique_y])       
        except:
            pass  

        try:
            if np.array_equal(temp[plot['x']], temp[plot['x']].astype(int)) and len(unique_x) <= 30:            
                plt.xticks([i for i in unique_x], [i for i in unique_x])       
        except:
            pass    


    ### VIOLIN
    #####################################################################################################################


    def violin(self, data, plot):

        temp = data.copy()

        # Change the Data to Plot

        if plot['filter'] is not None:
            temp = self.filter_data(temp, plot)

        if plot['round'] is not None and plot['round'] != '':
            temp[plot['x']] = temp[plot['x']].round(int(plot['round']))    

        if plot['stat'] is not None and plot['stat'] != '':
            temp = self.select_group_by(temp, plot, plot['x'], plot['y'], plot['c'])


        # Create Plot
        # Has Not_NaN Built-in

        x, y = temp[plot['x']], temp[plot['y']]

        var_list, labels = [], []
        for idx, x_unique in enumerate(sorted(x.unique())):

            est = temp[temp[plot['x']] == x_unique]

            var_list.append(est[~est[plot['y']].isna()][plot['y']].values)
            labels.append(x_unique)

        plt.violinplot(var_list, showmeans=True, showmedians=True)

        # Adjusting Labels

        plt.xticks([i for i in range(1, len(labels)+1)], labels, rotation=45) 



    ### HEATMAP
    #####################################################################################################################

    def heatmap(self, data, plot):

        temp = data.copy()

        # Change the Data to Plot

        if plot['filter'] is not None:
            temp = self.filter_data(temp, plot)

        if plot['round'] is not None and plot['round'] != '':
            temp[plot['x']] = temp[plot['x']].round(int(plot['round']))    

        if plot['stat'] is not None and plot['stat'] != '':
            temp = self.select_group_by(temp, plot, plot['x'], plot['c'], plot['y'])


        # Create Plot

        scat   = temp[[plot['x'], plot['y'], plot['c']]].copy()
        colors = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']

        scat[plot['x']] = scat[plot['x']].astype('str')
        scat[plot['y']] = scat[plot['y']].astype('str')
        

        x, y, c = scat[plot['x']], scat[plot['y']], scat[plot['c']]

        # x = [str(ix) + 'c' for ix in x]
        # y = [str(iy) + 'c' for iy in y]

        try:
            inter, stringer = np.array_equal(c, c.astype(int)), False
        except:
            inter, stringer = False, True


        if len(c.unique()) == 1:
            points  = plt.scatter(x, y, marker='s')


        elif (inter or stringer) and len(c.unique()) <= 20: 
        
            cmap    = LinearSegmentedColormap.from_list('my_list', colors[:len(c.unique())], N=len(c.unique()))      
            points  = plt.scatter(x, y, c=c, cmap=cmap, marker='s')

            plt.colorbar(points, ticks=[c.unique()[i] for i in range(0, len(c.unique()))])     

        else:
            cmap    = LinearSegmentedColormap.from_list('my_list', colors[:10], N=10)      
            points  = plt.scatter(x, y, c=c, cmap=cmap, marker='s')

            plt.colorbar(points, ticks=[i*(c.max()/10) for i in range(0, 11)])  

        # Adjusting Labels

        unique_y = scat[plot['y']].unique()
        plt.yticks([i for i in range(len(unique_y))], [i for i in unique_y]) 

        unique_x = scat[plot['x']].unique()
        plt.xticks([i for i in range(len(unique_x))], [i for i in unique_x], rotation=90)    


    ### BARPLOT
    #####################################################################################################################

    def barplot(self, data, plot):

        temp = data.copy()


        # Change the Data to Plot

        if plot['filter'] is not None:
            temp = self.filter_data(temp, plot)

        if plot['round'] is not None and plot['round'] != '':
            temp[plot['x']] = temp[plot['x']].round(int(plot['round']))    

        if plot['stat'] is not None and plot['stat'] != '':
            temp = self.select_group_by(temp, plot, plot['x'], plot['y'], None)

        # Create Plot


        scat   = temp[[plot['x'], plot['y']]].copy()
        colors = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']

        scat[plot['x']] = scat[plot['x']].astype('str')        

        x, y = scat[plot['x']], scat[plot['y']]


        plt.bar(x, y)

        # Adjusting Labels

        unique_x = scat[plot['x']].unique()
        if len(unique_x) > 10:
            plt.xticks([i for i in range(len(unique_x))], [i for i in unique_x], rotation=90)    
        else:
            plt.xticks([i for i in range(len(unique_x))], [i for i in unique_x])








class PDFGenerator():     
    def __init__(self, name, fig):
          
        self.name = name
        self.figs = fig
     
    def _transpose(self, lst):
        return list(map(list, zip(*lst)))
    
    def _head(self, color, font):
        self.pdf.add_page()
        self.pdf.image(resource_path('assets/header_expands.png'), x=0, y=0, w=508)
        self.pdf.set_font('Times', 'B', font)
        self.pdf.set_text_color(color)

    def _posis(self, length):
        if   length == 1: posis = [(50, 40, 400)]
        elif length == 2: posis = [(2, 70, 250), (255, 70, 250)]
        else:             posis = [(2, 70, 165), (167, 70, 165), (334, 70, 165)]
        
        return posis
    
    def _new_chapter(self, chapter):

        self._head(color=0, font=50)
        self.pdf.cell(0, 200, chapter, align='C')
    
    def fit(self):

        self.pdf = FPDF('L', 'mm', (285.75, 508))   

        self.pdf.add_page()
        self.pdf.set_font('Times', 'B', 40)
        self.pdf.image(resource_path('assets/header_expands.png'), x=0, y=0, w=508)
        self.pdf.cell(0, 110, 'REPORT:', align='C')
        self.pdf.ln(10)
        self.pdf.set_font('Times', 'B', 36)
        self.pdf.cell(0, 160, self.name, align='C') 

        

        for k in self.figs.keys():

            sub_figs = self.figs[k]

            self._new_chapter(k)

            for fig, _title in sub_figs:

                self._head(color=255, font=30)
                self.pdf.set_font('Times', 'B', 36)
                self.pdf.cell(0, 0, _title, align='L')

                for f, p in zip(fig, self._posis(len(fig))):

                    self.pdf.set_y(100)
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
                        f.savefig(tmpfile.name, bbox_inches="tight")
                        self.pdf.image(tmpfile.name, x=p[0], y=p[1], w=p[2])

        
        return self.pdf



if __name__ == '__main__':

    path = 'C:/Users/Scarlet/Desktop/rev2_Remaneja Sto Antonio e Jirau/vars.csv'
    data = pd.read_csv(path)

    path = 'C:/Users/Scarlet/Desktop/rev2_Remaneja Sto Antonio e Jirau/plot.json'



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
        


    PDF = PDFGenerator('name', data_plot)
    pdf = PDF.fit()
    pdf.output('Teste.pdf')  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap






def select_group_by(data, plot):

    if plot['stat'] == 'Mean':
        if plot['c'] is not None:
            return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].mean()
        else:
            return data.groupby([plot['x']], as_index=False)[plot['y']].mean()
        

    if plot['stat'] == 'Std':
        if plot['c'] is not None:
            return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].std()
        else:
            return data.groupby([plot['x']], as_index=False)[plot['y']].std()
        
    if plot['stat'] == 'Sum':
        if plot['c'] is not None:
            return data.groupby([plot['x'], plot['c']], as_index=False)[plot['y']].sum()
        else:
            return data.groupby([plot['x']], as_index=False)[plot['y']].sum()




def filter_data(data, plot):


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





def scatter(data, plot):

    scat   = data.copy()
    colors = ['royalblue', 'lightgreen', 'tan', 'thistle', 'red']
    

    if plot['c'] is not None:

        x, y, c = scat[plot['x']], scat[plot['y']], scat[plot['c']]

        if np.array_equal(c, c.astype(int)) and len(c.unique()) <= 20: 
        
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



def line(data, plot):

    if plot['c'] is not None:
        for c in data[plot['c']].unique():

            f    = data[plot['c']] == c
            x, y = data[f][plot['x']], data[f][plot['y']]

            plt.plot(x, y, label=c)

    else:

        x, y = data[plot['x']], data[plot['y']]

        plt.plot(x, y)





def plot_from_json(data, plot):  

    temp = data.copy()



    # Change the Data to Plot

    if plot['filter'] is not None:
        temp = filter_data(temp, plot)

    if plot['round'] is not None:
        print(plot['round'])
        temp[plot['x']] = temp[plot['x']].round(int(plot['round']))    

    if plot['stat'] is not None:
        temp = select_group_by(temp, plot)


    # Plot the data

    if plot['plot'] == 'Scatter':
        scatter(temp, plot)


    elif plot['plot'] == 'Line':
        line(temp, plot)   


    # Features

    plt.xlabel(plot['x_label'] if plot['x_label'] is not None else plot['x'])
    plt.ylabel(plot['y_label'] if plot['y_label'] is not None else plot['y'])

    
    unique_y = temp[plot['y']].unique()

    try:
        if np.array_equal(temp[plot['y']], temp[plot['y']].astype(int)):            
            plt.yticks([i for i in unique_y], [i for i in unique_y])       
    except:
        plt.yticks([i for i in unique_y], [i for i in unique_y])

        



    plt.show()




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
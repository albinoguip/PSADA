from DataTool import *
from itertools import permutations
from WFS_Editor import *
import os

import pyautogui
import subprocess
import time

from tqdm import tqdm


PATH     = 'Data/AI/RawDataset/'
PATH_NTW = PATH + '9bus.ntw'

ND = NTW_Reader(PATH_NTW)
ND = NTW_Editor(PATH_NTW)
ND.networkInfo()

# PATAMARES DE CARGA DAS BARRAS #################################################################################################

unicos  = [i*10 for i in range(1, 9)]
valores = []

for i in range(3):
    for u in unicos:
        valores.append(u)

patamares = list(set(permutations(valores, 3)))
columns   = ['Load_' + str(i+1) for i in range(len(patamares[0]))]

patamar_carga = pd.DataFrame(patamares, columns=columns)
patamar_carga = patamar_carga.sort_values(by=columns)
patamar_carga['Carga_Total'] = patamar_carga[columns].sum(axis=1)
patamar_carga = patamar_carga[patamar_carga['Carga_Total'] <= 95].reset_index(drop=True)

# print(f'\n ================ {len(patamar_carga)} ================ \n')
# print(patamar_carga.head())

# PATAMARES DE GERAÇÃO DAS BARRAS ###############################################################################################

unicos  = [20, 30, 50]

patamares = list(set(permutations(unicos, 3)))
columns   = ['Gen_' + str(i+1) for i in range(len(patamares[0]))]

patamar_gerac = pd.DataFrame(patamares, columns=columns)
patamar_gerac = patamar_gerac.sort_values(by=columns).reset_index(drop=True)

# print(f'\n ================ {len(patamar_gerac)} ================ \n')
# print(patamar_gerac.head())

# PATAMARES DE VSPECPU ##########################################################################################################

unicos  = [0.98, 0.99, 1.00, 1.01, 1.02]
valores = []

for i in range(3):
    for u in unicos:
        valores.append(u)

patamares = list(set(permutations(valores, 3)))
columns   = ['Volt_' + str(i+1) for i in range(len(patamares[0]))]

patamar_tensao = pd.DataFrame(patamares, columns=columns)
patamar_tensao = patamar_tensao.sort_values(by=columns)

# print(f'\n ================ {len(patamar_tensao)} ================ \n')
# print(patamar_tensao.head())

# print(f'\n ====================================================== \n')


# CENARIOS ######################################################################################################################

dyn_path = 'Data/AI/RawDataset/9bus/'

if not os.path.exists(dyn_path):
    os.mkdir(dyn_path)

nomes = []
for i in tqdm(range(len(patamar_carga))):
# for i in range(1):

    # CARGA
    ex = patamar_carga.iloc[i].values[:len(columns)]
    v  = patamar_carga.iloc[i].values[len(columns)]

    kw, kvar = ND.load_data['PL_MW'].values, ND.load_data['QL_MVAR'].values
    FP       = np.cos(np.arctan(kvar/kw))

    ND.load_data['PL_MW']   = ND.total_PMAX_MW*(ex/100)
    ND.load_data['PL_MW']   = ND.load_data['PL_MW'].round(1)
    ND.load_data['QL_MVAR'] = np.tan(np.arccos(FP))*ND.load_data['PL_MW']
    ND.load_data['QL_MVAR'] = ND.load_data['QL_MVAR'].round(1)

    nameL = '9bus__L__' + str(ex[0]) + '_' + str(ex[1]) + '_' + str(ex[2])

    # GERAÇÃO
    for j in range(len(patamar_gerac)):
    # for j in range(1):

        ex1 = patamar_gerac.iloc[j].values[:len(columns)]
        ND.gen_data['PG_MW'] = (v*ex1*ND.total_PMAX_MW)/(100*100)
        ND.gen_data['PG_MW'] = ND.gen_data['PG_MW'].round(1)
        nameG = nameL + '__G__' + str(ex1[0]) + '_' + str(ex1[1]) + '_' + str(ex1[2])

        if all(ND.gen_data['PMAX_MW'] > ND.gen_data['PG_MW']):

            # TENSAO
            for k in range(len(patamar_tensao)):
            # for k in range(2):

                ex2 = patamar_tensao.iloc[k].values[:len(columns)]
                ND.bus_data.loc[0:2, 'MODV_PU'] = ex2

                nameV = nameG + '__V__' + str(ex2[0]).replace('.', '') + '_' + str(ex2[1]).replace('.', '') + '_' + str(ex2[2]).replace('.', '')

                # print(ND.bus_data)

                ND.save(save_path = dyn_path + nameV + '.ntw')
                nomes.append(nameV + '.ntw')

    # GERAÇÃO
    ND.gen_data['PG_MW'] = (v*ND.gen_data['PMAX_MW'])/100
    nameG = nameL + '__G__EQ'

    # TENSÃO
    for k in range(len(patamar_tensao)):
    # for k in range(2):

        ex2 = patamar_tensao.iloc[k].values[:len(columns)]
        ND.bus_data.loc['MODV_PU', [0, 1, 2]] = ex2
        nameV = nameG + '__V__' + str(ex2[0]).replace('.', '') + '_' + str(ex2[1]).replace('.', '') + '_' + str(ex2[2]).replace('.', '')

        ND.save(save_path = dyn_path + nameV + '.ntw')
        nomes.append(nameV + '.ntw')

# DINAMICOS #####################################################################################################################

unicos  = ['I', 'M']
valores = []

for i in range(3):
    for u in unicos:
        valores.append(u)

patamares = list(set(permutations(valores, 3)))

dinamicos = []
for i in patamares:
    # print(i)
    dinamicos.append(f'9bus_1_{i[0]}_2_{i[1]}_3_{i[2]}.dyn')

for dyn in dinamicos:

    dyn_path = PATH + dyn.split('.')[0] + '/'

    if not os.path.exists(dyn_path):
        os.mkdir(dyn_path)
            
#     # WORK

    for ntw in nomes:
        
        files = [ntw.replace('.ntw', '.ntw'),  dyn, '9bus.evt']    
        WorkData(save_path = dyn_path + ntw.replace('.ntw', '') + '.dsa', lista=files)

    # SCRIPT

    path_script = dyn_path + 'RST_automation.txt'

    with open(path_script, 'w') as f:
        for nome in nomes:
            f.write('Open "' + "C:/Users/Scarlet/Desktop/Power Systems/" + dyn_path + nome.split('.')[0] + '.dsa"')
            f.write('\n')
            f.write('DSA DOP')
            f.write('\n')
            f.write('SAVE "' + "C:/Users/Scarlet/Desktop/Power Systems/" + dyn_path + nome + '"')
            f.write('\n')


# AUTOMATION ####################################################################################################################

# for dyn in dinamicos:

#     for nome in nomes:

#         dyn_path = PATH + dyn.split('.')[0] + '/'

#         b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/Capture.PNG')
#         w = b.width  / 2 + b.left
#         h = b.height / 2 + b.top  + 50

#         pyautogui.click(w, h, duration=0.25)
#         time.sleep(1)

#         time.sleep(1)
#         pyautogui.write(['down'])
#         pyautogui.hotkey('ctrl', 'a')
#         pyautogui.hotkey('del')

#         pyautogui.write('Open "' + dyn_path + nome.split('.')[0] + '.dsa"')
#         pyautogui.hotkey('enter')
        
#         pyautogui.write('DSA DOP')
#         pyautogui.hotkey('enter')

#         pyautogui.write('SAVE "' + dyn_path + nome + '"')
#         pyautogui.hotkey('enter')

#         time.sleep(1)

#         b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/Capture.PNG')
#         w = b.width  / 2 + b.left
#         h = b.height / 2 + b.top

#         pyautogui.click(w, h, duration=0.25)

#         # break

#     break



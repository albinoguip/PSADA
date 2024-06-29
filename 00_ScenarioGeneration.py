from PowerSystemsAnalysis import *

import matplotlib.pyplot as plt

import shutil, os, glob

from tqdm import tqdm



# 01 ---------------------------------------------------------------------------------------------------------------------
'''
_, _ = DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
'''

# 02 ---------------------------------------------------------------------------------------------------------------------
'''
_, _ = DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=True, P_fixo=False)
'''

# 03 ---------------------------------------------------------------------------------------------------------------------


'''
BUS_ID = DG.RemoveGen() 
'''

# 04 ---------------------------------------------------------------------------------------------------------------------

'''
_, _ = DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=0.30, max_load=0.6, PF_fixo=False, P_fixo=False)
'''

# 06 ---------------------------------------------------------------------------------------------------------------------

'''
    BUS_ID = DG.RemoveGen() 
    _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
'''

# 07 ---------------------------------------------------------------------------------------------------------------------

'''
    DG.RemoveLT(b_min=1, b_max=15, connections=None)
'''

# 08 ---------------------------------------------------------------------------------------------------------------------

'''
    _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
    DG.RemoveLT(b_min=1, b_max=15, connections=None)
'''

# 09 ---------------------------------------------------------------------------------------------------------------------

'''
    BUS_ID = DG.RemoveGen() 
    DG.RemoveLT(b_min=1, b_max=15, connections=None)
'''


# 10 ---------------------------------------------------------------------------------------------------------------------

'''
    BUS_ID = DG.RemoveGen() 
    _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
    DG.RemoveLT(b_min=1, b_max=15, connections=None)
'''




# pl_mw, ql_mvar, pg_mw, qg_mvar = [], [], [], []

# for idx in tqdm(range(0, 10)):

#     path = f'D:/BATCH/BATCH_11/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE_9BUS/9bus.ntw', dyn_path='D:/Modeling/BASE_9BUS/9bus.dyn')

#     BUS_ID = DG.RemoveGen() 
#     _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE_9BUS/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
#     DG.RemoveLT(b_min=1, b_max=2, connections=None)

#     DG.net.networkInfo(show=False)    

#     # pl_mw.append(DG.net.total_PL_MW)   
#     # ql_mvar.append(DG.net.total_QL_MVAR)
#     # pg_mw.append(DG.net.total_PG_MW)  
#     # qg_mvar.append(DG.net.total_QG_MVAR)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# # fig, axs = plt.subplots(2, 2)


# # axs[0, 0].hist(pl_mw, bins=50)
# # axs[0, 0].set_title("PL MW")

# # axs[0, 1].hist(ql_mvar, bins=50)
# # axs[0, 1].set_title("QL MVAR")

# # axs[1, 0].hist(pg_mw, bins=50)
# # axs[1, 0].set_title("PG MW")

# # axs[1, 1].hist(qg_mvar, bins=50)
# # axs[1, 1].set_title("QG MVAR")


# # plt.show()



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_11/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE_9BUS/9bus.ntw', dyn_path='D:/Modeling/BASE_9BUS/9bus.dyn')

#     _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE_9BUS/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_12/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE_9BUS/9bus.ntw', dyn_path='D:/Modeling/BASE_9BUS/9bus.dyn')

#     _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE_9BUS/CARGA.csv', min_load=0.30, max_load=0.6, PF_fixo=False, P_fixo=False)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_13/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE_9BUS/9bus.ntw', dyn_path='D:/Modeling/BASE_9BUS/9bus.dyn')

#     BUS_ID = DG.RemoveGen() 
#     _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE_9BUS/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_14/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE_9BUS/9bus.ntw', dyn_path='D:/Modeling/BASE_9BUS/9bus.dyn')

#     _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE_9BUS/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
#     DG.RemoveLT(b_min=1, b_max=2, connections=None)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_15/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE_9BUS/9bus.ntw', dyn_path='D:/Modeling/BASE_9BUS/9bus.dyn')

#     BUS_ID = DG.RemoveGen() 
#     _, _   = DG.ChangeLoad(carga='D:/Modeling/BASE_9BUS/CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
#     DG.RemoveLT(b_min=1, b_max=2, connections=None)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_16/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/BASE_9BUS/9bus.ntw', dyn_path='D:/Modeling/BASE_9BUS/9bus.dyn')

#     BUS_ID = DG.RemoveGen() 
#     DG.RemoveLT(b_min=1, b_max=2, connections=None)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')













# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_17/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.ntw', dyn_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.dyn')

#     # BUS_ID = DG.RemoveGen() 
#     _, _   = DG.ChangeLoad(carga='D:/Modeling/NETWORKS/24_BUS/24_CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
#     # DG.RemoveLT(b_min=1, b_max=2, connections=None)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')





# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_18/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.ntw', dyn_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.dyn')

#     _, _   = DG.ChangeLoad(carga='D:/Modeling/NETWORKS/24_BUS/24_CARGA.csv', min_load=0.30, max_load=0.6, PF_fixo=False, P_fixo=False)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_19/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.ntw', dyn_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.dyn')

#     BUS_ID = DG.RemoveGen() 
#     _, _   = DG.ChangeLoad(carga='D:/Modeling/NETWORKS/24_BUS/24_CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_20/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.ntw', dyn_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.dyn')

#     _, _   = DG.ChangeLoad(carga='D:/Modeling/NETWORKS/24_BUS/24_CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
#     DG.RemoveLT(b_min=1, b_max=5, connections=None)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_21/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.ntw', dyn_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.dyn')

#     BUS_ID = DG.RemoveGen() 
#     _, _   = DG.ChangeLoad(carga='D:/Modeling/NETWORKS/24_BUS/24_CARGA.csv', min_load=0.30, max_load=0.98, PF_fixo=False, P_fixo=False)
#     DG.RemoveLT(b_min=1, b_max=5, connections=None)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



# for idx in tqdm(range(0, 100_000)):

#     path = f'D:/BATCH/BATCH_22/'

#     os.makedirs(path, exist_ok=True)

#     DG = ScenarioGenerator(net_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.ntw', dyn_path='D:/Modeling/NETWORKS/24_BUS/24_BUS.dyn')

#     BUS_ID = DG.RemoveGen() 
#     DG.RemoveLT(b_min=1, b_max=2, connections=None)

#     DG.Save(net_path=path+f'R{idx:06d}.ntw')



























# batchs = ['17', '18', '19', '20', '21', '22']

# for i in batchs:

#     print(f'\n\n--------------------------------- {i} ---------------------------------\n\n')

#     os.makedirs(f'D:/BATCH/BATCH_{i}/Conv/', exist_ok=True)
#     os.makedirs(f'D:/BATCH/BATCH_{i}/No_Conv/', exist_ok=True)

#     not_conv, files = [], [f for f in os.listdir(f'D:/BATCH/BATCH_{i}/') if 'ntw' in f]
#     with open (f"D:/BATCH/BATCH_{i}/ConvStatus.txt", "r") as myfile:

#         lines, nao_conv = myfile.readlines(), []

#         for line in tqdm(lines):

#             try:
#                 if 'ntw' in line:
#                     mod_line = line.strip().replace('Case ', '').replace('not converged', '').replace(' ', '')                    
#                     not_conv.append(mod_line)
#             except:
#                 pass

#     not_conv = set(not_conv)
#     files    = set(files)
#     conv     = files - not_conv

#     for f in tqdm(list(conv)):
#         os.rename(f'D:/BATCH/BATCH_{i}/{f}', f'D:/BATCH/BATCH_{i}/Conv/{f}')

#     for f in tqdm(list(not_conv)):
#         os.rename(f'D:/BATCH/BATCH_{i}/{f}', f'D:/BATCH/BATCH_{i}/No_Conv/{f}')

















# D:/BATCH/
# C:/Users/PC-67/Desktop/
# batchs = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']
batchs = ['17', '18', '19', '20', '21', '22']

for i in batchs:

    path_script = f'D:/BATCH/BATCH_{i}/NTW_automation.txt'

    with open(path_script, 'w') as f:        

        casos = [f.split('.')[0] for f in os.listdir(f'D:/BATCH/BATCH_{i}/Conv/') if ('.ntw' in f or '.NTW' in f)]

        os.makedirs(f"D:/BATCH/BATCH_{i}/Conv/NEWTON/", exist_ok=True)

        for caso in tqdm(casos):

            actual = caso.split('_')[0]

            f.write(f'OPEN "D:/Organon.prm"')
            f.write('\n')
            f.write(f'OPEN "D:/BATCH/BATCH_{i}/Conv/{actual}.ntw"')
            f.write('\n')
            f.write('NEWTON')
            f.write('\n')
            f.write(f'SAVE "D:/BATCH/BATCH_{i}/Conv/NEWTON/{actual}_NEWTON.ntw"')
            f.write('\n')



















# batchs = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']#, '11', '12', '13', '14', '15', '16']

# # # f'D:/BATCH/BATCH_{batch}/OPF/'

# for batch in batchs:

#     files = [f.split('.')[0] for f in os.listdir(f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/') if ('ntw' in f.lower())]


#     shutil.copyfile('D:/Modeling/MOD/bus68.dyn', f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/bus68.dyn')
#     shutil.copyfile('D:/Modeling/MOD/bus68.evt', f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/bus68.evt')
#     shutil.copyfile('D:/Organon.prm'           , f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/Organon.prm')

#     for caso in tqdm(files):

#         WorkData(save_path=f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/{caso}.dsa', lista=['Organon.prm', f'{caso}.ntw', f'bus68.dyn', 'bus68.evt'])


# batchs = ['15', '16']

# for batch in batchs:

#     files = [f.split('.')[0] for f in os.listdir(f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/') if ('ntw' in f.lower())]


#     shutil.copyfile('D:/Modeling/NETWORKS/09_BUS/9bus.dyn', f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/9bus.dyn')
#     shutil.copyfile('D:/Modeling/NETWORKS/09_BUS/9bus.evt', f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/9bus.evt')
#     shutil.copyfile('D:/Organon.prm'                      , f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/Organon.prm')

#     for caso in tqdm(files):

#         WorkData(save_path=f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/{caso}.dsa', lista=['Organon.prm', f'{caso}.ntw', f'9bus.dyn', '9bus.evt'])





















# batchs = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']#, '11', '12', '13', '14', '15', '16']

# for batch in batchs: 
#     os.makedirs(f'D:/BATCH/BATCH_{batch}/Conv/DSA/', exist_ok=True)

# for batch in batchs: 

#     path_script = f'D:/BATCH/BATCH_{batch}/RST_automation.txt'
#     with open(path_script, 'w') as f:

#         casos   = [f for f in os.listdir(f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/') if '.dsa' in f]
#         rodados = [f.replace('.rst', '.dsa') for f in os.listdir(f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/') if '.rst' in f] # .replace('_NEWTON.rst', '.dsa')
#         casos   = list(set(casos) - set(rodados))

#         try:
#             print(batch, len(casos), len(rodados), casos[0], rodados[0])
#         except:
#             print(batch, len(casos), len(rodados), casos[0], None)
        

#         for caso in tqdm(casos):

#             actual = caso.split('.')[0]

#             f.write(f'OPEN "D:/BATCH/BATCH_{batch}/Conv/NEWTON/Organon.prm"')
#             f.write('\n')
#             f.write(f'OPEN "D:/BATCH/BATCH_{batch}/Conv/NEWTON/{actual}.dsa"')
#             f.write('\n')
#             f.write('DSA DOP')
#             f.write('\n')
#             f.write(f'SAVE "D:/BATCH/BATCH_{batch}/Conv/DSA/{actual}.ntw"')
#             f.write('\n')








# batchs = ['11', '12', '13', '14', '15', '16']

# for batch in batchs: 
#     os.makedirs(f'D:/BATCH/BATCH_{batch}/Conv/DSA/', exist_ok=True)


# ALL_BATCHS = []

# for batch in batchs:
#     print(batch)
#     casos   = [f for f in os.listdir(f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/') if '.dsa' in f]
#     rodados = [f.replace('.rst', '.dsa') for f in os.listdir(f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/') if '.rst' in f] # .replace('_NEWTON.rst', '.dsa')
#     casos_f = list(set(casos) - set(rodados))

#     print(len(casos), len(rodados), len(casos_f))

#     ALL_BATCHS.append(casos_f)


# path_script = f'D:/BATCH/RST_automation.txt'
# with open(path_script, 'w') as f:    

#     for i in range(20_000):
#         for j in range(len(ALL_BATCHS)):       
           

#             actual = ALL_BATCHS[j][i].split('.')[0]

#             f.write(f'OPEN "D:/BATCH/BATCH_{batchs[j]}/Conv/NEWTON/Organon.prm"')
#             f.write('\n')
#             f.write(f'OPEN "D:/BATCH/BATCH_{batchs[j]}/Conv/NEWTON/{actual}.dsa"')
#             f.write('\n')
#             f.write('DSA DOP')
#             f.write('\n')
#             f.write(f'SAVE "D:/BATCH/BATCH_{batchs[j]}/Conv/DSA/{actual}.ntw"')
#             f.write('\n')
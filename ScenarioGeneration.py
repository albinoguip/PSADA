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












# batchs = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']

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













# D:/BATCH
# C:\Users\PC-67\Desktop\BATCH_16
# batchs = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']
batchs = ['15']

for i in batchs:

    path_script = f'D:/BATCH/BATCH_{i}/NTW_automation.txt'

    with open(path_script, 'w') as f:        

        casos = [f.split('.')[0] for f in os.listdir(f'D:/BATCH/BATCH_{i}/Conv/') if ('.ntw' in f or '.NTW' in f)]

        os.makedirs(f"D:/BATCH/BATCH_{i}/Conv/NEWTON/", exist_ok=True)

        for caso in tqdm(casos):

            actual = caso.split('_')[0]

            f.write(f'OPEN "C:/Users/PC-67/Desktop/Organon.prm"')
            f.write('\n')
            f.write(f'OPEN "C:/Users/PC-67/Desktop/BATCH_{i}/Conv/{actual}.ntw"')
            f.write('\n')
            f.write('NEWTON')
            f.write('\n')
            f.write(f'SAVE "C:/Users/PC-67/Desktop/BATCH_{i}/Conv/NEWTON/{actual}_NEWTON.ntw"')
            f.write('\n')














# batchs = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']

# # # f'D:/BATCH/BATCH_{batch}/OPF/'

# for batch in batchs:

#     files = [f.split('.')[0] for f in os.listdir(f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/') if 'ntw' in f]

#     shutil.copyfile('D:/Modeling/MOD/bus68.dyn', f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/bus68.dyn')
#     shutil.copyfile('D:/Modeling/MOD/bus68.evt', f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/bus68.evt')
#     shutil.copyfile('D:/Organon.prm'           , f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/Organon.prm')

#     for caso in tqdm(files):

#         WorkData(save_path=f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/{caso}.dsa', lista=['Organon.prm', f'{caso}.ntw', f'bus68.dyn', 'bus68.evt'])



















# path_script = 'D:/RST_automation.txt'
# with open(path_script, 'w') as f:

#     for i in [21]: 

#         print(i)

#         casos   = [f for f in os.listdir(f'D:/BATCH/BATCH_{i}/NEWTON/') if '.dsa' in f]
#         rodados = [f.replace('_NEWTON.rst', '.dsa') for f in os.listdir(f'D:/BATCH/BATCH_{i}/NEWTON/') if '.rst' in f]
#         casos   = list(set(casos) - set(rodados))

        

#         for caso in tqdm(casos):

#             actual = caso.split('.')[0]

#             f.write(f'OPEN "D:/BATCH/BATCH_{i}/NEWTON/Organon.prm"')
#             f.write('\n')
#             f.write(f'OPEN "D:/BATCH/BATCH_{i}/NEWTON/{actual}.dsa"')
#             f.write('\n')
#             f.write('DSA DOP')
#             f.write('\n')
#             f.write(f'SAVE "D:/BATCH/BATCH_{i}/NEWTON/{actual}D.ntw"')
#             f.write('\n')
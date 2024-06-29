from PowerSystemsAnalysis import *

import os, glob, shutil

from tqdm import tqdm
import pandas as pd

pd.set_option('mode.chained_assignment', None)


### ==================================================================================================================================== ###
''' MOVE RSTS'''
### ==================================================================================================================================== ###



# BASE_PATH = 'D:/RUN/'

# folders = os.listdir(BASE_PATH)

# for folder in tqdm(folders):

#     RSTS = [f'{BASE_PATH}{folder}/{f}' for f in os.listdir(f'{BASE_PATH}/{folder}/') if 'rst' in f]#[6000:]
#     DYNS = [rst.split('_')[0] + '.dyn' for rst in RSTS]
#     NTWS = [rst.replace('rst', 'ntw') for rst in RSTS]

#     for rst in RSTS:
#         shutil.copyfile(rst, 'D:/DEFINITIVE/' + rst.split('/')[-1])

#     for dyn in DYNS:
#         shutil.copyfile(dyn, 'D:/DEFINITIVE/' + dyn.split('/')[-1])

#     for ntw in NTWS:
#         shutil.copyfile(ntw, 'D:/DEFINITIVE/' + ntw.split('/')[-1])


 
### ==================================================================================================================================== ###
''' EXTRACT: RST's INFO'''
### ==================================================================================================================================== ###

batchs = ['07', '08', '09', '10']

for batch in batchs:    

    PATH   = f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/'
    AUX    = f'D:/BATCH/BATCH_{batch}/'
    MASTER = [PATH + f for f in os.listdir(PATH) if '.rst' in f.lower()]
    parts  = len(MASTER)//2000 + 1 if len(MASTER)%2000 > 0 else len(MASTER)//2000

    print(f'\n\n --------------------------------------------------------------------------------------------------------------- {batch} {parts} --------------------------------------------------------------------------------------------------------------- \n\n')

    for cont in range(0, parts):
        
        FILES = MASTER[2000*(cont):2000*(cont+1)]
        vars  = pd.DataFrame()

        print(len(FILES), FILES[-1])

        print(len(FILES))

        for RST in tqdm(FILES):

            RR = RST_Reader(RST)
            a, net_info = RR.generate_json()

            if a == 'NOT':
                continue

            rede = np.expand_dims(np.array(net_info).ravel(), axis=(0))
            columns = []
            for isl in net_info['ISLD']:
                for col in net_info.columns:
                    columns.append(col + '_I' + isl)
            net_info = pd.DataFrame(rede, columns=columns)

            name          = RST.split('/')[-1].split('.')[0]
            RP            = RST_Process(a, name=name)
            RP.df.columns = [col[0] if col[1] == '' else col[0] + '_' + col[1] for col in RP.df.columns]

            # print(RP.df)

            RP.df['Contigence'] = [int(a.split('_')[-1]) for a in RP.df['Contigence']]
            RP.df['OP']         = name
            RP.df['OPD']        = name + 'D'
            RP.df['A_CODE']     = RP.df['A_CODE'].astype('int')

            RP.df = RP.df.sort_values(by=['OP', 'Contigence']).reset_index(drop=True)
            
            net_info['OP'] = RP.df['OP'].values[0]

            RP.df = RP.df.merge(net_info, on='OP', how='left')
            vars  = pd.concat([vars, RP.df]).reset_index(drop=True)


        vars.to_csv(f'{AUX}vars_part_{cont}.csv', index=False)

    PATHS = [AUX + f for f in os.listdir(AUX) if 'vars_part_' in f.lower()]

    data = pd.concat([pd.read_csv(f) for f in PATHS], axis=0)
    data.to_csv(f'{AUX}vars_BATCH_{batch}.csv', index=False)

    for path in PATHS:
        if os.path.exists(path):
            os.remove(path)



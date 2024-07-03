03_FeatureExtractorfrom PowerSystemsAnalysis import *
import pandas as pd



 
batchs = ['07', '08', '09', '10', '11', '12', '13', '14', '15', '16'] #'01', '02', '03', '04', '05', '06', 
batchs = ['06']

for batch in batchs:

    main_path = f'D:/BATCH/BATCH_{batch}/DSA/'
    out_path  = f'D:/BATCH/BATCH_{batch}/DATABASE/'
    cont_path = f'D:/BATCH/BATCH_{batch}/vars_BATCH_{batch}.csv'

    context = pd.read_csv(cont_path)

    os.makedirs(f'{out_path}NODE/', exist_ok=True)
    os.makedirs(f'{out_path}EDGE/', exist_ok=True)

    ops   = [f.split('.')[0] for f in os.listdir(main_path)]
    c_ops = context['OP'].unique()
    both  = list(set(ops) & set (c_ops))

    print(f'BATCH: {batch}')
    print(f'DSA: {len(ops)}')
    print(f'RST: {len(c_ops)}')
    print(f'BOTH: {len(both)}')


    for op in tqdm(both):


        # NODES
        # ///////////////////////////////////////////////////////////////


        NT = NTW_Reader(f'{main_path}{op}.ntw')
        NT.fit()
        NT.concat()
        fdata = NT.data[['BUS_ID', 'MODV_PU', 'ANGV_DEG', 'PL_MW', 'QL_MVAR', 'PG_MW', 'QG_MVAR', 'PMAX_MW']]

        # dyn = DynamicData('D:/BATCH/BATCH_1/' + dyn_name.split('_')[0] + '.dyn')
        # dyn.Params()
        # df_dyn = dyn.to_dataframe()       

        # fdata = fdata.merge(df_dyn, left_on='BUS_ID', right_on='Bus', how='left')



        fdata['MODV_PU']     = fdata['MODV_PU'].astype('float')
        fdata['ANGV_DEG']    = fdata['ANGV_DEG'].astype('float')
        fdata['PL_MW']       = fdata['PL_MW'].astype('float')
        fdata['QL_MVAR']     = fdata['QL_MVAR'].astype('float')
        fdata['PG_MW']       = fdata['PG_MW'].astype('float')
        fdata['QG_MVAR']     = fdata['QG_MVAR'].astype('float')
        fdata['PMAX_MW']     = fdata['PMAX_MW'].astype('float')
        # fdata['Base(MVA)']   = fdata['Base(MVA)'].astype('float')
        # fdata['H(MW/MVA.s)'] = fdata['H(MW/MVA.s)'].astype('float')

        fdata['P'] = fdata['PL_MW']*-1
        fdata['Q'] = fdata['QL_MVAR']*-1

        fdata.loc[fdata['P'].isna(), 'P'] = fdata[fdata['P'].isna()]['PG_MW']
        fdata.loc[fdata['Q'].isna(), 'Q'] = fdata[fdata['Q'].isna()]['QG_MVAR']


        # fdata = fdata[['BUS_ID', 'MODV_PU', 'ANGV_DEG', 'PL_MW', 'QL_MVAR', 'PG_MW', 'QG_MVAR', 'PMAX_MW', 'Base(MVA)', 'H(MW/MVA.s)', 'P', 'Q']]
        fdata = fdata[['BUS_ID', 'MODV_PU', 'ANGV_DEG', 'PL_MW', 'QL_MVAR', 'PG_MW', 'QG_MVAR', 'P', 'Q']]
        fdata = fdata.fillna(0)

        fdata.to_csv(f'{out_path}NODE/{op}.csv', index=False)


        # EDGES
        # ///////////////////////////////////////////////////////////////
        

        NT.concat_trans()

        fdata = NT.data_trans[['BFR_ID', 'BTO_ID']]#, 'RL_PU', 'XL_PU']]

        # fdata['RL_PU'] = fdata['RL_PU'].astype('float')
        # fdata['XL_PU'] = fdata['XL_PU'].astype('float')
        # fdata['RL_PU'] = fdata['RL_PU'].fillna(fdata['RL_PU'].mean().round(4))
        # fdata['XL_PU'] = fdata['XL_PU'].fillna(fdata['XL_PU'].mean().round(4))
        

        # fdata['X'] = (fdata['RL_PU']**2 + fdata['XL_PU']**2)**(0.5)
        # fdata['S'] = fdata['X']**(-1)/100

        fdata.to_csv(f'{out_path}EDGE/{op}.csv', index=False)






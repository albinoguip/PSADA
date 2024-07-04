import pandas as pd
import os
from tqdm import tqdm

class NTW_Reader():
    
    def __init__(self, path, first_line=None):
        
        self.path  = path
        self.begin = 4 if first_line is None else first_line

        with open(path) as f:
            self.lines = f.readlines()


    def fit(self):

        self._find_limits_in_file()
        self._get_bus_data()
        self._get_gen_data()
        self._get_load_data()
        self._get_transformer_data()
        self._get_transmission_data()

    
    def save_helper(self, table):

        if table == 'bus':
            return self.f_bus, self.l_bus
        
        if table == 'load':
            return self.f_load, self.l_load
        
        if table == 'gen':
            return self.f_gen, self.l_gen
        
        if table == 'transformer':
            return self.f_trs, self.l_trs
        
        if table == 'transmission':
            return self.f_tra, self.l_tra
        
        if table == '':
            return None

    def save(self, save_path):


        list_of_tables = [
                          (self.bus_data         , 'bus'),
                          (self.load_data        , 'load'),
                          (self.gen_data         , 'gen'),
                        #   (self.transformer_data , 'transformer'),
                          (self.transmission_data, 'transmission')
                          ]
        
        for table, name in list_of_tables:

            self._find_limits_in_file()  

            f, l = self.save_helper(name)

            # self.lines[f-1] = ', '.join(table.columns) + '\n'

            for index in range(l-f+1):
                self.lines.pop(f)

            for index in range(len(table)):
                new_line = ', '.join([str(v) for v in table.iloc[index]]) + '/\n'
                self.lines.insert(f+index, new_line)

            self._find_limits_in_file()  
           

        with open(save_path, 'w') as f:
            for line in self.lines:
                f.write(line)


    def _find_limits_in_file(self):


        for idx, line in enumerate(self.lines):

            # BUS

            self.f_bus = self.begin
            if 'END OF BUS DATA'  in line: self.l_bus  = idx - 1

            if 'BEGIN LOAD DATA'  in line: self.f_load = idx + 2
            if 'END OF LOAD DATA' in line: self.l_load = idx - 1

            if 'BEGIN GENERATOR DATA'  in line: self.f_gen = idx + 2
            if 'END OF GENERATOR DATA' in line: self.l_gen = idx - 1

            if 'BEGIN SHUNT DATA' in line: self.f_shu = idx + 2
            if 'END OF SWITCHED SHUNT DATA' in line: self.l_shu = idx - 1

            # CONNECTIONS

            if 'BEGIN TRANSMISSION LINE DATA'  in line: self.f_tra = idx + 2
            if 'END OF TRANSMISSION LINE DATA' in line: self.l_tra = idx - 1

            if 'BEGIN TRANSFORMER DATA'  in line: self.f_trs = idx + 2
            if 'END OF TRANSFORMER DATA' in line: self.l_trs = idx - 1

            if 'BEGIN SERIES CAPACITOR DATA' in line: self.f_sca = idx + 2
            if 'END OF SERIES CAPACITOR DATA' in line: self.l_sca = idx - 1

            if 'BEGIN DCLINK DATA' in line: self.f_dcl = idx + 2
            if 'END OF DCLINK DATA' in line: self.l_dcl = idx - 1


    # BUS =====================================================================================================================================================

    def _get_bus_data(self):      

        columns = self.lines[self.f_bus-1].strip().replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split() #
        data = []

        for i in range(self.f_bus, self.l_bus + 1):
            bus_info = self.lines[i].strip().replace('/', ' ').replace(' ', '').split(',') #.replace(',', ' ') .replace('\'', ' ')
            data.append(bus_info)

        try:
            self.bus_data = pd.DataFrame(data, columns=columns)
            
            for col in self.bus_data.columns:
                try:
                    self.bus_data[col] = self.bus_data[col].astype('int')

                except:
                    pass

        except:
            self.bus_data = pd.DataFrame(data)
            print('BUS: Check the data or the columns')



    # Get the LOAD's DATA =====================================================================================================================================

    def _get_load_data(self):      

        columns = self.lines[self.f_load-1].strip().replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        data = []

        for i in range(self.f_load, self.l_load + 1):
            load_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(' ', '').split(',')
            data.append(load_info)

        try:
            self.load_data = pd.DataFrame(data, columns=columns)
            
            for col in self.load_data.columns:
                try:
                    self.load_data[col] = self.load_data[col].astype('int')

                except:
                    pass

        except:
            self.load_data = pd.DataFrame(data)
            print('LOAD: Check the data or the columns')
 
    # Get the GENERATION's DATA ===============================================================================================================================

    def _get_gen_data(self):      

        columns = self.lines[self.f_gen-1].strip().replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        data = []

        for i in range(self.f_gen, self.l_gen + 1):
            gen_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(' ', '').split(',')
            data.append(gen_info)

        try:
            self.gen_data = pd.DataFrame(data, columns=columns)

            for col in self.gen_data.columns:
                try:
                    self.gen_data[col] = self.gen_data[col].astype('int')

                except:
                    pass

        except:
            try:
                self.gen_data = pd.DataFrame(data, columns=columns[:-1])

            except:
                try:
                    self.gen_data = pd.DataFrame(data, columns=columns[:-2])

                except:
                    self.gen_data = pd.DataFrame(data)
                    print('GEN: Check the data or the columns')

    # Get the GENERATION's DATA ===============================================================================================================================

    def _get_shunt_data(self):      

        columns = self.lines[self.f_shu-1].strip().replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        data = []

        for i in range(self.f_shu, self.l_shu + 1):
            gen_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(' ', '').split(',')
            data.append(gen_info)

        try:
            self.shu_data = pd.DataFrame(data, columns=columns)
        except:
            try:

                hard_col = ['BUS_ID', 'TC', 'VMAX_PU', 'VMIN_PU', 'BCO_ID', 'B0_MVAR', 'ST']
                outros   = ['ST', 'N', 'B_Mvar', 'XZ_PU']
                
                self.shu_data = pd.DataFrame(data)

                a = int((len(self.shu_data.columns) - len(hard_col))/4)

                for idx_sh in range(1, a+1):
                    for var in outros:
                        hard_col.append(var+str(idx_sh))

                self.shu_data = pd.DataFrame(data, columns=hard_col)

                self.shu_data['BUS_ID'] = self.shu_data['BUS_ID'].astype('float')

            except:
                self.shu_data = pd.DataFrame(data)
                print('\nSHUNT: Check the data or the columns')

    # Get the TRANSMISSION's DATA ===============================================================================================================================

    def _get_transmission_data(self):      

        columns = self.lines[self.f_tra-1].strip().replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        data = []

        for i in range(self.f_tra, self.l_tra + 1):
            tra_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(' ', '').split(',')
            data.append(tra_info)

        try:
            self.transmission_data = pd.DataFrame(data, columns=columns)

        except:
            try:

                hard_col = ['BFR_ID', 'BTO_ID', 'CI', 'RL_PU', 'XL_PU', 'B_MVAR', 'L1_MVA', 'L2_MVA', 'L3_MVA',
                            'BFR_LB', 'BTO_LB', 'LEN_KM', 'ARE', 'OWN', 'ZE_R', 'ZE_X', 'ZE_C', 'BR_NAME',
                            'BUS_CTR1', 'CTR1', 'BUS_CTR2', 'CTR2',
                            'BFR_SH1', 'GSHT_F1', 'BSHT_F1','BTO_SH1', 'GSHT_T1', 'BSHT_T1',
                            'BFR_SH2', 'GSHT_F2', 'BSHT_F2','BTO_SH2', 'GSHT_T2', 'BSHT_T2',
                            'BFR_SH3', 'GSHT_F3', 'BSHT_F3','BTO_SH3', 'GSHT_T3', 'BSHT_T3']
                self.transmission_data = pd.DataFrame(data, columns=hard_col)

            except:
                self.transmission_data = pd.DataFrame(data)
                print('TRANSMISSION: Check the data or the columns')
                print(columns)

    # Get the 's DATA ===============================================================================================================================

    def _get_transformer_data(self):      

        # columns = self.lines[self.s-1].strip().replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        data_raw, data = [], []

        head = [self.lines[i].strip() for i in range(self.f_trs-1, self.l_trs + 1) if '/' in self.lines[i].strip()]


        for line in head:
            trs_info = line.strip().replace('/', ' ').replace('\'', ' ').replace(' ', '').split(',')
            data.append(trs_info)

            # print(trs_info)

        # for i in range(len(data_raw)//4):
        #     prov = data_raw[i*4]

        #     # for d in data_raw[i*2+1]:
        #     #     prov.append(d)

        #     data.append(prov)

        try:
            try:
                hard_col = ['BUS1', 'BUS2', 'BUS3', 'CI', 'G_MAG', 'B_MAG', 'WI1', 'WI2', 'WI3', 'WI_V', 'WI_A', 'ARE', 'OWN', 'NAME', 'BUS4',  'NAME2']
                self.transformer_data = pd.DataFrame(data, columns=hard_col)
            except:
                hard_col = ['BUS1', 'BUS2', 'BUS3', 'CI', 'G_MAG', 'B_MAG', 'WI1', 'WI2', 'WI3', 'WI_V', 'WI_A', 'ARE', 'OWN', 'NAME']
                self.transformer_data = pd.DataFrame(data, columns=hard_col)

        except:
            self.transformer_data = pd.DataFrame(data)
            print('TRANSFORMER: Check the data or the columns')
            print(hard_col)

    # Get the GENERATION's DATA ===============================================================================================================================

    def _get_series_capacitor_data(self):

        columns = self.lines[self.f_sca-1].strip().replace('!', ' ').replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        data = []

        for i in range(self.f_sca, self.l_sca + 1):
            sca_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(' ', '').split(',')
            data.append(sca_info)

            # print(sca_info)

        try:
            self.series_capacitor_data = pd.DataFrame(data, columns=columns)

        except:
            try:

                hard_col = ['BFROM_ID', 'BTO_ID', 'CRC', 'R_PU', 'X_PU', 'RATEA_MVA', 'RATEB_MVA', 'RATEC_MVA', 'SHTF_ST',
                            'GSHTF', 'BSHTF', 'SHTT_ST', 'GSHTT', 'BSHTT', 'BRKERF_ST', 'BRKERT_ST', 'OWNER', 'NAME']
                self.series_capacitor_data = pd.DataFrame(data, columns=hard_col)

            except:
                self.series_capacitor_data = pd.DataFrame(data)
                print('SERIES CAPACITOR: Check the data or the columns')
                print(columns)


    # Get the GENERATION's DATA ===============================================================================================================================

    def _get_dclink_data(self):

        columns  = self.lines[self.f_dcl-1].strip().replace('!', ' ').replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        columnsr = self.lines[self.f_dcl].strip().replace('!', ' ').replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()
        columnsi = self.lines[self.f_dcl+1].strip().replace('!', ' ').replace('/', ' ').replace('(', ' ').replace(')', ' ').replace('\'', ' ').replace(',', ' ').split()

        data, datar, datai = [], [], []

        cont = 0

        for i in range(self.f_dcl+2, self.l_dcl + 1):
            dcl_info = self.lines[i].strip().replace('/', ' ').replace('\'', ' ').replace(' ', '').split(',')

            if cont == 0:
                data.append(dcl_info)
            elif cont == 1:
                datar.append(dcl_info)
            elif cont == 2:
                datai.append(dcl_info)
            else:
                print('ERROR')

            cont = cont + 1 if cont != 2 else 0

            # data.append(dcl_info)

            # print(dcl_info)

        try:
            self.dc_link_cab_data = pd.DataFrame(data, columns=columns)
            self.ret_data = pd.DataFrame(datar, columns=['R_' + col for col in columnsr])
            self.inv_data = pd.DataFrame(datai, columns=['I_' + col for col in columnsi])

            self.dc_link_data = pd.concat([self.dc_link_cab_data, self.ret_data, self.inv_data], axis=1)

        except:
            print('teste')
        #     try:

        #         hard_col = ['BFROM_ID', 'BTO_ID', 'CRC', 'R_PU', 'X_PU', 'RATEA_MVA', 'RATEB_MVA', 'RATEC_MVA', 'SHTF_ST',
        #                     'GSHTF', 'BSHTF', 'SHTT_ST', 'GSHTT', 'BSHTT', 'BRKERF_ST', 'BRKERT_ST', 'OWNER', 'NAME']
        #         self.series_capacitor_data = pd.DataFrame(data, columns=hard_col)

        #     except:
        #         self.series_capacitor_data = pd.DataFrame(data)
        #         print('SERIES CAPACITOR: Check the data or the columns')
        #         print(columns)




    # Get the GENERATION's DATA ===============================================================================================================================

    def concat(self):

        self.load_data = self.load_data.rename(columns={'ID':'LOAD_ID', 'ST':'LOAD_ST'})
        self.gen_data  = self.gen_data.rename(columns={'ID':'GEN_ID', 'ST':'GEN_ST'})
        # self.shu_data  = self.shu_data.rename(columns={'BCO_ID':'SHU_ID', 'ST':'SHU_ST'})

        self.gen_data['BUS_ID'] = self.gen_data['BUS_ID'].astype('int')

        self.data = self.bus_data.merge(self.load_data, on='BUS_ID', how='outer')
        self.data = self.data.merge(self.gen_data, on=['BUS_ID'], how='left')
        # self.data = self.data.merge(self.shu_data, on=['BUS_ID'], how='left')

    # Get the GENERATION's DATA ===============================================================================================================================

    def concat_trans(self):

        # self.transformer_data['BTO_ID'] = self.transformer_data['BUS2']

        # print(self.transformer_data)


        a = self.transformer_data.copy()
        b = self.transformer_data.copy()
        # c = self.transformer_data.copy()

        a.loc[:, 'BTO_ID'] = a['BUS2']
        b.loc[:, 'BTO_ID'] = b['BUS3']
        # c.loc[:, 'BTO_ID'] = c['BUS4'] Q

        # a = a.rename(columns={'BUS2':'BTO_ID'})
        # b = b.rename(columns={'BUS3':'BTO_ID'})
        # c = c.rename(columns={'BUS4':'BTO_ID'})


        # self.transformer_data = pd.concat([a, b], axis=0).dropna(subset='BTO_ID').reset_index(drop=True)
        # self.transformer_data = pd.concat([a, b, c], axis=0).dropna(subset='BTO_ID').reset_index(drop=True)

        # print(self.transformer_data)


        # if 'BUS4' in self.transformer_data.columns:
        #     self.transformer_data.loc[~self.transformer_data['BUS4'].isna(), 'BTO_ID']  =self.transformer_data[~self.transformer_data['BUS4'].isna()]['BUS4']

        # self.transformer_data['TIPO']      = 'TF'
        # self.transmission_data['TIPO']     = 'TM'
        # self.series_capacitor_data['TIPO'] = 'SC'
        # self.dc_link_data['TIPO']          = 'DC'

        self.data_trans = self.transformer_data.rename(columns={'BUS1':'BFR_ID', 'BUS2':'BTO_ID'})
        self.data_trans = self.data_trans.merge(self.transmission_data                                                             , on=['BFR_ID', 'BTO_ID'], how='outer')
        # self.data_trans = self.data_trans.merge(self.series_capacitor_data.rename(columns={'BFROM_ID':'BFR_ID', 'BTO_ID':'BTO_ID'}), on=['BFR_ID', 'BTO_ID'], how='outer')
        # self.data_trans = self.data_trans.merge(self.dc_link_data.rename(columns={'R_RET_ID':'BFR_ID', 'I_INV_ID':'BTO_ID'})       , on=['BFR_ID', 'BTO_ID'], how='outer')

        # self.data_trans.loc[~self.data_trans['BSHT_T2'].isna(),   'TIPO'] = 'TF'
        # self.data_trans.loc[~self.data_trans['G_MAG'].isna(),     'TIPO'] = 'TM'
        # self.data_trans.loc[~self.data_trans['RATEA_MVA'].isna(), 'TIPO'] = 'SC'
        # self.data_trans.loc[~self.data_trans['R_BASE_KV'].isna(), 'TIPO'] = 'DC'

        self.data_trans = self.data_trans.astype({'BFR_ID': 'int32', 'BTO_ID': 'int32'})

    # Get the INFORMATION  ===============================================================================================================================

    def networkInfo(self, show=False):

        self.total_PL_MW   = self.load_data['PL_MW'].astype('float').sum()   
        self.total_QL_MVAR = self.load_data['QL_MVAR'].astype('float').sum() 
        # print(self.total_PL_MW, self.total_QL_MVAR)

        self.total_PG_MW   = self.gen_data['PG_MW'].astype('float').sum()    
        self.total_QG_MVAR = self.gen_data['QG_MVAR'].astype('float').sum() 
        # print(self.total_PG_MW, self.total_QG_MVAR)

        self.total_PMAX_MW = self.gen_data['PMAX_MW'].astype('float').sum()  
        self.total_PMIN_MW = self.gen_data['PMIN_MW'].astype('float').sum()
        # print(self.total_PMAX_MW, self.total_PMIN_MW)

        # self.reserva_total   = self.total_PMAX_MW - self.total_PG_MW
        self.reserva_per_gen = self.gen_data['PMAX_MW'].astype('float') - self.gen_data['PG_MW'].astype('float')

        try:
            self.total_PG_RENEW = self.gen_data[self.gen_data['TYPE'] == 4]['PG_MW'].astype('float').sum() 
            self.total_PG_SYNC  = self.gen_data[(self.gen_data['BLOCKED'] == 0)]['PG_MW'].astype('float').sum() 
            self.penetration    = self.total_PG_RENEW / self.total_PG_MW
        except:
            pass
        # print(self.total_PG_RENEW, self.total_PG_SYNC)

        try:
            self.total_PMAX_MW_unblock  = self.gen_data[self.gen_data['BLOCKED'] == 0]['PMAX_MW'].astype('float').sum() 
            self.total_PMAX_MW_block    = self.gen_data[self.gen_data['BLOCKED'] == 1]['PMAX_MW'].astype('float').sum() 

            self.total_PG_MW_unblock    = self.gen_data[self.gen_data['BLOCKED'] == 0]['PG_MW'].astype('float').sum() 
            self.total_PG_MW_block      = self.gen_data[self.gen_data['BLOCKED'] == 1]['PG_MW'].astype('float').sum() 
        
            self.total_headroom_unblock = self.total_PMAX_MW_unblock - self.total_PG_MW_unblock

        except:
            pass
        
        
        self.total_headroom = self.total_PMAX_MW - self.total_PG_MW
        
        
        
        if show:
            
            print(' ====================== Network Info ====================== ')
            print(' ======================== GENERATOR ======================= \n')
            print(f' Total Active Power:   {self.total_PG_MW:.4f} MW')
            print(f' Total Reactive Power: {self.total_QG_MVAR:10.4f} MVar\n')
            
            print(f' Total Max Active Power: {self.total_PMAX_MW:.4f} MW')
            print(f' Total Min Active Power: {self.total_PMIN_MW:10.4f} MW\n')
            
            print(f' Total Renew Active Power: {self.total_PG_RENEW:10.4f} MW')
            print(f' Total Sync Active Power:  {self.total_PG_SYNC:.4f} MW\n')
            
            print(f' Total Headroom:             {self.total_headroom:10.4f} MW')
            print(f' Total Max Unblocked Power:  {self.total_PMAX_MW_unblock:.4f} MW')
            print(f' Total Head Unblocked Power: {self.total_headroom_unblock:10.4f} MW\n')
            
            print(f' Renewable Penetration: {self.penetration*100:.4f} %\n')

            print(f' Total Max Unblocked Power:  {self.total_PMAX_MW_unblock:.4f} MW')
            print(f' Total Max Blocked Power:    {self.total_PMAX_MW_block:10.4f} MW\n')

            print(f' Total Unblocked Power:  {self.total_PG_MW_unblock:10.4f} MW')
            print(f' Total Blocked Power:    {self.total_PG_MW_block:10.4f} MW')
            
            print(' ========================== LOAD ========================== \n')
            print(f' Total Active Power:   {self.total_PL_MW:10.4f} MW')
            print(f' Total Reactive Power: {self.total_QL_MVAR:10.4f} MVar\n\n')

    def graph_get_nodes(self, data):

        tra = data[['BFR_ID', 'BTO_ID']]
        tra = tra.drop_duplicates()
        tra = tra[tra['BTO_ID'] != 0]

        tra = tra.astype({'BFR_ID': 'int32', 'BTO_ID': 'int32'})


        fr, to = [], []

        for i in range(len(tra)):
            fr.append(tra.iloc[i]['BFR_ID']-1)
            to.append(tra.iloc[i]['BTO_ID']-1)

        a = sorted(range(len(fr)), key=lambda k: fr[k])

        return [(fr[i]+1, to[i]+1) for i in a]


if __name__ == '__main__':

    import numpy as np

    NR = NTW_Reader('D:/PowerSystems/Sistemas/SIN/MEDIA/NET/D_1_H_00-00.ntw')

    NR._find_limits_in_file()

    print(NR.f_bus , NR.l_bus)
    print(NR.f_gen , NR.l_gen)
    print(NR.f_load, NR.l_load)
    print(NR.f_tra , NR.l_tra)







    # # NR = NTW_Reader('Data/AI/bus68/BASE/bus68.ntw')
    # NR.concat_trans()

    # # print(NR.data_trans[['BFR_ID', 'BTO_ID']])
    # print(NR.dc_link_data.columns.values)
    # print(NR.transmission_data[['BFR_ID', 'B_MVAR', 'ZE_R' ,'ZE_X', 'ZE_C', 'BR_NAME', 'BUS_CTR1', 'CTR1', 'BUS_CTR2', 'CTR2' ,'BFR_SH1']])
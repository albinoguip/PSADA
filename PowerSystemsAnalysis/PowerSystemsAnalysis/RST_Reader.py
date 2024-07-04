import pandas as pd
import json, os
import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# class RST_Reader():

#     def __init__(self, path):

#         days = os.listdir(path)

#         reports = []
#         for day in days:
#             hours = os.listdir(path + '/' + day)

#             for hour in hours:
#                 reports.append(path + '/' + day + '/' + hour)

#         self.reports = reports
#         self.path    = path

#     def generate_json(self, save_path=None, cont_path=None, debug=True):

#         all_reports = {}
#         for report_file in tqdm(self.reports):

#             with open(report_file) as f:
#                 raw_lines = f.readlines()

#             lines = [line.strip().split() for line in raw_lines]

#             contigences, reports, cont = [], [], True
#             for line in lines[3:]:

#                 try:
#                     int(line[0])
#                     if cont: contigences.append(line)
#                     else: reports.append(line)

#                 except ValueError:
#                     cont = False
#                     pass

#             # code_names = set([report[1] for report in reports])

#             if debug:
#                 print(report_file)

#             dict_report, actual_contigence, cont = {}, '0', 0
#             for report in reports:
                
#                 for idx, var in enumerate(report[2:]):
#                     report[idx+2] = float(var)


#                 if report[0] != actual_contigence:
#                     cont = 0
#                     actual_contigence = report[0]
#                     dict_report['Contigence_' + actual_contigence] = {'Line_' + str(cont) : report}

#                 else:
#                     cont += 1
#                     dict_report['Contigence_' + actual_contigence]['Line_' + str(cont)] = report

#             all_reports[report_file.split('.')[0].replace('Month/DS202210', '').replace('/20230406_C_', '/')] = dict_report

#         return all_reports
        # with open(save_path, "w") as write_file:
        #     json.dump(all_reports, write_file, indent=4)

        # with open(cont_path, "w") as write_file:
        #     json.dump(contigences, write_file, indent=4)




class RST_Process():
    def __init__(self, repots_path, contigences_path):

        with open(repots_path, 'r') as f:
            data = json.load(f)

        with open(contigences_path, 'r') as f:
            contigences = json.load(f)


        stab_points = []
        for operation_point in tqdm(data.keys()):
            for contigence in data[operation_point].keys():
                for params in data[operation_point][contigence]:

                    actual_param, param = [operation_point, contigence], data[operation_point][contigence][params]
                    for i in param: actual_param.append(i)

                    stab_points.append(actual_param)

        cont_number = ['Contigence_' + contigence[0] for contigence in contigences]
        cont_name   = [' '.join(contigence[1:]) for contigence in contigences]

        df = pd.DataFrame(stab_points, columns=['Operational Point', 'Contigence', 'Contigence_Number', 'SIGLA', 'A', 'B', 'C', 'D', 'E'])
        df = df.replace(cont_number, cont_name)

        df['Contigence'] = df.astype({'Contigence_Number':'str'})['Contigence_Number'] + '_' + df['Contigence']
        df['key'] = df['Operational Point'] + df['Contigence']

        self.data = df


class RST_Reader():

    def __init__(self, path):

        self.path = path

    def generate_json(self):

        with open(self.path) as f:
            raw_lines = f.readlines()

        lines = [line.replace(':', '').replace(';', '').strip().split() for line in raw_lines]

        contigences, reports, cont, net_info = [], [], True, []
        for line in lines[3:]:

            try:
                int(line[0])
                if cont: contigences.append(line)
                else: reports.append(line)

            except ValueError:
                if len(line) > 5:
                    net_info.append(line)
                cont = False
                pass


        dict_report, actual_contigence, cont = {}, '0', 0
        for report in reports:
            
            for idx, var in enumerate(report[2:]):

                try:
                    report[idx+2] = float(var)

                except:
                    print(self.path)


            if report[0] != actual_contigence:
                cont = 0
                actual_contigence = report[0]
                dict_report['Contigence_' + actual_contigence] = {'Line_' + str(cont) : report}

            else:
                cont += 1
                dict_report['Contigence_' + actual_contigence]['Line_' + str(cont)] = report

        vars, valores = [], []
        for island in net_info:

            var, valor = [], []
            for idx, val in enumerate(island):
                if idx%2 == 0:
                    var.append(val)
                else:
                    valor.append(val)

            vars.append(var)
            valores.append(valor)

        try:
            net_info = pd.DataFrame(valores, columns=vars[0])
        except:
            print(self.path)
            
        net_info = net_info.loc[:, ~net_info.columns.duplicated()].copy()

        reserva  = net_info.iloc[int(len(net_info)/2):][['ISLD', 'SLCK', 'TBUS']].rename(columns={'SLCK':'TRSV', 'TBUS':'HRSV'})
        net_info = net_info.iloc[:int(len(net_info)/2)].merge(reserva, on='ISLD', how='left')
    
        return dict_report, net_info
    

class RST_Process():
    def __init__(self, reports, name):

        stab_points = []
        for contigence in reports.keys():
            for params in reports[contigence]:

                actual_param, param = [contigence], reports[contigence][params]
                for i in param: actual_param.append(i)

                stab_points.append(actual_param)

        try:
            df = pd.DataFrame(stab_points, columns=['Contigence', 'Contigence_Number', 'SIGLA', 'A', 'B', 'C', 'D', 'E'])

            df['OP'] = name
        
            df = df[['OP', 'Contigence', 'SIGLA', 'A', 'B']]
            df = df[df['SIGLA'].isin(['CODE', 'STAB', 'DAMP', 'RCFC', 'NDRC', 'INRT', 'PGTM'])]
            df = df.pivot_table(['A', 'B'], ['OP', 'Contigence'], 'SIGLA').reset_index(drop=False)

        except:
            # print(name)
            df = pd.DataFrame(stab_points, columns=['Contigence', 'Contigence_Number', 'SIGLA', 'A'])

            df['OP'] = name
        
            df = df[['OP', 'Contigence', 'SIGLA', 'A']]
            df = df[df['SIGLA'].isin(['CODE', 'STAB', 'DAMP', 'RCFC', 'NDRC', 'INRT', 'PGTM'])]
            df = df.pivot_table(['A'], ['OP', 'Contigence'], 'SIGLA').reset_index(drop=False)
        
        self.df = df

if __name__ == '__main__':

    # path = 'C:/Users/Scarlet/Desktop/Data/PTOPER_A2V2F2_rev2/RenovaveisONS'
    # RR = RST_Reader(path)
    # RR.generate_json(save_path= path + "/PTOPER_A2V2F2_rev2.json",
    #                  cont_path= path + "/PTOPER_A2V2F2_rev2_cont.json")

    ### ================================================================================================== ###
    ### ============================================= MESTRADO =========================================== ###
    ### ================================================================================================== ###

    # PATH      = 'Data/AI/bus68/'
    # PATH_DEST = 'Data/AI/bus68/vars/'

    # folders = os.listdir(PATH)

    # folders = ['SIMU_L0']

    # columns = []
    # for idx in range(121):
    #     columns.append('C'+str(idx+1))

    # cont = np.eye(121)

    # cons = pd.DataFrame(cont, columns=columns)
    # cons['Contigence'] = ['Contigence_'+str(i) for i in range(1, 122)]

    # for folder in folders:

    #     rsts  = os.listdir(PATH + folder + '/')
    #     rsts = [rst for rst in rsts if '.rst' in rst]

    #     vars = pd.DataFrame()

    #     # rsts = ['PL_109_QL_6_V_3_PG_EQ_L0.rst']

    #     for rst in tqdm(rsts):

    #         RR = RST_Reader(PATH + folder + '/' + rst)
    #         a, net_info = RR.generate_json()

    #         RP = RST_Process(a, name=rst.split('.')[0])
    #         # RP.df['Inercia'] = folder
    #         # break

    #         # net_info['Value'] = net_info['Value'].astype('float')
    #         # net_info = pd.pivot_table(net_info, values='Value', columns='NetVar', aggfunc=np.mean).reset_index(drop=True)
    #         net_info['OP'] = RP.df['OP'].values[0]

    #         RP.df = RP.df.merge(net_info, on='OP', how='left')
    #         vars  = pd.concat([vars, RP.df]).reset_index(drop=True)
            
    #         break
    #     # break

    #     print(vars)
    #     print(cons)

    #     # 'Inercia'
    #     # vars = vars[['OP', 'Contigence',
    #     #              'RCFC', 'NDRC', 'DAMP',
    #     #              'DCEX', 'DCIM', 'EMXI', 'GBUS', 'GIMX', 'GINR', 'GIRS', 'GMAX', 'GRES', 'INDC',
    #     #              'INER', 'INLD', 'ISLD', 'LOAD', 'LOSS', 'SHNT', 'SLCK', 'TBUS', 'TGEN', 'TINR']]
        
    #     # vars = vars.sort_values(by=['OP', 'Contigence']).reset_index(drop=True)

    #     # print(vars)

    #     rede = pd.read_csv(PATH_DEST + folder + '_vars.csv')
    #     rede = rede.merge(cons, on='Contigence', how='left')
    #     rede = rede.drop(['Unnamed: 0'], axis=1)

    #     print(rede)

    #     rede.to_csv(PATH_DEST + folder + '_one_line_vars.csv', index=False)


    ### ================================================================================================== ###
    ### ============================================= PROJETO ============================================ ###
    ### ================================================================================================== ###

    PATH      = 'D:/PowerSystems/Sistemas/SIN/MEDIA/'
    PATH_DEST = 'D:/PowerSystems/Sistemas/SIN/OUT/'
    folders   = os.listdir(PATH)

    for folder in folders:

        rsts = os.listdir(PATH + folder + '/Output/' )
        rsts = [rst for rst in rsts if '.rst' in rst]
        vars = pd.DataFrame()

        for rst in tqdm(rsts):

            RR = RST_Reader(PATH + folder + '/Output/' + rst)
            a, net_info = RR.generate_json()

            rede = np.expand_dims(np.array(net_info).ravel(), axis=(0))
            columns = []
            for isl in net_info['ISLD']:
                for col in net_info.columns:
                    columns.append(col + '_I' + isl)
            net_info = pd.DataFrame(rede, columns=columns)

            RP            = RST_Process(a, name=rst.split('.')[0])
            RP.df.columns = [col[0] if col[1] == '' else col[0] + '_' + col[1] for col in RP.df.columns]

            RP.df['Dia']        = folder.replace('DS202210', '')
            RP.df['Contigence'] = [int(a.split('_')[-1]) for a in RP.df['Contigence']]
            RP.df['Hora']       = [a.split('_')[-1] for a in RP.df['OP']]
            RP.df['OP']         = 'D_' + RP.df['Dia'] + '_H_' + RP.df['Hora']
            RP.df['Dia']        = int(folder.replace('DS202210', ''))
            RP.df['A_CODE']     = RP.df['A_CODE'].astype('int')

            try:
                RP.df = RP.df[['OP', 'Dia', 'Hora', 'Contigence', 'A_STAB', 'A_CODE', 'A_RCFC', 'A_NDRC', 'A_DAMP', 'A_INRT',
                                                                  'B_STAB',                     'B_NDRC', 'B_DAMP', 'B_INRT']]
            except:
                try:
                    RP.df = RP.df[['OP', 'Dia', 'Hora', 'Contigence', 'A_STAB', 'B_STAB', 'A_CODE']]
                    RP.df.loc[:, 'A_RCFC'] = np.nan
                    RP.df.loc[:, 'A_NDRC'] = np.nan
                    RP.df.loc[:, 'A_DAMP'] = np.nan
                    RP.df.loc[:, 'A_INRT'] = np.nan

                    RP.df.loc[:, 'B_NDRC'] = np.nan
                    RP.df.loc[:, 'B_DAMP'] = np.nan
                    RP.df.loc[:, 'B_INRT'] = np.nan

                    print(RP.df['OP'].unique())
                except:
                    RP.df = RP.df[['OP', 'Dia', 'Hora', 'Contigence', 'A_CODE']]
                    RP.df.loc[:, 'A_STAB'] = np.nan
                    RP.df.loc[:, 'A_RCFC'] = np.nan
                    RP.df.loc[:, 'A_NDRC'] = np.nan
                    RP.df.loc[:, 'A_DAMP'] = np.nan
                    RP.df.loc[:, 'A_INRT'] = np.nan

                    RP.df.loc[:, 'B_STAB'] = np.nan
                    RP.df.loc[:, 'B_NDRC'] = np.nan
                    RP.df.loc[:, 'B_DAMP'] = np.nan
                    RP.df.loc[:, 'B_INRT'] = np.nan

                    print(RP.df['OP'].unique())

            RP.df = RP.df.sort_values(by=['Dia', 'Hora', 'Contigence']).reset_index(drop=True)
            RP.df = RP.df[['OP', 'Dia', 'Hora', 'Contigence', 'A_STAB', 'A_CODE', 'A_RCFC', 'A_NDRC', 'A_DAMP', 'A_INRT',
                                                              'B_STAB',                     'B_NDRC', 'B_DAMP', 'B_INRT']]

            net_info['OP'] = RP.df['OP'].values[0]

            RP.df = RP.df.merge(net_info, on='OP', how='left')

            vars = pd.concat([vars, RP.df]).reset_index(drop=True)
            
        vars.to_csv(PATH_DEST + folder + '_vars.csv', index=False)
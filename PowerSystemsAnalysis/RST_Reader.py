import pandas as pd
import json, os
import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib.colors import LinearSegmentedColormap
import numpy as np



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

        # print(reports)
        dict_report, actual_contigence, cont = {}, '0', 0
        for report in reports:
            
            for idx, var in enumerate(report[2:]):
                # print(var)

                try:
                    report[idx+2] = float(var)

                except:
                    report[idx+2] = var#print(self.path)


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
            print('SEGUNDO', self.path)
            
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

        ok = []
        for i in stab_points:

            conta = 5 - len(i)

            if conta > 0:
                for j in range(conta):
                    i.append(None)
                ok.append(i)

            else:
                ok.append(i[:5])
            # print(len(i))


        df = pd.DataFrame(ok)
        # print(df)

        try:
            df = pd.DataFrame(ok, columns=['Contigence', 'Contigence_Number', 'SIGLA', 'A', 'B'])#, 'C', 'D', 'E', 'F'

            df['OP'] = name
        
            df = df[['OP', 'Contigence', 'SIGLA', 'A', 'B']]
            df = df[df['SIGLA'].isin(['CODE', 'STAB', 'DAMP', 'RCFC', 'NDRC', 'INRT', 'PGTM'])]
            df = df.pivot_table(['A', 'B'], ['OP', 'Contigence'], 'SIGLA').reset_index(drop=False)

        except:
            try:
                df = pd.DataFrame(ok, columns=['Contigence', 'Contigence_Number', 'SIGLA', 'A'])

                df['OP'] = name
            
                df = df[['OP', 'Contigence', 'SIGLA', 'A']]
                df = df[df['SIGLA'].isin(['CODE', 'STAB', 'DAMP', 'RCFC', 'NDRC', 'INRT', 'PGTM'])]
                df = df.pivot_table(['A'], ['OP', 'Contigence'], 'SIGLA').reset_index(drop=False)
            except:
                df = None
        
        self.df = df
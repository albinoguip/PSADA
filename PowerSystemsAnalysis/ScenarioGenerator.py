from . NTW_Editor import *
from . DYN_Reader import *
from . WFS_Editor import *
from . EVT_Editor import *
from . PLV_Editor import *

import random


class ScenarioGenerator():

    def __init__(self, net_path, dyn_path=None):

        self.net = NTW_Editor(path=net_path, other=False)
        self.net.networkInfo(show=False)

        if dyn_path is not None:
            self.dyn      = DynamicData(path=dyn_path)
            self.dyn.Params()
            self.dyn_path = dyn_path

        self.net_path = net_path



    def Sbase(self, b_min=3, b_max=9, low=0.20, high=0.8):

        n_sm_change = random.sample(range(b_min, b_max), 1)
        sms         = random.sample(range(0, len(self.net.gen_data)), n_sm_change[0])
        multiplica  = [round(i, 2) for i in np.random.uniform(size=n_sm_change[0], low=low, high=high)]
        sm_multipli = [1 for i in range(len(self.net.gen_data))]

        for idx, sm in enumerate(sms):
            sm_multipli[sm] = multiplica[idx]

        for idx, (line_idx, sm_params) in enumerate(zip(self.dyn.sm_params.keys(), self.dyn.sm_params.values())):

            self.dyn.sm_params[line_idx]['Params']['Base(MVA)'] = self.dyn.sm_params[line_idx]['Params']['Base(MVA)']*sm_multipli[idx]


        self.net.gen_data['PMAX_MW'] = self.net.gen_data['PMAX_MW'].astype('float')*sm_multipli

        self.net.networkInfo(show=False)


    def Reforco(self, b_min=3, b_max=15):

        m_refo_cone = random.sample(range(b_min, b_max), 1)
        reforc_cone = random.sample(range(0, len(self.net.transmission_data)), m_refo_cone[0])

        # print(m_refo_cone)
        # print(reforc_cone)

        # print(self.net.transmission_data.iloc[reforc_cone])

        self.net.transmission_data['RL_PU'].iloc[reforc_cone] = self.net.transmission_data['RL_PU'].iloc[reforc_cone].astype('float')*0.5
        self.net.transmission_data['XL_PU'].iloc[reforc_cone] = self.net.transmission_data['XL_PU'].iloc[reforc_cone].astype('float')*0.5

        # print(self.net.transmission_data.iloc[reforc_cone])

        self.net.networkInfo(show=False)


    def RemoveLT(self, b_min=3, b_max=15):

        n_remo_cone = random.sample(range(b_min, b_max), 1)
        remove_cone = random.sample(range(0, len(self.net.transmission_data)), n_remo_cone[0])

        self.net.transmission_data = self.net.transmission_data.drop(remove_cone, axis=0).reset_index(drop=True)

        self.net.networkInfo(show=False)


    def RemoveGen(self):

        remove_gen  = [False, False, False, False, True][random.sample(range(0, 5), 1)[0]]
        gen_to_rem  = random.sample(range(0, len(self.net.transformer_data)), 1)[0] if remove_gen else None

        # print(gen_to_rem)

        if gen_to_rem is not None:
            self.net.transformer_data = self.net.transformer_data.drop([gen_to_rem], axis=0).reset_index(drop=False)

        self.net.networkInfo(show=False)


    def ChangeLoad(self, carga, min_load=0.60, max_load=0.95):

        carga = pd.read_csv(carga)

        carga   = carga[(carga['Total'] > self.net.total_PMAX_MW*min_load) & (carga['Total'] < self.net.total_PMAX_MW*max_load)]
        n_carga = random.sample(range(0, len(carga)), 1)[0]

        self.net.load_data['PL_MW']   = self.net.load_data['PL_MW'].astype('float')
        self.net.load_data['QL_MVAR'] = self.net.load_data['QL_MVAR'].astype('float')

        old_PL = self.net.load_data['PL_MW']
        old_QL = self.net.load_data['QL_MVAR']

        self.net.load_data['PL_MW']   = carga.iloc[n_carga].values[:-2]
        self.net.load_data['PL_MW']   = self.net.load_data['PL_MW'].round(decimals=1)
        self.net.load_data['QL_MVAR'] = self.net.load_data['PL_MW']*(old_QL/old_PL)
        self.net.load_data.loc[self.net.load_data['QL_MVAR'].isin([np.inf, -np.inf]), 'QL_MVAR'] = 0
        self.net.load_data['QL_MVAR'] = self.net.load_data['QL_MVAR'].round(decimals=1)


    def Save(self, net_path, dyn_path=None, wfs_path=None, wfs_list=None):

        self.net.save(save_path=net_path)

        if dyn_path is not None:
            self.dyn.save_params(save_path=dyn_path)

        if wfs_path is not None:
            WorkData(save_path=wfs_path, lista=wfs_list)


    def GenerateEvent(self, path):


        ED = EventData(time=30)

        # self.events.append([f'{evento:3d}    {info1:4d} {info2:4} {info3:4}      {param1:7.3f}  {param2:7.3f}     {time:5.3f}  \"xxxxxxxxxx  \"  \"xxxxxxxxxx  \"  {param3:7.3f}

        for gerador in self.net.gen_data['BUS_ID'].astype('int'):
            # print('\'GS\'', end=', ')
            ED.new_event(name='GS_'+str(gerador), evento=18, info1=gerador, param1=1, time=1, info2=0, info3=1, param2=0, param3=0)

        for load in self.net.load_data['BUS_ID'].astype('int'):
            # print('\'LS\'', end=', ')
            ED.new_event(name='LS_'+str(load), evento=17, info1=3, param1=100.00000, time=1, info2=load, info3=0, param2=100.00000, param3=0)

        for bus in self.net.bus_data['BUS_ID'].astype('int'):
            # print('\'CC\'', end=', ')
            ED.new_event(name='CC_'+str(bus), evento=27, info1=bus, param1=0.00000, time=1, info2=0, info3=0, param2=0.00000, param3=0)

        i = len(self.net.gen_data['BUS_ID']) + len(self.net.load_data['BUS_ID']) + 1
        for bus in self.net.bus_data['BUS_ID'].astype('int'):
            ED.append(n_event=i, evento=28, info1=bus, param1=0.00000, time=1.2, info2=0, info3=0, param2=0.00000, param3=0)
            i += 1

        ED.save(path)


    def GeneratePlot(self, path):

        PE = PLV_Editor(self.net_path)

        bus_info = self.net.bus_data
        gen_info = self.net.gen_data

        geradores = gen_info['BUS_ID'].astype('int').unique()
        buses     = bus_info['BUS_ID'].astype('int').unique()

        idx, points = 0, []
        for bus in buses:
            PE.new_variable(var='Ang(deg)', tipo='BUS', barra1=bus, eqp1=0, barra2=0, eqp2=0, multiplier=1)
            idx += 1
        points.append(idx)

        for bus in buses:
            PE.new_variable(var='Freq(Hz)', tipo='BUS', barra1=bus, eqp1=0, barra2=0, eqp2=0, multiplier=1)
            idx += 1
        points.append(idx)

        for bus in buses:
            PE.new_variable(var='V(pu)', tipo='BUS', barra1=bus, eqp1=0, barra2=0, eqp2=0, multiplier=1)
            idx += 1
        points.append(idx)


        for gerador in geradores:
            PE.new_variable(var='Ang(deg)', tipo='SM', barra1=gerador, eqp1=1, barra2=0, eqp2=0, multiplier=1)
            idx += 1
        points.append(idx)

        for gerador in geradores:
            PE.new_variable(var='W(pu)', tipo='SM', barra1=gerador, eqp1=1, barra2=0, eqp2=0, multiplier=1)
            idx += 1
        points.append(idx)

        for gerador in geradores:
            PE.new_variable(var='Vt(pu)', tipo='SM', barra1=gerador, eqp1=1, barra2=0, eqp2=0, multiplier=1)
            idx += 1
        points.append(idx)

        # print(points)

        PE.new_plot(name='BUS_Angle', variable_number=[i for i in range(1          , points[0]+1)])
        PE.new_plot(name='BUS_Freq' , variable_number=[i for i in range(points[0]+1, points[1]+1)])
        PE.new_plot(name='BUS_Volt' , variable_number=[i for i in range(points[1]+1, points[2]+1)])

        PE.new_plot(name='SM_Angle', variable_number=[i for i in range(points[2]+1, points[3]+1)])
        PE.new_plot(name='SM_Freq' , variable_number=[i for i in range(points[3]+1, points[4]+1)])
        PE.new_plot(name='SM_Volt' , variable_number=[i for i in range(points[4]+1, points[5]+1)])

        PE.save(path) 

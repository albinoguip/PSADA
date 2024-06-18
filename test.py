from PowerSystemsAnalysis import *
import networkx as nx


path = 'BASE/bus68.ntw'
NTW  = NTW_Reader(path, first_line=None)

NTW.fit()
NTW.concat_trans()

NTW.data_trans = NTW.data_trans[~(NTW.data_trans['BTO_ID'] == 18)]

nodes = NTW.graph_get_nodes(NTW.data_trans)

# print(NTW.data_trans[['BFR_ID', 'BTO_ID']])

# print(NTW.data_trans[NTW.data_trans['BTO_ID'] == 16])

# all_buses = list(NTW.data_trans['BFR_ID'].unique())
# all_buses.extend(NTW.data_trans['BTO_ID'].unique())
# all_buses = list(set(all_buses))

# print(NTW.bus_data['BUS_ID'].unique())

# G = nx.Graph()
# G.add_edges_from(nodes)

# for bus in NTW.bus_data['BUS_ID'].unique():

#     try:
#         a, b = nx.all_shortest_paths(G, 1, bus), []
#         for path in a:
#             b.extend(path)
#     except:
#         print('ISLAND DETECTED')
#         break


# NTW._find_limits_in_file()
# NTW._get_bus_data()
# NTW._set_bus_data()

NTW.save('BASE/bus68_teste.ntw')

# print(NTW.bus_data)
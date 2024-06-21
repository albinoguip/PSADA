from PowerSystemsAnalysis import *
import networkx as nx


path = 'C:/Users/Scarlet/Desktop/rev2_Remaneja Sto Antonio e Jirau/vars.csv'
RST = RST_Generic(report_path = path,
                  eol         = None,
                  sol         = None,
                  save_path   = None,
                  code_filtro = None)

print(RST._get_variables())
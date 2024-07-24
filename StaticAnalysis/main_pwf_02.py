from StaticAnalysis.LineAnalysis import *

scenario = 'V2A2F2_REV2_2026'
main_path = f"C:/Users/Gabriel/Desktop/PSADA/extract_data/{scenario}/StaticAnalysis/"
path_data = f"C:/Users/Gabriel/Desktop/PSADA/extract_data/{scenario}/StaticAnalysis/Data/Fluxo em Ramos/Df_Linhas.csv"
path_PWF_NC = f"C:/Users/Gabriel/Desktop/PSADA/extract_data/{scenario}/StaticAnalysis/Data/Geral/PWF_NC.csv"
pathtosave = main_path + '/Plots/Intercambios AC-DC/Lines_Analysis/'
os.makedirs(main_path + '/Plots/Intercambios AC-DC', exist_ok=True)
os.makedirs(pathtosave, exist_ok=True)

if __name__ == '__main__':

    PWF16_Filt = pd.read_csv(path_data)
    linha_teste = Analise_Linhas(PWF16_Filt)

    linha_teste.Removedor_n_convergiu(path_PWF_NC)
    linha_teste.Remover_e_salvar_L1MVA9999(pathtosave)
    linha_teste.Graficos_Por_REG(pathtosave)
    linha_teste.Graficos_Por_VBA(pathtosave)
    linha_teste.Analises_Especificas(pathtosave)
    linha_teste.Analise_PF(pathtosave)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PLV_Reader():
    
    def __init__(self, path, tipo="Organon"):
        
        self.path = path
        self.tipo = tipo
        
        if self.tipo == "Organon":
            self.rows = 5
            
        if self.tipo == "Anatem":
            self.rows = 6
            
        self.get_data()
        self.get_values()
        self.get_names()
        
        
    def get_data(self):
        
        with open(self.path) as f:
            self.lines = f.readlines()
            
        self.var_num = int(self.lines[0].strip())
        self.var_num = int(self.var_num)

        # print("Numero de variaveis: ", self.var_num)

        self.resto = self.var_num % self.rows
        # print("Variaveis na ultima: ", self.resto)

        if self.resto > 0:
            self.num_linhas = int(self.var_num / self.rows) + 1
        else:
            self.num_linhas = int(self.var_num / self.rows)

        # print("Numero de linhas:    ", self.num_linhas)

        self.doc_size = int((len(self.lines) - 1 - self.var_num)/self.num_linhas)
        # print("Tamanho do documento:", self.doc_size)

        self.variaveis = np.zeros((self.var_num, self.doc_size))
        # print("Matriz de variaveis: ", self.variaveis.shape)
        
    def get_values(self):
        
        linha = 1
        cont = 0
        for i in range(self.var_num + 1, len(self.lines)):

            temporaria = self.lines[i].split()

            for e in range(len(temporaria)):
                self.variaveis[e + ((linha - 1)*self.rows), cont] = float(temporaria[e])



            if linha == self.num_linhas:
                linha = 1
                cont += 1
            else:
                linha += 1
        
    def get_names(self):
        
        self.var_dic = {}

        for i in range(1, self.var_num + 1):    
            self.var_dic[self.lines[i].rstrip()] = self.variaveis[i-1]

        # print(self.var_dic.keys())

    def to_DataFrame(self):

        return pd.DataFrame(self.var_dic)

    def save(self, save_path):

        df = pd.DataFrame(self.var_dic)
        df.to_csv(save_path)


if __name__ == '__main__':

    import json

    
    path  = 'Ver/D_06_H_22-00_C_26.plt'
    teste = PLV_Reader(path=path,  tipo="Organon")

    labels = list(teste.var_dic.keys())

    df = teste.to_DataFrame()
    df = df.iloc[2500:2501]

    brigas = {'superior'  : [col for col in df.columns[1:] if df[col].values > 200],
              'medio'     : [col for col in df.columns[1:] if ((df[col].values < 200) & (df[col].values > -500))],
              'inferior1' : [col for col in df.columns[1:] if ((df[col].values < -500) & (df[col].values > -2000))],
              'inferior2' : [col for col in df.columns[1:] if df[col].values < -2000]}

    with open('ver/D_06_H_22-00_C_26.json', 'w') as fp:
        json.dump(brigas, fp, indent=3)


    print(df[df.columns[1]].values)

    # print(labels)

    fig = plt.figure()

    for i in range(1,len(labels)):

        plt.plot(teste.var_dic[labels[0]], teste.var_dic[labels[i]])
        plt.grid(True)

    plt.xlim([10, 15])
    plt.ylim([-3500, 1000])
    plt.show()
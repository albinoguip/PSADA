from . NTW_Reader import NTW_Reader
import numpy as np



class NTW_Editor(NTW_Reader): 

    def change_load(self, param, multi, spec=None, arre=2, keepFP=False):
        
        
        ite = spec if spec else [i for i in range(len(self.load_data))]
        
        if keepFP:
            for i in ite:      
                
                kw, kvar = self.load_data['PL_MW'].values[i], self.load_data['QL_MVAR'].values[i]
                FP       = np.cos(np.arctan(kvar/kw))
                
                kw_new   = kw*multi
                kvar_new = np.tan(np.arccos(FP))*kw_new
                
                self.load_data.loc[i, 'PL_MW']   = kw_new
                self.load_data.loc[i, 'QL_MVAR'] = kvar_new             

        else:      
            for i in ite:
                self.load_data[param][i] = round(float(self.load_data.iloc[i][param])*multi, arre)    
                
        self.cargaTotal = 0
        for i in self.load_data['PL_MW'].values:
            self.cargaTotal += float(i)

    def save(self, save_path):

        # BUS
        for idx, i in enumerate(range(self.f_bus, self.l_bus+1)):
            
            df = self.bus_data
            new_line  = f'{str(int(df.iloc[idx, 0])): >5}, \'{str(df.iloc[idx, 1]) : <12}\', {str(df.iloc[idx, 2]) : >8}, {str(int(df.iloc[idx, 3])) : >5}, '
            new_line += f'{str(int(df.iloc[idx, 4])): >5}, {str(df.iloc[idx, 5]) : >8}, {str(df.iloc[idx, 6]) : >8}, {str(int(df.iloc[idx, 7])) : >5}, '
            new_line += f'{str(int(df.iloc[idx, 8])): >5}, {str(df.iloc[idx, 9]): >14}, {str(df.iloc[idx, 10]): >14}, {str(df.iloc[idx, 11]): >8}, '
            new_line += f'{str(df.iloc[idx, 12]): >9}, {str(df.iloc[idx, 13]) : >8}, {str(df.iloc[idx, 14]) : >8}, {str(int(df.iloc[idx, 15])) : >5}, '
            new_line += f'{str(int(df.iloc[idx, 16])): >5}, {str(int(df.iloc[idx, 17])): >5} /'
                
            self.lines[i] = new_line + ' \n'      

        # LOAD
            
        for idx, i in enumerate(range(self.f_load, self.l_load+1)):

            df = self.load_data
            new_line  = f'{str(int(df.iloc[idx, 0])): >8}, {str(int(df.iloc[idx, 1])) : >8}, {str(int(df.iloc[idx, 2])) : >8}, {str(df.iloc[idx, 3]) : >8}, {str(df.iloc[idx, 4]): >8}, '
            new_line += f'{str(df.iloc[idx, 5]): >9}, {str(df.iloc[idx, 6]) : >8}, {str(df.iloc[idx, 7]) : >8}, {str(df.iloc[idx, 8]) : >8}, '
            new_line += f'{str(int(df.iloc[idx, 9])): >8}, {str(df.iloc[idx, 10]): >14}, {str(df.iloc[idx, 11]): >14}, {str(df.iloc[idx, 12]): >8} /'

            self.lines[i] = new_line + ' \n'          
        
        # GEN
        
        for idx, i in enumerate(range(self.f_gen, self.l_gen+1)):
            
            df = self.gen_data
            new_line  = f'{str(int(df.iloc[idx, 0])): >8}, {str(int(df.iloc[idx, 1])) : >8}, {str(df.iloc[idx, 2]) : >8}, {str(df.iloc[idx, 3]) : >8}, '
            new_line += f'{str(df.iloc[idx, 4]): >9}, {str(df.iloc[idx, 5]) : >8}, {str(df.iloc[idx, 6]) : >8}, {str(int(df.iloc[idx, 7])) : >8}, '
            new_line += f'{str(df.iloc[idx, 8]): >8}, {str(df.iloc[idx, 9]): >14}, {str(df.iloc[idx, 10]): >14}, {str(df.iloc[idx, 11]): >8}, '
            new_line += f'{str(int(df.iloc[idx, 12])): >9}, {str(df.iloc[idx, 13]) : >8}, {str(df.iloc[idx, 14]) : >8}, {str(df.iloc[idx, 15]) : >8}, '
            new_line += f'{str(int(df.iloc[idx, 16])): >8}, {str(int(df.iloc[idx, 17])): >14}, {str(int(df.iloc[idx, 18])): >14}, {str(int(df.iloc[idx, 19])): >8}, '
            new_line += f'{str(df.iloc[idx, 20]): >9}, {str(df.iloc[idx, 21]) : >8}, {str(df.iloc[idx, 22]) : >8}, {str(df.iloc[idx, 23]) : >8}, '
            new_line += f'{str(df.iloc[idx, 24]): >8}, {str(df.iloc[idx, 25]): >14}, {str(df.iloc[idx, 26]): >14}, {str(df.iloc[idx, 27]): >8}, '
            new_line += f'{str(df.iloc[idx, 28]): >9}, {str(df.iloc[idx, 29]) : >8}, {str(df.iloc[idx, 30]) : >8}, {str(int(df.iloc[idx, 31])) : >8}, '
            new_line += f'{str(df.iloc[idx, 32]): >8}, {str(int(df.iloc[idx, 33])): >14}, {str(int(df.iloc[idx, 34])): >14} /'
                
            self.lines[i] = new_line + ' \n'
            
        

        # TRANSMISSAO
            
        

        for idx, i in enumerate(range(self.f_tra, self.l_tra+1)):
            
            df = self.transmission_data
            try:
                new_line  = f'{str(int(df.iloc[idx, 0])): >8}, {str(int(df.iloc[idx, 1])) : >8}, \'{str(df.iloc[idx, 2]) : >8}\', {str(df.iloc[idx, 3]) : >8}, '
                new_line += f'{str(df.iloc[idx, 4]): >9}, {str(df.iloc[idx, 5]) : >8}, {str(df.iloc[idx, 6]) : >8}, {str(df.iloc[idx, 7]) : >8}, '
                new_line += f'{str(df.iloc[idx, 8]): >8}, {str(df.iloc[idx, 9]): >14}, {str(df.iloc[idx, 10]): >14}, {str(df.iloc[idx, 11]): >8}, '
                new_line += f'{str(df.iloc[idx, 12]): >9}, {str(df.iloc[idx, 13]) : >8}, {str(df.iloc[idx, 14]) : >14}, {str(df.iloc[idx, 15]) : >14}, '
                new_line += f'{str(df.iloc[idx, 16]): >14}, \'{str(df.iloc[idx, 17]): <14}\', {str(df.iloc[idx, 18]): >14}, {str(df.iloc[idx, 19]): >8}, '
                new_line += f'{str(df.iloc[idx, 20]): >9}, {str(df.iloc[idx, 21]) : >8}, {str(df.iloc[idx, 22]) : >8}, {str(df.iloc[idx, 23]) : >8}, '
                new_line += f'{str(df.iloc[idx, 24]): >8}, {str(df.iloc[idx, 25]): >14}, {str(df.iloc[idx, 26]): >14}, {str(df.iloc[idx, 27]): >8}, '
                new_line += f'{str(df.iloc[idx, 28]): >9}, {str(df.iloc[idx, 29]) : >8}, {str(df.iloc[idx, 30]) : >8}, {str(df.iloc[idx, 31]) : >8}, '
                new_line += f'{str(df.iloc[idx, 32]): >8}, {str(df.iloc[idx, 33]): >14}, {str(df.iloc[idx, 34]): >14}, '
                new_line += f'{str(df.iloc[idx, 35]): >8}, {str(df.iloc[idx, 36]): >14}, {str(df.iloc[idx, 37]): >14}, '
                new_line += f'{str(df.iloc[idx, 38]): >8}, {str(df.iloc[idx, 39]): >14} /'
                    
                self.lines[i] = new_line + ' \n'

            except:

                self.lines[i] = ''
            
            
            
        # TRANSFORMER

        df = self.transformer_data

        if 'index' in df.columns:

            for idx, i in enumerate(range(self.f_trs, self.l_trs+1)):

                df = self.transformer_data
                indexes = df['index'].values

                if idx%2==0:
                    try:
                        new_line  = f'{str(int(df.iloc[int(idx/2), 1])): >8}, {str(int(df.iloc[int(idx/2), 2])) : >8}, {str(df.iloc[int(idx/2), 3]) : >8}, \'{str(df.iloc[int(idx/2), 4]) : >8}\', '
                        new_line += f'{str(df.iloc[int(idx/2), 5]): >9}, {str(df.iloc[int(idx/2), 6]) : >8}, {str(df.iloc[int(idx/2), 7]) : >8}, {str(df.iloc[int(idx/2), 8]) : >8}, '
                        new_line += f'{str(df.iloc[int(idx/2), 9]): >8}, {str(df.iloc[int(idx/2), 10]): >14}, {str(df.iloc[int(idx/2), 11]): >14}, {str(df.iloc[int(idx/2), 12]): >8}, '
                        new_line += f'{str(df.iloc[int(idx/2), 13]): >8}, \'{str(df.iloc[int(idx/2), 14]): >9}\' /'
                            
                        self.lines[i] = new_line + ' \n'

                    except:

                        self.lines[i] = ''

                else:
                    jdx = int((idx-1)/2)
                    try:
                        tra = indexes[jdx]
                        self.lines[i] = self.lines[self.f_trs + 1 + 2*tra]

                    except:
                        self.lines[i] = ''

            
        
        # SAVE
            
        with open(save_path, 'w') as f:
            for line in self.lines:
                f.write(line)






if __name__ == '__main__':

    path = 'C:/Users/albing-local/Desktop/Data/DataForTest/9bus.ntw'

    NE = NTW_Editor(path)
    NE.change_gen()
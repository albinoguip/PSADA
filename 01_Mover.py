import os
from tqdm import tqdm



def remove_multiple_files_per_extension(batchs, extension):

    for batch in batchs: 
        
        path = f'D:/BATCH/BATCH_{batch}/NEWTON/' # DEIXAR PATH GENERICO
        hsts = [f for f in os.listdir(path) if f'.{extension}' in f.lower()]

        for hst in tqdm(hsts):
            os.remove(f'{path}{hst}')


def organize_files(batchs):

    for batch in batchs:

        con_o = f'D:/BATCH/BATCH_{batch}/No_Conv/'
        new_o = f'D:/BATCH/BATCH_{batch}/Conv/NEWTON/'
        dsa_o = f'D:/BATCH/BATCH_{batch}/Conv/DSA/'

        con_n = f'D:/BATCH/BATCH_{batch}/NO_CONV/'
        new_n = f'D:/BATCH/BATCH_{batch}/NEWTON/'
        dsa_n = f'D:/BATCH/BATCH_{batch}/DSA/'
        rst_n = f'D:/BATCH/BATCH_{batch}/RST/'



        os.rename(con_o, con_n)
        os.rename(new_o, new_n)
        os.rename(dsa_o, dsa_n)

        os.mkdir(rst_n)

        rsts = [f for f in os.listdir(new_n) if f'.rst' in f.lower()]

        for rst in tqdm(rsts):
            os.rename(f'{new_n}{rst}', f'{rst_n}{rst}')



if __name__ == '__main__':

    batchs = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']#'01', 
    
    # organize_files(batchs)
    remove_multiple_files_per_extension(batchs, 'dsa')

import pyautogui
import subprocess
import time
import os
import pandas as pd


# PATH      = 'C:/Users/Scarlet/Desktop/Power Systems Advanced Data Analysis Tool/9bus/9bus/'
# PATH_DEST = 'C:/Users/Scarlet/Desktop/Power Systems Advanced Data Analysis Tool/9bus/9bus_1_I_2_I_3_I/'

# ntws  = os.listdir(PATH)
# files = os.listdir(PATH_DEST)

# fake = [file.replace('.rst', '.ntw') for file in files if '.rst' in file]
# # print(fake)
# print(len(ntws), len(fake))
# ntws = set(ntws) - set(fake)
# print(len(ntws))

ntws = os.listdir('Data/AI/Dataset/Embeddings/')
ntws = {ntw.split('.')[0] for ntw in ntws}

vars          = pd.read_csv('Data/AI/Dataset/vars.csv')
ntws_vars     = vars['OP'].unique()#.values
ntws_vars_set = {ntw for ntw in ntws_vars}

print(ntws_vars_set-ntws)
print(ntws-ntws_vars_set)
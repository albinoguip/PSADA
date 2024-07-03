import pandas as pd
import os

batchs = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '14']

for batch in batchs:

    data  = pd.read_csv(f'D:/BATCH/BATCH_{batch}/DATABASE/train.csv')
    files = [f.split('.')[0] for f in os.listdir(f'D:/BATCH/BATCH_{batch}/DATABASE/NODE/')]
    data  = data[data['OP'].isin(files)]
    data.to_csv(f'D:/BATCH/BATCH_{batch}/DATABASE/train.csv', index=False)



    data  = pd.read_csv(f'D:/BATCH/BATCH_{batch}/DATABASE/valid.csv')
    files = [f.split('.')[0] for f in os.listdir(f'D:/BATCH/BATCH_{batch}/DATABASE/NODE/')]
    data  = data[data['OP'].isin(files)]
    data.to_csv(f'D:/BATCH/BATCH_{batch}/DATABASE/valid.csv', index=False)
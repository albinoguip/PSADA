import os
import shutil

batches = ['03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '14']

for batch in batches:

    if os.path.exists(f'D:/BATCH/BATCH_{batch}/DATABASE/GNN/'):
        shutil.rmtree(f'D:/BATCH/BATCH_{batch}/DATABASE/GNN/')
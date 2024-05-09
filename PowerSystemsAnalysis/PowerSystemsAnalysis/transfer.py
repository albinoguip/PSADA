import shutil, os
from tqdm import tqdm

PATH      = 'Data/AI/RawDataset/9bus/'
PATH_DEST = 'Data/AI/RawDataset/9bus_1_M_2_I_3_M/'
ntws = os.listdir(PATH)

print(len(ntws))

for ntw in tqdm(ntws):

    shutil.copyfile(PATH + ntw, PATH_DEST + ntw)
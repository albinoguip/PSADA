
import os, time


while True:
    os.system('taskkill /f /im hydra_pmi_proxy.exe')
    os.system('taskkill /f /im OrgProc.exe')
    time.sleep(120)
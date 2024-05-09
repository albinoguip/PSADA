import pyautogui
import subprocess
import time
import os

def run_script():
    b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/edit.PNG')
    w = b.width  / 2 + b.left
    h = b.height / 2 + b.top
    pyautogui.click(w, h, duration=0.25)
 
    time.sleep(0.2)

    b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/click.PNG')
    while (b is None):
        b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/click.PNG')
    
    w = b.width  / 2 + b.left
    h = b.height / 2 + b.top
    pyautogui.click(w, h, duration=0.25)


PATH      = 'C:/Users/Scarlet/Desktop/Power Systems Advanced Data Analysis Tool/9bus/9bus/'
PATH_DEST = 'C:/Users/Scarlet/Desktop/Power Systems Advanced Data Analysis Tool/9bus/9bus_1_I_2_I_3_I/'

ntws  = os.listdir(PATH)
files = os.listdir(PATH_DEST)

fake = [file.replace('.rst', '.ntw') for file in files if '.rst' in file]
# print(fake)
print('Total: ', len(ntws), 'Rodados: ', len(fake))
ntws = set(ntws) - set(fake)
print('Para rodar: ', len(ntws))

i = 0
for ntw in ntws:

    print(ntw)

    b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/script.PNG')
    while (b is None):
        run_script()    
        b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/script.PNG')

    w = b.width  / 2 + b.left
    h = b.height / 2 + b.top  + 50
    pyautogui.click(w, h, duration=0.25)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('del')
    pyautogui.write('Open "' + PATH_DEST + ntw.split('.')[0] + '.dsa"')
    pyautogui.hotkey('enter')
    pyautogui.write('DSA DOP')
    pyautogui.hotkey('enter')
    pyautogui.write('SAVE "' + PATH_DEST + ntw + '"')

    b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/script.PNG')
    w = b.width  / 2 + b.left
    h = b.height / 2 + b.top
    pyautogui.click(w, h, duration=0.25)

    pyautogui.move(20, 0)

    time.sleep(1)

    erro = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/erro.PNG')
    while (erro is not None):

        b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/run.PNG')
        w = b.width  / 2 + b.left
        h = b.height / 2 + b.top
        pyautogui.click(w, h, duration=0.25)

        pyautogui.press(['up', 'up', 'enter'])    

        b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/script.PNG')
        while (b is None):
            run_script() 
            b = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/script.PNG')   

        w = b.width  / 2 + b.left
        h = b.height / 2 + b.top
        pyautogui.click(w, h, duration=0.25)

        pyautogui.move(20, 0)

        time.sleep(1)

        erro = pyautogui.locateOnScreen('C:/Users/Scarlet/Desktop/Power Systems Data Analysis Tool/erro.PNG')
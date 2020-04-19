import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from os.path import expanduser

import time as t
from pygame import mixer
mixer.init()
fpath = os.path.join(os.getcwd(),"Eye.mp3")

mixer.music.load("Eye.mp3")
import getpass
usernm = getpass.getuser()
from datetime import datetime



   
    
def userDirFinder():
    from os.path import expanduser
    usrpth = expanduser("~")
    mainp = os.path.join(usrpth, "Documents")
    return mainp
    
def checknSetdir():
    mainp=userDirFinder()
    target_path = os.path.join(mainp,"HealthManger","Eye_Excercise_log")
    
    if os.path.exists(target_path):
        os.chdir(target_path)
    else:
        
        os.makedirs(target_path)
        os.chdir(target_path)
        
    
def getCurrentDateandTime():
    Dat = datetime.now()
    
    currentD = Dat.strftime("%d/%m/%Y") 
    currentT = Dat.strftime("%I:%M %p")
    return currentD , currentT
    

    

def timCount():
    mins =1
    hr = 0
    while mins!=0:
        sec = 20
        while sec >= 0:
           
            t.sleep(1)
           
            os.system("cls")
            print("Timer Started For Next Eye Break")
            print(f"Time left: {hr}:{mins}:{sec}")
            
         
            sec-=1
        print("Countdown paused")
        # mixer.music.load("Eye.mp3")
        mixer.music.play(-1)

        logCreater()
        mixer.music.stop()
        
        mins-=1

def logCreater():
        print("Countdown paused")
       
        mixer.music.play(-1)
        write_msg = f"Eye Excercise Done by {usernm}"
        
       
        while 1:
        
            try:
                usr_msg = input("Type \"Done\" to stop this alarm: ")
                
                usr_msg = usr_msg.lower()
                if usr_msg != "done":
                    raise ValueError("Invalid Answer")
                elif "done" == usr_msg:
                    checknSetdir()
                    with open("eye_excercise_log.txt","a") as fi:
                        cdat , ctim = getCurrentDateandTime()
                        fi.write(f"Date: {cdat}          Time: {ctim}          Message: {write_msg}\n")
                        # print("Log Created")
                        mixer.music.stop()
                        break
                        
                
            except Exception as e:
                print(e)
    
            
def logReader():
         
        try:
            checknSetdir()
            
            with open("eye_excercise_log.txt","r") as fi:
                lis = fi.readlines()
                for i in lis:
                    print(i)
            input("Press to contiue")
        except FileNotFoundError:
            print("File is not created Yet")
            input("Press to contiue")
            
    

# if __name__ =="__main__":
#     logCreater()
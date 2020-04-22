
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from os.path import expanduser
import time as t
import pygame




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
    target_path = os.path.join(mainp,"HealthManger","Physical_Excercise_log")
    
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
 
def logCreater():
        print("Countdown paused")
        current_dir = os.getcwd()
        pygame.mixer.init()
        pygame.mixer.music.load("Physound.mp3")
        pygame.mixer.music.play(-1)
        write_msg = f"Physical Excercise Done by {usernm}"
        while 1:
        
            try:
                print("Time for a Physical Excercise Break , After the Physical Excercise Break")
                usr_msg = input("Type \"Done\" to stop this alarm: ")
                
                usr_msg = usr_msg.lower()
                if usr_msg != "done":
                    raise ValueError("Invalid Answer")
                elif "done" == usr_msg:
                    checknSetdir()
                    with open("Physical_Excercise_log.txt","a") as fi:
                        cdat , ctim = getCurrentDateandTime()
                        fi.write(f"Date: {cdat}          Time: {ctim}          Message: {write_msg}\n")
                        # print("Log Created")
                        pygame.mixer.music.stop()
                        pygame.mixer.quit()
                        os.chdir(current_dir)
                        # pygame.mixer.music.unload()
                        break
                        
                
            except Exception as e:
                print(e)
    
def logReader():
        
        checknSetdir()
        try:
            print(os.getcwd())
            with open("Physical_Excercise_log.txt","r") as fi:
                lis = fi.readlines()
                for i in lis:
                    print(i)
            input("Press to contiue")
        except FileNotFoundError:
            print("No log is created yet")
            input("Press to contiue")

    

if __name__ =="__main__":
    print("Please Run the MainModule.py only")
    input("Press Enter to continue...")
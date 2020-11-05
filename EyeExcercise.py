import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from os.path import expanduser

import time as t
import getpass
usernm = getpass.getuser()
from datetime import datetime
import pygame
current_dir = "none"
from plyer import notification

   
    
def userDirFinder():
    from os.path import expanduser
    usrpth = expanduser("~")
    mainp = os.path.join(usrpth, "Documents")
    return mainp
    
def checknSetdir():
    mainp=userDirFinder()
    target_path = os.path.join(mainp,"Programmers_Alram","Eye_Excercise_log")
    
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
    

def notifier():
    
   
    notification.notify(
            title = "Time for a Eye Excercise break.",
            message ="Please do eye excercise and after that open the program and type \"Done\" in the Program Windows",
            app_icon = ".\\Notification_Icons\\Eye.ico",
            app_name = "Programmers alarm"
            
        
        )
    t.sleep(4)


def logCreater():
        
        notifier()
        current_dir = os.getcwd()
        
        print("Countdown paused")
        pygame.mixer.init()
        pygame.mixer.music.load(".\\Notification_Sounds\\Eyesound.mp3")
        pygame.mixer.music.play(-1)
       
        write_msg = f"Eye Excercise Done by {usernm}"
        
       
        while 1:
            os.system('cls')
            try:
                print("Time for a Eye Excercise Break , After the Eye Excercise")
                usr_msg = input("Type \"Done\" to stop this alarm: ").strip()
                
                usr_msg = usr_msg.lower()
                if usr_msg != "done":
                    raise ValueError("Invalid Answer")
                elif "done" == usr_msg:
                    checknSetdir()
                    with open("eye_excercise_log.txt","a") as fi:
                        cdat , ctim = getCurrentDateandTime()
                        fi.write(f"Date: {cdat}          Time: {ctim}          Message: {write_msg}\n")
                        
                        
                        pygame.mixer.music.stop()
                        pygame.mixer.quit()
                        os.chdir(current_dir)
                        break
                        
                
            except Exception as e:
                print(e)
                input("Press Enter to Continue")
            
            
def logReader():
         
        try:
            checknSetdir()
            
            with open("eye_excercise_log.txt","r") as fi:
                lis = fi.readlines()
                for i in lis:
                    print(i)
            input("Press to contiue")
        except FileNotFoundError:
            print("No Log is created Yet")
            input("Press to contiue")
        except Exception as e:
            print(e)
            input("Press Enter to Continue")
            
    

if __name__ =="__main__":
    
    print("Please Run the MainModule.py only")
    input("Press Enter to continue...")
    
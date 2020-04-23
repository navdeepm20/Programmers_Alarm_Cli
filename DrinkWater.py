
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame



import time as t
import getpass
from datetime import datetime
usernm = getpass.getuser()




    
    
def userDirFinder():
    from os.path import expanduser
    usrpth = expanduser("~")
    mainp = os.path.join(usrpth, "Documents")
    return mainp
    
def checknSetdir():
    mainp=userDirFinder()
    target_path = os.path.join(mainp,"HealthManger","Water_log")
    
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
        current_dir = os.getcwd()
        pygame.mixer.init()
        pygame.mixer.music.load("Watersound.mp3")
        pygame.mixer.music.play(-1)
        write_msg = f"Drink Water Done by {usernm}"
        while 1:
        
            try:
                print("Time for a Water Break , After the Water Break")
                usr_msg = input("Type \"Done\" to stop this alarm: ")
                
                usr_msg = usr_msg.lower()
                if usr_msg != "done":
                    raise Exception("Invalid Answer")
                elif "done" == usr_msg:
                    
                    checknSetdir()
                    
                    with open("waterlog.txt","a") as fi:
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
            
            with open("waterlog.txt","r") as fi:
                lis = fi.readlines()
                for i in lis:
                    print(i)
            input("Press to contiue")
        except FileNotFoundError:
            print("No log is created yet")
            input("Press to contiue")
        except Exception as e:
            print(e)
            input("Press Enter to Continue")
            
        
             
if __name__ == "__main__":
    logCreater()
    #print("Please Run the MainModule.py only")
    #input("Press Enter to continue...")


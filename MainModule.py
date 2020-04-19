
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
mins = 0
from os.path import expanduser
usrpath = expanduser("~")
import getpass
usrnm  = getpass.getuser()
import time as t

import DrinkWater
import EyeExcercise
import PhysicalExcercise

def timCount():         #This function is used to create a clock for the program to work. This works for the 8 hours.
    hr = 0
    
    
    while hr<=8:

        mins = 0
        while mins<=2:
           
            sec = 1
            while sec <= 5:
               
                t.sleep(1)
                
                os.system('cls')
                if mins < 1:
                
                    print("Timer Started For Next Water Break")
                    print(f"Time left: {hr}:{mins}:{sec}")
                if mins >=1 and mins < 2:
                    print("Timer Started For Next Eye Break")
                    print(f"Time left: {hr}:{mins}:{sec}")
                if mins >=2 and mins < 3:
                    print("Timer Started For Next Physical Break")
                    print(f"Time left: {hr}:{mins}:{sec}")
                    
                sec+=1
            mins+=1
            
            if mins == 1:
                
                DrinkWater.logCreater()
            if mins == 2:
                
                EyeExcercise.logCreater()
            if mins == 3:
                
                PhysicalExcercise.logCreater()
                
                
                
                
        
        hr+=1
 
def logReaderChoiceSelector():  #This  Fuction is used to select the right option to read the right log file
    
    while True:
        
        os.system('cls')
        print("Select the below option to read the desired log --\n\n")
        print("1)Read WaterExcercise log\n2)Read EyeExcercise log\n3)Read PhysicalExcercise log\n4)Back to previous menu\n")
        try:
            choc = int(input())
            if choc == 1:
                DrinkWater.logReader()
            elif choc == 2:
                EyeExcercise.logReader()
            elif choc == 3:
                PhysicalExcercise.logReader()
            elif choc == 4:
                mainModule()                
            else:
                print("Enter the key from the given options above")
                input()    
        except ValueError:
            print("Enter the correct numbers only")
        except KeyboardInterrupt:
            print("Thankyou,See You Again.....")
            input("Press Enter to Exit")
            exit()
        except EOFError:
            print("Thankyou,See You Again.....")
            input("Press Enter to Exit")
            exit()
        
        
            

def mainModule():       #This is the main function which show the option menu to select the desired choice 
    try:
        while True:
        
            os.system('cls')
        
            print(f"-------------------Hello {usrnm}-------------------\n")
            print("-------------Welcome to health manger--------------\n")
            print("1)Start the Program\n2)See logs\n3)Exit the program\n")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Press Ctrl+c to stop the countdonwn")
                input("Press Enter to continue...")
                
                while True:
                    timCount()
            elif choice == 2:
                logReaderChoiceSelector()
            elif choice == 3:
                    exit()
            else:
                print("Enter the right choice")
                input("Press Enter to continue...")

    except KeyboardInterrupt:
            print("\n\nThankyou,See You Again.....")
            input("Press Enter to Exit")
            exit() 
    except EOFError:
            print("\n\nThankyou,See You Again.....")
            input("Press Enter to Exit")
            exit()    
    except ValueError:
            print("Enter a valid choice only: ")
#The Main Script starts from here.

mainModule()




if __name__ == "__main__":
        mainModule()
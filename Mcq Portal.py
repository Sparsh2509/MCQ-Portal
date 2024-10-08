import random
import time
import datetime

def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 
  
  

t = input("Enter the time in seconds: ") 
  

countdown(int(t)) 

##def loginpage():
    
##    try:
##
##        lower = "abcdefghijklmnopqrstuvwxyz"
##        numbers = "0123456789"
##
##
##        string = lower + numbers 
##        length = int(input("How Many Characters Do You Want Your Password To Be: "))
##        password = "".join(random.sample(string, length))
##        print("Here Is Your Password: ", password)
##        print()
##        usern=input("Enter Username: ")
##        paws=input("Enter the given password: ")
##        if usern.lower()=="student" and paws==password:
##            print()
##            print("LOADING",end="")
##            for _ in range(3):
##                print(".",end="")
##                time.sleep(0.5)
##            print("LOGGED IN TO ---")
##            print()
##            while True:
##                global now
##                now = datetime.datetime.now()
##                print("_"*75)
##                print("""
##                                   WELCOME TO MCQ TEST PORTAL                       {}
##    0)EXIT
##    1)MATHEMATICS
##    2)SCIENCE
##    3)GENERAL KNOWLEDGE
##    4)CODING QUES ON PYTHON LANGUAGE
##    
##    """.format(now.strftime('%d-%m-%Y %H:%M')))
##                break
##                
##                print()
##                val=intinput("CHOOSE THE TASK : ")
##                if val == 0:
##                       return
##                elif val == 1:
##                    print()
##                    addrecord()
##                elif val == 2:
##                    print()
##                    sortingpage()
##                elif val == 3:
##                    print()
##                    update()
##                elif val == 4:
##                    print()
##                    delete()
##                else:
##                    print()
##                    print("PLEASE ENTER CORRECT TASK !! ")    
##            
##        else:
##            print()
##            print("INCORRECT USERNAME OR PASSWORD!!!")
##            print("TRY AGAIN..")
##            loginpage()
##            
##    except:
##        print()
##        print(" SOMETHING WENT WRONG !!!")
##        print(" TRY AGAIN ")
##    
##
##def main():
##    
##    try:
##        random_password()
##        loginpage()
##
##    except:
##         print("NO FUNCTION CALLED")
##
##
##main()
##

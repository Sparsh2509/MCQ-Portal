import random
import time
import datetime

def loginpage():
    

        lower = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"


        string = lower + numbers 
        length = intinput("How Many Characters Do You Want Your Password To Be: ")
        password = "".join(random.sample(string, length))
        print("Here Is Your Password: ", password)
        print()
        usern=input("Enter Username: ")
        paws=input("Enter the given password: ")
        if usern.lower()=="student" and paws==password:
            print()
            print("LOADING",end="")
            for _ in range(3):
                print(".",end="")
                time.sleep(0.5)
            print()
            print("LOGGED IN TO ---")
            print()
            while True:
                global now
                now = datetime.datetime.now()
                print("_"*75)
                print("""
                                   WELCOME TO MCQ TEST PORTAL                       {}
    0)EXIT
    1)MATHEMATICS
    2)SCIENCE
    3)GENERAL KNOWLEDGE
    4)CODING QUES ON PYTHON LANGUAGE
    
    """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
                
                print()
                val=intinput("CHOOSE THE TASK : ")
                if val == 0:
                       print("Thanks for Visiting...")
                       break
                # elif val == 1:
                #     print()
                #     mathematics()
                # elif val == 2:
                #     print()
                #     science()
                # elif val == 3:
                #     print()
                #     general_knowlegde()
                elif val == 4:
                    print()
                    print("Python MCQ test will start in 15 seconds")
                    countdown(15)
                    python_mcq()
                else:
                    print()
                    print("PLEASE ENTER CORRECT TASK !! ")  
        else:
            print()
            print("INCORRECT USERNAME OR PASSWORD!!!")
            print("TRY AGAIN..")
            loginpage()               

def intinput(statement):
    
    while True:
        
        try:
            x=int(input(statement))
            return x   
            
        except:
            print()
            print("****Integer Value Required****")
            print()

def python_mcq():

        global now
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    PYTHON QUES MCQ                     {}
        
        INSTRUCTIONS FOR CANDIDATES DURING EXAMINATIONS!!!
        
        1)There are total 10 mcq based questions in the test.
        2)Each question carries 10 marks.
        3)Grade will be provided according to the marks obtained.
        4)Number of correct and wrong answers also provided to candidates.
        
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print("Question 1 is coming up in 30 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(30)
        python_ques()
                    
    

sum_py = 0
correct_py=0
wrong_py=0
def python_ques():
    
        global now
        global sum_py 
        global correct_py
        global wrong_py
        sum=0
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 1                    {}
                                    
        1) What is the maximum possible length of an identifier?

           (A) 16
           (B) 32
           (C) 64
           (D) None of these above        
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "d":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()


        print("Question 2 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 2                    {}
                                    
        2) Who developed the Python language?

           (A) Zim Den
           (B) Guido van Rossum
           (C) Niene Stom
           (D) Wick van Rossum       
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "b":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()


        print("Question 3 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 3                   {}
                                    
        3) In which language is Python written?

          (A) English
          (B) PHP
          (C) C
          (D) All of the above       
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "c":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()


        print("Question 4 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 4                 {}
                                    
        4) What do we use to define a block of code in Python language?

           (A) Key
           (B) Indentation
           (C) Brackets
           (D) None of these       
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "b":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()

        print("Question 5 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 5                   {}
                                    
        5) Which character is used in Python to make a single line comment?

            (A) #
            (B) //
            (C) /
            (D) !       
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "a":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1

        print("Question 6 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 6                 {}
                                    
        6) What will be the datatype of the var in the below code snippet?
            var = 10
            print(type(var))
            var = "Hello"
            print(type(var))
              
            What will be the output of this code?

            (A) str and int
            (B) int and int
            (C) str and str
            (D) int and str       
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "d":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()

        print("Question 7 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 7                  {}
                                    
        7) What will be the output of the following code snippet?
            a = [1, 2, 3]
            a = tuple(a)
            a[0] = 2
            print(a)
              
            What will be the output of this code?  

            (A) [2,2,3]
            (B) (2,2,3)
            (C) error
            (D) (1,2,3)     
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "c":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()       

        print("Question 8 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 8                   {}
                                    
        8) What will be the output of the following code snippet?  
            a = [1, 2, 3, 4, 5]
            sum = 0
            for ele in a:
            sum += ele 
            print(sum)
              
            What will be the output of this code?   

           (A) 15
           (B) 0
           (C) 20 
           (D) None of these       
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "a":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()        
        
        print("Question 9 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 9                   {}
                                    
        9) What will be the output of the following code snippet?
            def check(a):
                if a%2==0:
                   print("Even")
                else:
                    print("odd")
   
            check(12)
            
            What will be the output of this code?     
               
           (A) Even 
           (B) Odd
           (C) Error
           (D) None      
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "a":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1
        print()        

        print("Question 10 is coming up in 5 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        countdown(5)
        now = datetime.datetime.now()
        print("_"*75)
        print("""
                                    Question 10                   {}
                                    
        10) What will be the output of the following code snippet?
              
            print(2**3 + (5 + 6)**(1 + 1))
              
            What will be the output of this code?  

           (A) 129
           (B) 8
           (C) 121
           (D) None of the above       
        """.format(now.strftime('%d-%m-%Y %H:%M')) .format())
        print()
        val=input("CHOOSE THE OPTION : ")
        if val.lower() == "a":
            sum_py+=10
            correct_py+=1
            
        else:
            wrong_py+=1

        print("Number of correct answers = ",correct_py)
        print("Number of wrong answers = ",wrong_py)       
        sum+=sum_py 
        # print("total sum = ",sum) 
        grade(sum)
        print("You can choose another test type in 30 sec",end="")
        for _ in range(3):
              print(".",end="")
              time.sleep(0.5)
        print()
        print("Take a break!!!")
        
        countdown(30)

def grade(a):

    if a >=90 and a<=100:
        print("You secure A grade....Well done")    
    elif a>=75 and a<90:
         print("You secure B Grade...good attempt")  
    elif a>=50 and a<75:
         print("You secure C Grade...u can do better")  
    else:
         print("Fail")        
         print("Practice More")


def countdown(t): 
    
     while t>-1: 
         mins, secs = divmod(t, 60) 
         # timer = '{:02d}:{:02d}'.format(mins, secs) 
         print('{:02d}:{:02d}'.format(mins, secs), end="\r") 
         time.sleep(1) 
         t -= 1
     print()
##     print("Time's Up")  

def main():
   
    loginpage()

main()

#to define a function with calc()
import math
def calc():
    logo = ("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
    print(logo)
    print("!!WELCOME TO THE SIMPLE CALCULATOR!!")
    print("Addition        =1")
    print("Substraction    =2")
    print("Mulitiplication =3")
    print("Divison         =4")
    print("Reminder        =5")
    print("Exponential     =6")
    print("Sqrt of a number=7")
    print("choose any numbers given above according to your need.")
    num = int(input("Enter a number:\n"))
    if num == 1:
        # num=int(input("Enter a number:\n"))
        num1 = int(input("Enter a number:\n"))
        num2 = int(input("Enter a number:\n"))
        result = int(num1 + num2)
        print(f"Your added number is {result}")
    elif num == 2:
        num2 = int(input("Enter a number:\n"))
        num3 = int(input("Enter a number:\n"))
        result1 = int(num2 - num3)
        print(f"Your substracted number is {result1}")
    elif num == 3:
        num4 = int(input("Enter a number:\n"))
        num5 = int(input("Enter a number:\n"))
        result2 = int(num4 * num5)
        print(f"Your multiplied number is {result2}")
    elif num == 4:
        num6 = int(input("Enter a number:\n"))
        num7 = int(input("Enter a number:\n"))
        result3 = round(num6 / num7,2)
        print(f"Your divided  number is {result3}")
    elif num == 5:
        num8 = int(input("Enter a number:\n"))
        num9 = int(input("Enter a number:\n"))
        result4 = int(num8 % num9)
        print(f"The reminder of the the numbers is {result4}")
    elif num==6:
        num10=int(input("Enter a base number:\n"))
        num11=int(input("Enter an exponent:\n"))
        result5=int(num10**num11)
        print(f"Exponetial Value is:{result5}")
    elif num==7:
        num12=int(input("Enter a number:\n"))
        sqRoot=round(math.sqrt(num12))
        print(f"The square root of {num12} is",sqRoot)
    else:     
       print("You have enter a wrong number choose the exact number")     
# To run again the program
should_continue=True
while should_continue:
    #to call the function.
    calc()
    restart= input("If you want to go again type yes otherwise no \n")
    if restart=="yes":
        calc()
        
    if restart=="no":
        should_continue=False
        print("Goodbye ,Thanks for using me.")
    else:
        print("you entered wrong input choose correct choice")
   # else:
        
        
        #print("You have enter a wrong number choose the exact number")


#BMI CALCULATOR 2.0
print("!!WELCOME TO BMI CLACULATOR 2.0!!")
w = float(input("Enter Your weight in kg:\n"))
h= float(input("Enter Your height in m:\n"))
#BMI =weight(kg)/height(m)*2
bmi = round(w/h**2)

if bmi <18.5:
    print(f"Your bmi is:{bmi} ,You are under weight")
elif bmi <25:
    print(f"Your bmi is:{bmi} ,You have normal weight")
elif bmi <30:
    print(f"Your bmi is:{bmi} ,You are  slightly over weight")
elif bmi<35:    
    print(f"Your bmi is:{bmi} ,You are obese")
else:
    print(f"Your bmi is:{bmi} ,You are clinically obese")
    

   



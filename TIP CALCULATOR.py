#Tip Calculator
#no of persons 5
#tip givee by the each of person is calculated by the following method (150/5)*1.12
#bill_amount_per_person rounded by 2 decimal places.
print("!!WELOME TO THE TIP CALCULATOR!!")
#t = total amount
#tp = tip percentage
#p = people
t = float(input("What was   the total amount:\n $"))
tp =int(input("What percentage of the tip would you to give: 10 ,15 or 12\n"))        
p =int(input("How many people to split the bill:\n"))
#tip_as_percentage=tsp
tsp=float(tp/100)
total_tip_amount=(t*tsp)
total_bill_amount=(t+total_tip_amount)
bill_amount_per_person=(total_bill_amount/p)
#e= bill_amount_person
e=round(bill_amount_per_person ,2)
e="{:.2f}".format(bill_amount_per_person)
print(f"Each  person should pay: ${e}\n")





 
           
             
                    
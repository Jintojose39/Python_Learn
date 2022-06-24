#To Crate program for making bank roulete bot for who is the person to pay the bill in hotel
#using functions like random choice and random.randint
import random
name_string =input("Give me everybody name ,separated by coma:\n")
#to convert string into the list .
names =name_string.split(",")
# print(names)
#to find the total numbers of the string
#print(len(names))
num_items =len(names)
random_choice =random.randint(0,num_items-1)
person_is_going_to_pay_today =names[random_choice]
#person_is_going_to_pay_today =random.choice(names)
print(person_is_going_to_pay_today + " "+"is going to pay today")
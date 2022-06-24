import random
print("!!Think Head or Tails in your mind!!\n")
toss=input("Press any key to see your prediction:\n")
random_side =random.randint(0,1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

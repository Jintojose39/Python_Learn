logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("!!Welcome to Secret Auction Program!!")
#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#rom art import logo
#print(logo)
bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
  highest_bid=0
  winner=" "
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner} with bid of {highest_bid}")

while not  bidding_finished:
  name=input("What is your name?:")
  price=int(input("What is your bid amount?: $"))
  bids[name]=price
  should_continue =input("Are they are any other bidders.Type yes or no:\n")
  if should_continue=="no":
    bidding_finished=True
    find_highest_bidder(bids)
  else:
      print("Thanks for being with us")
  
      
    
  
   

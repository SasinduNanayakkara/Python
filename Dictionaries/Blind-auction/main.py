from replit import clear
#HINT: You can call clear() to clear the output in the console.

bit = {} #intialize the dictionary

def Find_the_max_bid(bidding_record):
  max_bid = 0
  
  for bidder in bidding_record:#loop through the dictionary
    bid_amount = bidding_record[bidder]# assign the bid value into the variable
    if bid_amount > max_bid:# check the maximum bid
      max_bid = bid_amount
      winner = bidder
    else:
      max_bid = max_bid
  print(f"The winner id {winner} with the bid of ${max_bid}") #print the winner


responce = "yes"
from art import logo
print(logo) #print the logo 

finished_bidding = False
while not finished_bidding:# until user enter 'no' loop through it

  name = input("What is your name : ")
  price = int(input("What's your bit : "))

  bit[name] = price # assign the user entered price into the dictionary

  responce = input("Are there any other bidders? type 'yes' or 'no' :  ") # get the user responce

  if responce == "no": # if there are no more bids
    finished_bidding = True
    Find_the_max_bid(bit)
  elif responce == "yes": # if there more bids
    clear() #clear the console(from repl.it package)

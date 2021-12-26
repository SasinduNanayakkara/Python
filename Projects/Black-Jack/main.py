

def deal_card():# card selection function
  """Returns a random card from the deck."""#function definition
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card #return randomly generated card


def calculate_score(cards): # score calculation function
  """Take a list of cards and return the score calculated from the cards"""#function definition

  if sum(cards) == 21 and len(cards) == 2: # check sum of the cards and there are only 2 cards
    return 0
 
  if 11 in cards and sum(cards) > 21:# chek for and 11()ace.if score is already over 21 remove the 11 and replace it with 1.
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score): #compare function
 
  if user_score > 21 and computer_score > 21:# check both player's score above 21
    return "You went over. You lose 😤"


  if user_score == computer_score: #check the draw situation
    return "Draw 🙃"
  elif computer_score == 0: #check computer's blackjack
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0: # check user's blackjack
    return "Win with a Blackjack 😎"
  elif user_score > 21: #chek users overflow
    return "You went over. You lose 😭"
  elif computer_score > 21:# check computer's overflow
    return "Opponent went over. You win 😁"
  elif user_score > computer_score: #compare user's and computer's score
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game(): # the main function

  print(logo) #print the blackjack logo

  
  user_cards = [] #create user card list
  computer_cards = [] #create computer card list
  is_game_over = False

  for _ in range(2): #add randomly generated cards into the list
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over: #until user decide to end the game
   
    user_score = calculate_score(user_cards) #calculate the user's score using calculate_score function
    computer_score = calculate_score(computer_cards) #calculate computer's score using calculate_score function
    print(f"   Your cards: {user_cards}, current score: {user_score}") #print the values
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21: # fix the bugs
      is_game_over = True
    else:
      
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ") # if user want get another card, add a card using deal_card function
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  
  while computer_score != 0 and computer_score < 17: #until computer score grater than 0 and lower than 16
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)# add cards to the computers list using deal_card function

# print the final result
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))# print the final reslut


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y": # get the user's decition to play another round
  clear()
  play_game()

import random 
from replit import clear


def blackjack():
  print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
      
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # 11 is ace
    random_card = cards[random.randint(0,12)]
    return random_card
    
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
      
    return sum(cards)
  
  def compare(user_score, computer_score):
    if user_score == computer_score:
      return "It's a draw!"
    elif computer_score == 0:
      return "You lose!"
    elif user_score == 0:
      return "You win!"
    elif user_score > 21: 
      return "You lose!"
    elif computer_score > 21:
      return "You win!"
    elif user_score > computer_score:
      return "You win!"
    else:
      return "You lose!"
  
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not is_game_over:
    user_score =calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are: {user_cards}. Current score: {user_score}")
    print(f"The computer's first card is: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      draw = input("Do you want to draw another card? Type 'y' or 'n'. ")
    if draw == 'y':
      user_cards.append(deal_card())
    else:
      is_game_over = True
    
  while computer_score > 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  answer = input("Do you want to restart the game? Type 'y' or 'n'.")
  if answer == 'y':
    clear()
    blackjack()
  else: 
    exit(0)


blackjack()

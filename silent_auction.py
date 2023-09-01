#Secret Auction Program
from replit import clear()
print( '''
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
''')
to_continue = 'y'
auction_dict = {}
while to_continue == 'y':
 
  name = input("What is your name?\n")
  bid_price = input("How much do you want to bid? $")
  auction_dict[name] = bid_price
  to_continue = input("Are there any other users who want to bid? Type y/n.\n")
  if to_continue == 'y':
    clear()

if auction_dict:
  max_bidder, max_bid = max(auction_dict.items(), key = lambda x: x[1])
  print(f"The winner is {max_bidder} with ${max_bid}.")
else: 
  print("No bids were entered.")
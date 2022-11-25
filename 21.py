import os
import random
cards=["A",2,3,4,5,6,7,8,9,10,10,10,10,"A",2,3,4,5,6,7,8,9,10,10,10,10,"A",2,3,4,5,6,7,8,9,10,10,10,10,"A",2,3,4,5,6,7,8,9,10,10,10,10]
def random_card(ComOrNot):
  card =random.choice(cards)
  
  if card =="A":
    ace_done=True
    while ace_done:
      if ComOrNot:
        choice=11      
      if not ComOrNot:
        choice =int(input("you got ace choose 1 or 11: "))

      if choice==1:
        ace_done=False
        return 1
      elif choice==11:
        ace_done=False
        return 11
      else :
        print("do not cheat" )
  return int(card)
stop_game=False
while not stop_game:

  computer_first_Card=random_card(True)
  computer_second_Card=random_card(True)
  print(f"computer first card is {computer_first_Card}")
  computer_card_sum=computer_first_Card+computer_second_Card

  player_first_card=random_card(False)
  player_second_card=random_card(False)
  player_card_sum=player_first_card+player_second_card
  print(f"your cards are {player_first_card}+{player_second_card}={player_card_sum}")

  continute=False
  def new_card_function(next_card):
    while next_card:
      condition =input("if you want to next card? y/n: ")
      if condition=="y":
        next_card=False
        continute=True
      elif condition=="n":
        next_card=False
        continute=False
      else :
        print("wrong input")
    return continute
  continute=new_card_function(True)

  while continute:
    next_card_number=random_card(False)
    die=False
    total_number=player_card_sum+next_card_number
    if total_number>21:
      die=True
    if die:
      print(f"you got {next_card_number} as new card so you die")
      player_card_sum=total_number
      continute=False
    else:
      print(f"you got {next_card_number} as new card and total is {total_number}")
      player_card_sum=total_number
      continute=new_card_function(True)

  if 22>player_card_sum>computer_card_sum:
    print(f"computer card sum is {computer_card_sum} so you win")
  else :
    print(f"computer card sum is {computer_card_sum} so you lose")
  tryagain_whileloot=True
  while tryagain_whileloot:
    tryagan=input("if you want to play again? y/n: ")
    if tryagan=="y":
      stop_game=False
      tryagain_whileloot=False
      os.system("clear")

    elif tryagan=="n":
      stop_game=True
      tryagain_whileloot=False
      
    else :
      print("wrong input")
      tryagain_whileloot=True
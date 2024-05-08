from random import randint

# open up a terminal, run the file, and play !
# how to run? right click / run Python/ run Python file in Terminal

def play_game (choices):
  if choices['player'] == choices['computer']: 
    print('thats a draw, try again')
    play_again_yes()
  else: check_win(choices['computer'], choices['player'])


def play_again_yes ():
  get_choices(input('enter a choice again: '))

def check_win(comp, user):
  
  win_options = [
    {"win": "rock", "lose": "scissors"},
    {"win": "scissors", "lose": "paper"},
    {"win": "paper", "lose": "rock"},
  ]

  for obj in win_options:
    if obj["win"] == comp and obj["lose"] == user: 
      print( "comp played " + comp + " and won" )
      response = input('want to play again? yes or no ')
      if response == "yes":
        play_again_yes()
      else:
        print('okay bye')

    elif obj["win"] == user and obj["lose"] == comp:  
      print( "you played " + user + " and won" )
      response = input('want to play again? yes or no ')
      if response == "yes":
        play_again_yes()
      else:
        print('okay bye')


def get_choices(playChoice):
  choice_option = ["rock", "paper", "scissors"]
  index = randint(0, 2)

  player_choice = playChoice
  comp_choice = choice_option[index]

  choices = {"player" : player_choice, "computer" : comp_choice}

  play_game(choices)
  return choices

choices = get_choices(input('enter a choice- rock, paper, or scissors: '))


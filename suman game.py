import random
items =["ROCK","PAPER","SCISSORS"]
print ("Welcome to rock, paper, scissors")
player = ''
score1 = 0
score2 = 0
play = 'y'
while play.lower() == 'y':
    player = input("Choose rock, paper or scissors: ").upper()
    print("You chose ", player)
    computer = choice(items)
    print("I chose ", computer)
    rules = {"ROCK":"SCISSORS","PAPER":"ROCK","SCISSORS":"PAPER"}

    if player == computer:
        print("We drew")
    elif rules[player] == computer:
        print("You Won")
        score1 = score1 + 1
    else:
        print("I won")
        score2 = score2 + 1
    print("Your score ", score1, ". My score ", score2, ".")
    play = input("Play again? [y/n]: ")

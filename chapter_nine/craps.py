"""
File: craps.py
This module studies and plays the game of craps.
"""

from player import Player


def playOneGame():
    """
    Plays a single game and prints the results
    """
    player = Player()
    youWin = player.play()
    if youWin:
        print("You win!")
    else:
        print("You lose!")


def playManyGames(number):
    """
    Plays a number of games and prints statistics
    """
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.play()
        rolls = player.getRollsCount()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))


def main():
    """
    Plays a number of games and prints statistics
    """
    number = int(input("Enter the number of games: "))
    if number == 1:
        playOneGame()
    elif number > 1:
        playManyGames(number)


if __name__ == "__main__":
    main()

"""
File: player.py
This module defines the Player class
"""

from die import Die


class Player(object):

    def __init__(self):
        """
        Has a pair of dice and an empty rolls list
        """
        self.die1 = Die()
        self.die2 = Die()
        # self.rolls = []
        self.rollsCount = 0
        self.currentRoll = ""
        self.atStartup = True
        self.winner = False
        self.loser = False
        self.point = 0

    def play(self):
        """
        Plays the game while prompting the player to continue rolling.
        As soon as the player wins or loses, the method returns True or False.
        """
        self.atStartup = True
        self.winner = False
        self.loser = False
        self.point = 0
        self.rollDice()
        while not self.winner and not self.loser:
            print(f"Point is {self.point}")
            print(f"{self.currentRoll}")
            cont = input("Press Enter to continue or 'q' to quit: ")
            if cont == "q":
                self.rollsCount = 0
                return False
            self.rollDice()
        return self.winner

    def rollDice(self):
        """
        Rolls the dice and records the roll.
        """
        self.die1.roll()
        self.die2.roll()
        sum = self.die1.getValue() + self.die2.getValue()
        self.currentRoll = f"Roll: {self.die1} + {self.die2} = {sum}"
        self.rollsCount += 1

        if self.atStartup:
            if sum in (7, 11):
                self.winner = True
                self.loser = False
            elif sum in (2, 3, 12):
                self.loser = True
                self.winner = False
            else:
                self.point = sum
            self.atStartup = False
        else:
            if sum == self.point:
                self.winner = True
                self.loser = False
            elif sum == 7:
                self.loser = True
                self.winner = False

        return (self.die1.getValue(), self.die2.getValue())

    def getRollsCount(self):
        """
        Returns the number of rolls
        """
        return self.rollsCount

    def isWinner(self):
        """
        Returns True if the player is a winner
        """
        return self.winner

    def isLoser(self):
        """
        Returns True if the player is a loser
        """
        return self.loser

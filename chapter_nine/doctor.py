"""
File: doctor.py
Project 5

Softbot for a non-directive psychotherapist.
"""

import random


class Doctor:

    # All doctors share the same qualifiers, replacements, and hedges.

    QUALIFIERS = [
        "Why do you say that ",
        "You seem to think that ",
        "Did I just hear you say that ",
        "Why do you believe that ",
    ]

    REPLACEMENTS = {
        "i": "you",
        "me": "you",
        "my": "your",
        "we": "you",
        "us": "you",
        "am": "are",
        "you": "i",
        "you": "I",
    }

    HEDGES = [
        "Go on.",
        "I would like to hear more about that.",
        "And what do you think about this?",
        "Please continue.",
    ]

    GREETINGS = [
        "Hello, I am your non-directive psychotherapist. How can I help you today?",
        "Welcome to the non-directive psychotherapist. What brings you here?",
        "Hello, I am here to listen. What would you like to talk about?",
    ]

    FAREWELLS = [
        "Goodbye. I hope you have a great day.",
        "Goodbye. I hope to see you soon.",
        "Goodbye. I am here if you need me.",
    ]

    # Each doctor keeps its own individual history.

    def __init__(self, name="Doctor"):
        """Loads history from a file, if it exists."""
        self.history = []
        self.name = name
        try:
            with open(f"{name}.txt") as file:
                for line in file:
                    self.history.append(line.rstrip())
        except IOError:
            pass

    def greeting(self):
        """Returns the doctor's greeting"""
        return random.choice(Doctor.GREETINGS)

    def farewell(self):
        """Saves the history and returns the doctor's farewell"""
        with open(f"{self.name}.txt", "w") as file:
            for line in self.history:
                file.write(line + "\n")
        return random.choice(Doctor.FAREWELLS)

    def reply(self, sentence):
        """Returns the doctor's reply to sentence."""
        choice = random.randint(1, 10)
        if choice in (1, 2):
            if len(self.history) > 3:
                answer = "Earlier you said that " + self.change_person(
                    random.choice(self.history)
                )
            else:
                answer = random.choice(Doctor.HEDGES)
        elif choice in range(3, 7):
            answer = (
                random.choice(Doctor.QUALIFIERS) + self.change_person(sentence) + "?"
            )
        else:
            answer = random.choice(Doctor.HEDGES)
        self.history.append(sentence)
        return answer

    def change_person(self, sentence):
        """Replaces pronouns so as to shift the address."""
        oldlist = sentence.split()
        newlist = [Doctor.REPLACEMENTS.get(word.lower(), word) for word in oldlist]
        return " ".join(newlist)


def main():
    """Tester function for Doctor class.
    The patient enters 'quit' to exit."""
    name = input("What is the name of the Doctor?")
    doctor = Doctor(name)
    print(doctor.greeting())
    while True:
        sentence = input("> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break
        else:
            print(doctor.reply(sentence))


if __name__ == "__main__":
    main()

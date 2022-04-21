pic = ["  _____\n  |   |\n      |\n      |\n      |\n      |\n¯¯¯¯¯¯¯", 

        "  _____\n  |   |\n  O   |\n      |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n  |   |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|   |\n      |\n      |\n¯¯¯¯¯¯¯", 

        "  _____\n  |   |\n  O   |\n /|\  |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n¯¯¯¯¯¯¯"]

guesses = 0
player_name = ""
word = ["apina", "kissa"] #placeholder
guess_word = word[1] #placeholder

print("Hello!", "This is a basic game of hangman")
while len(player_name) < 1:
        print("Please give me your name")
        name = input()
        if len(name) > 1:
                player_name = name

def play_the_game(player_name):
        print("Okay", player_name.capitalize(), "Let's start!")
        print(pic[0])
        print("your word has", len(guess_word), "letters")
        guess = ""
        print("Guess the word")
        while guess != guess_word:
                guess = input()
                if guess == guess_word:
                        print("You won!")
                else:
                        print("Try again!")

play_the_game(player_name)
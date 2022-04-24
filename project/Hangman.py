import time

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
guessed_letters = []

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
        number_of_guesses = 0
        guess = ""
        t = time.perf_counter_ns()
        while guess != guess_word and number_of_guesses < 6:
                print("What is your guess?")
                guess = input()
                guessed_letters.append(guess.lower())
                for letter in guess_word:
                        if letter.lower() in guessed_letters:
                                print(letter, end= " ")
                        else:
                                print("_", end=" ")
                if guess == guess_word:
                        elapsed_time = (time.perf_counter_ns() - t) / 1000000000
                        print("You won!")
                        print("Your time was", elapsed_time, "seconds")
                elif number_of_guesses < 5:
                        number_of_guesses = number_of_guesses + 1
                        print("Wrong one!")
                        print("Guesses left:", 6 - number_of_guesses)
                        print(pic[number_of_guesses])
                else:
                        elapsed_time = (time.perf_counter_ns() - t) / 1000000000
                        print("Game over!")
                        print("Your time was", elapsed_time, "seconds")
                        number_of_guesses = number_of_guesses + 1
                        print(pic[number_of_guesses])


play_the_game(player_name)
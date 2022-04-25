import time
import random

pic = ["  _____\n  |   |\n      |\n      |\n      |\n      |\n¯¯¯¯¯¯¯", 

        "  _____\n  |   |\n  O   |\n      |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n  |   |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|   |\n      |\n      |\n¯¯¯¯¯¯¯", 

        "  _____\n  |   |\n  O   |\n /|\  |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n¯¯¯¯¯¯¯"]

guesses = 0
player_name = ""
f = open("wordlist.txt", "r")
word = f.readlines()
guess_word = random.choice(word)[:-1]
f.close()
guessed_letters = []
print("Hello!", "This is a basic game of hangman")
while len(player_name) < 1:
        print("Please give me your name")
        name = input()
        if len(name) > 1:
                player_name = name
def get_time(elem):
        return elem[1]

def pull_scores():
        f = open("highscores.txt", "r")
        scores = f.read()
        f.close()
        return scores

def scores_to_2D():
        pull = pull_scores()
        twoD = []
        lines = pull.strip().split("\n")
        for line in lines:
                twoD.append(line.split(","))
        twoD.sort(key=get_time)
        return twoD

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
                if guess == guess_word:
                        elapsed_time = (time.perf_counter_ns() - t) / 1000000000
                        print("That was the correct word, you won!")
                        print("Your time was", elapsed_time, "seconds")
                        if guess_word == "bunny":
                                sorted = scores_to_2D()
                                if float(sorted[0][1]) < elapsed_time and float(sorted[1][1]) < elapsed_time and float(sorted[2][1]) < elapsed_time:
                                        print("jee")
                elif number_of_guesses < 5:
                        number_of_guesses = number_of_guesses + 1
                        guessed_letters.append(guess.lower())
                        for letter in guess_word:
                                if letter.lower() in guessed_letters:
                                        print(letter, end= " ")
                                else:
                                        print("_", end=" ")
                        print("Guesses left:", 6 - number_of_guesses)
                        print(pic[number_of_guesses])
                else:
                        print("Game over!")
                        print("the correct word was", guess_word)
                        number_of_guesses = number_of_guesses + 1
                        print(pic[number_of_guesses])


play_the_game(player_name)
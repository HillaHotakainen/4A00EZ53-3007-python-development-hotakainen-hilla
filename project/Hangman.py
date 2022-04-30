import time
import random
import re

pic = ["  _____\n  |   |\n      |\n      |\n      |\n      |\n¯¯¯¯¯¯¯", 

        "  _____\n  |   |\n  O   |\n      |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n  |   |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|   |\n      |\n      |\n¯¯¯¯¯¯¯", 

        "  _____\n  |   |\n  O   |\n /|\  |\n      |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n¯¯¯¯¯¯¯",

        "  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n¯¯¯¯¯¯¯"]


f = open("wordlist.txt", "r")
word = f.readlines()
guess_word = random.choice(word)[:-1]
f.close()
guessed_letters = []
player_name = ""

def get_time(elem):
        return elem[1]

def scores_to_2D(highscore):
        f = open(highscore, "r")
        scores = f.read()
        twoD = []
        lines = scores.strip().split("\n")
        for line in lines:
                twoD.append(line.split(","))
        twoD.sort(key=get_time)
        f.close()
        return twoD

def winner_score(elapsed_time, win_time, number, name):
        file = f"highscores{number}.txt"
        sorted = scores_to_2D(file)
        first = float(sorted[0][1])
        second = float(sorted[1][1])
        third = float(sorted[2][1])
        if first > elapsed_time:
                set_new_score(name, win_time, sorted, 0, file)
        elif first < elapsed_time and second > elapsed_time:
                set_new_score(name, win_time, sorted, 1, file)
        elif first < elapsed_time and second < elapsed_time and third > elapsed_time:
                set_new_score(name, win_time, sorted, 2, file)
        else:
                print("you did not reach top3")

def set_new_score(name, wintime, scores, position, file):
        if position == 0:
                line1 = name, wintime
                line2 = scores[1][0], scores[1][1]
                line3 = scores[2][0], scores[2][1]
                new_scores = str(f"{line1}\n{line2}\n{line3}")
                stripped_scores = re.sub("[ ')(]", '', new_scores)
                score_file = open(file, "w")
                score_file.seek(0)
                score_file.write(stripped_scores)
                score_file.truncate()
                score_file = open(file, "r")
                print(score_file.read())
        elif position == 1:
                line1 = scores[0][0], scores[0][1]
                line2 = name, wintime
                line3 = scores[2][0], scores[2][1]
                new_scores = str(f"{line1}\n{line2}\n{line3}")
                stripped_scores = re.sub("[ ')(]", '', new_scores)
                score_file = open(file, "w")
                score_file.seek(0)
                score_file.write(stripped_scores)
                score_file.truncate()
                score_file = open(file, "r")
                print(score_file.read())
        else:
                line1 = scores[0][0], scores[0][1]
                line2 = scores[1][0], scores[1][1]
                line3 = name, wintime
                new_scores = str(f"{line1}\n{line2}\n{line3}")
                stripped_scores = re.sub("[ ')(]", '', new_scores)
                score_file = open(file, "w")
                score_file.seek(0)
                score_file.write(stripped_scores)
                score_file.truncate()
                score_file = open(file, "r")
                print(score_file.read())

def play_the_game(name):
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
                        win_time = str(elapsed_time)
                        print("That was the correct word, you won!")
                        print("Your time was", elapsed_time, "seconds")
                        if guess_word == "bunny":
                                number = 0
                                winner_score(elapsed_time, win_time, number, name)
                        if guess_word == "cactus":
                                number = 1
                                winner_score(elapsed_time, win_time, number, name)
                        if guess_word == "version":
                                number = 2
                                winner_score(elapsed_time, win_time, number, name)
                        if guess_word == "delivery":
                                number = 3
                                winner_score(elapsed_time, win_time, number, name)
                        if guess_word == "biscuit":
                                number = 4
                                winner_score(elapsed_time, win_time, number, name)
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

print("Hello!", "This is a basic game of hangman.")
print("would you like to play or check highscores?")
print("Play: 1")
print("highscores: 2")
choise = str(input())
if choise == "1":
        while len(player_name) < 1:
                print("Please give me your name")
                name = input()
                if len(name) > 1:
                        player_name = name
        play_the_game(player_name)
elif choise == "2":
        print("which score do you want to see?")
        print("all: 1", "bunny: 2", "cactus: 3", "version: 4", "delivery: 5", "biscuit: 6", sep="\n")
        chosie = str(input())
        if chosie == "1":
                print("all")
        elif chosie == "2":
                print("bnuuy")
        elif chosie == "3":
                print("cacaca")
        elif chosie == "4":
                print("versioncontrol")
        elif chosie == "5":
                print("wolt")
        elif chosie == "6":
                print("tasty")
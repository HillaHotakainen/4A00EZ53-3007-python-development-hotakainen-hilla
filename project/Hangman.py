import time
import random
import re

print("Hello!", "This is a basic game of hangman.")
#while loop to keep the program running until user ends it.
while True:
        #hangman pictures in one line each. 
        pic = ["  _____\n  |   |\n      |\n      |\n      |\n      |\n¯¯¯¯¯¯¯", 
                "  _____\n  |   |\n  O   |\n      |\n      |\n      |\n¯¯¯¯¯¯¯",
                "  _____\n  |   |\n  O   |\n  |   |\n      |\n      |\n¯¯¯¯¯¯¯",
                "  _____\n  |   |\n  O   |\n /|   |\n      |\n      |\n¯¯¯¯¯¯¯", 
                "  _____\n  |   |\n  O   |\n /|\  |\n      |\n      |\n¯¯¯¯¯¯¯",
                "  _____\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n¯¯¯¯¯¯¯",
                "  _____\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n¯¯¯¯¯¯¯"]

        #opening wordlist fron external file and choosing the word
        f = open("wordlist.txt", "r")
        word = f.readlines()
        guess_word = random.choice(word)[:-1]
        f.close()
        #gussed letters and player name are saved here for later use
        guessed_letters = []
        player_name = ""

        #function for using key element
        def get_time(elem):
                #always returns second item in list(in this case time)
                return elem[1]

        #function for making existing list into 2D and sorting it by time
        #returns sorted 2D list, (highscore) is deffined elsewhere and
        #depends on what words was used.
        def scores_to_2D(highscore):
                f = open(highscore, "r")
                scores = f.read()
                twoD = [] 
                #removes spaces from the highscore list found in .txt
                #then splits it at every time line changes
                lines = scores.strip().split("\n")
                #the split lines are split again at each "," and saved to twoD
                for line in lines:
                        twoD.append(line.split(","))
                #the 2D list is sorted by time using key element
                twoD.sort(key=get_time)
                f.close()
                return twoD

        #function to check player position if they guess the word correctly
        def winner_score(elapsed_time, win_time, number, name):
                #finds file corresponding to the word that was guessed
                file = f"highscores{number}.txt"
                #gets scores as sorted 2D list (sorted by time)
                sorted = scores_to_2D(file)
                #top 3 players, first being fastest
                first = float(sorted[0][1]) 
                second = float(sorted[1][1])
                third = float(sorted[2][1])
                #gross if/elif/else stuff to determine and tell what spot current player got 
                #or tell them if they did not reach top 3 :c
                if first > elapsed_time:
                        print("congratualtions, you are number 1!")
                        set_new_score(name, win_time, sorted, 0, file)
                elif first < elapsed_time and second > elapsed_time:
                        print("congratualtions, you are number 2!")
                        set_new_score(name, win_time, sorted, 1, file)
                elif first < elapsed_time and second < elapsed_time and third > elapsed_time:
                        print("congratualtions, you are number 3!")
                        set_new_score(name, win_time, sorted, 2, file)
                else:
                        print("you did not reach top3 :C")

        #function to overwrite specific highscore file
        def overwrite(file, stripped_scores):
                score_file = open(file, "w") #opens the file
                score_file.seek(0) #finds starting point
                score_file.write(stripped_scores) #writes new scores
                score_file.truncate() #removes old scores

        #function for setting new scores
        #all parameters come from where the function is called form
        def set_new_score(name, wintime, scores, position, file):
                file = file #This is the file holding highscores for specific word

                #if/elif for changing one line and then compiling the final string,
                #to be used with overwrite function
                if position == 0:
                        line1 = name, wintime
                        line2 = scores[1][0], scores[1][1]
                        line3 = scores[2][0], scores[2][1]
                        new_scores = str(f"{line1}\n{line2}\n{line3}") #scores swapped from list to string
                        stripped_scores = re.sub("[ ')(]", '', new_scores) #regex to remove ')(] and spaces
                        overwrite(file, stripped_scores) #calling overwrite function with final scores
                elif position == 1:
                        line1 = scores[0][0], scores[0][1]
                        line2 = name, wintime
                        line3 = scores[2][0], scores[2][1]
                        new_scores = str(f"{line1}\n{line2}\n{line3}") #scores swapped from list to string
                        stripped_scores = re.sub("[ ')(]", '', new_scores) #regex to remove ')(] and spaces
                        overwrite(file, stripped_scores) #calling overwrite function with final scores
                else:
                        line1 = scores[0][0], scores[0][1]
                        line2 = scores[1][0], scores[1][1]
                        line3 = name, wintime
                        new_scores = str(f"{line1}\n{line2}\n{line3}") #scores swapped from list to string
                        stripped_scores = re.sub("[ ')(]", '', new_scores) #regex to remove ')(] and spaces
                        overwrite(file, stripped_scores) #calling overwrite function with final scores

        #function for checking the highscores
        def check_scores(number):
                #file is chosen depending what words scores user wants to check
                file = f"highscores{number}.txt"
                f = open(file, "r")
                print(f.read())
                f.close()

        #function for playing the game of hangman
        def play_the_game(name):
                print("Okay", player_name.capitalize(), "Let's start!")
                print(pic[0]) # prints the starting picture
                print("your word has", len(guess_word), "letters") #let's you know number of letters in the word being guessed
                number_of_guesses = 0 #amount of guesses done
                guess = "" #guessed word
                t = time.perf_counter_ns() #start of timer

                #as long as word is not guessed and player has guesses left,
                #a while loop will ask for player to guess
                while guess != guess_word and number_of_guesses < 6:
                        print("What is your guess?")
                        guess = input() #players guess, can be one letter or full word

                        #if player guesses the word correctly we go here:
                        if guess == guess_word:
                                #timer is stopped and saved
                                elapsed_time = (time.perf_counter_ns() - t) / 1000000000
                                win_time_temp = str(elapsed_time) #saved time is changed into string
                                win_time = win_time_temp[0:4] #only two digits after . are shown
                                print("That was the correct word, you won!")
                                print("Your time was", win_time, "seconds")
                                #checks what word was guessed and based on that begins
                                # the scoring process
                                if guess_word == "bunny":
                                        number = 0 #deffines file on other functions
                                        winner_score(elapsed_time, win_time, number, name)
                                elif guess_word == "cactus":
                                        number = 1 #deffines file on other functions
                                        winner_score(elapsed_time, win_time, number, name)
                                elif guess_word == "version":
                                        number = 2 #deffines file on other functions
                                        winner_score(elapsed_time, win_time, number, name)
                                elif guess_word == "delivery":
                                        number = 3 #deffines file on other functions
                                        winner_score(elapsed_time, win_time, number, name)
                                elif guess_word == "biscuit":
                                        number = 4 #deffines file on other functions
                                        winner_score(elapsed_time, win_time, number, name)
                        #if player did not guess the word:
                        elif number_of_guesses < 5:
                                #number of guesses increases by one
                                number_of_guesses = number_of_guesses + 1
                                #guess is made to lowercase and added to guessed letter list
                                guessed_letters.append(guess.lower())
                                #will check letters in word player is guessing
                                for letter in guess_word:
                                        #if letter is in the word player is guessing
                                        #will print letter
                                        if letter.lower() in guessed_letters:
                                                print(letter, end= " ")
                                        #if letter is not in the word, will print _
                                        else:
                                                print("_", end=" ")
                                #tells player how many guesses are left
                                print("Guesses left:", 6 - number_of_guesses)
                                #prints the picture corresponding of how many guesses are left
                                print(pic[number_of_guesses])
                        #will go here if you run out of guesses
                        else:
                                #tells you that game is over and also what the correct word was
                                print("Game over!")
                                print("the correct word was", guess_word)
                                #ends the guess loop
                                number_of_guesses = number_of_guesses + 1
                                #prints the final picture
                                print(pic[number_of_guesses])

        #asks if user wants to play or check highscores
        print("would you like to play or check highscores?")
        print("Play: 1")
        print("highscores: 2")
        choise = str(input())
        #if user chooses to play:
        if choise == "1":
                #will ask for players name (need to be min 2 letters)
                while len(player_name) < 1:
                        print("Please give me your name")
                        name = input()
                        #checks if lenght is over 1
                        if len(name) > 1:
                                player_name = name
                #starts the function for playing the game
                play_the_game(player_name)
                #after game is over gives a choise to quit or continue
                print("__________")
                print("do you want to quit?")
                print("yes/no")
                yes_no = str(input())
                #if user choose yes, closes the program
                if yes_no == "yes":
                        print("Goodbye!")
                        break
                #if user chooses no, starts program again
                elif yes_no == "no":
                        print("okay")
                        continue
                #if neither no or yes is chosen closes the program
                else:
                        print("that was not yes or no")
                        print("you need to restart me, bye!")
                        break
        #if scorecheck is chosen:
        elif choise == "2":
                #asks what score user wishes to check
                print("which score do you want to see?")
                print("all:      1", "bunny:    2", "cactus:   3", "version:  4", "delivery: 5", "biscuit:  6", sep="\n")
                chosie = str(input())
                #shows all scores (also looks pretty gross in code)
                if chosie == "1":
                        print("BUNNY:", "\n")
                        check_scores(0)
                        print("_______")
                        print("CACTUS:", "\n")
                        check_scores(1)
                        print("_______")
                        print("VERSION:", "\n")
                        check_scores(2)
                        print("_______")
                        print("DELIVERY:", "\n")
                        check_scores(3)
                        print("_______")
                        print("BISCUIT:", "\n")
                        check_scores(4)
                        print("__________")
                        print("do you want to quit?")
                        print("yes/no")
                        yes_no = str(input())
                        if yes_no == "yes":
                                print("Goodbye!")
                                break
                        elif yes_no == "no":
                                print("okay")
                                continue
                        else:
                                print("that was not yes or no")
                                print("you need to restart me, bye!")
                                break
                #shows scores for word "bunny"
                elif chosie == "2":
                        print("bunny:")
                        check_scores(0)
                        #will ask if user wants to quit or not
                        print("__________")
                        print("do you want to quit?")
                        print("yes/no")
                        yes_no = str(input())
                        #if yes, quits the program
                        if yes_no == "yes":
                                print("Goodbye!")
                                break
                        #if no, starts program again
                        elif yes_no == "no":
                                print("okay")
                                continue
                        #if something else, quits the program
                        else:
                                print("that was not yes or no")
                                print("you need to restart me, bye!")
                                break
                #shows scores for word "cactus"
                elif chosie == "3":
                        print("cactus")
                        check_scores(1)
                        #will ask if user wants to quit or not
                        print("__________")
                        print("do you want to quit?")
                        print("yes/no")
                        yes_no = str(input())
                        #if yes, quits the program
                        if yes_no == "yes":
                                print("Goodbye!")
                                break
                        #if no, starts program again
                        elif yes_no == "no":
                                print("okay")
                                continue
                        #if something else, quits the program
                        else:
                                print("that was not yes or no")
                                print("you need to restart me, bye!")
                                break
                #shows scores for word "version"
                elif chosie == "4":
                        print("version")
                        check_scores(2)
                        #will ask if user wants to quit or not
                        print("__________")
                        print("do you want to quit?")
                        print("yes/no")
                        yes_no = str(input())
                        #if yes, quits the program
                        if yes_no == "yes":
                                print("Goodbye!")
                                break
                        #if no, starts program again
                        elif yes_no == "no":
                                print("okay")
                                continue
                        #if something else, quits the program
                        else:
                                print("that was not yes or no")
                                print("you need to restart me, bye!")
                                break
                #shows scores for word "delivery"
                elif chosie == "5":
                        print("delivery")
                        check_scores(3)
                        #will ask if user wants to quit or not
                        print("__________")
                        print("do you want to quit?")
                        print("yes/no")
                        yes_no = str(input())
                        #if yes, quits the program
                        if yes_no == "yes":
                                print("Goodbye!")
                                break
                        #if no, starts program again
                        elif yes_no == "no":
                                print("okay")
                                continue
                        #if something else, quits the program
                        else:
                                print("that was not yes or no")
                                print("you need to restart me, bye!")
                                break
                #shows scores for word "biscuit"
                elif chosie == "6":
                        print("biscuit")
                        check_scores(4)
                        #will ask if user wants to quit or not
                        print("__________")
                        print("do you want to quit?")
                        print("yes/no")
                        yes_no = str(input())
                        #if yes, quits the program
                        if yes_no == "yes":
                                print("Goodbye!")
                                break
                        #if no, starts program again
                        elif yes_no == "no":
                                print("okay")
                                continue
                        #if something else, quits the program
                        else:
                                print("that was not yes or no")
                                print("you need to restart me, bye!")
                                break
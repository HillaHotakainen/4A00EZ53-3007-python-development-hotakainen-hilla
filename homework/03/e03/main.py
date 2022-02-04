from string_helper import is_name

print("Your name:")
your_name = input()
if is_name(your_name, True) == True:
    print("Hello" , your_name, end= "!")
else:
    print("You did not give a proper name.")
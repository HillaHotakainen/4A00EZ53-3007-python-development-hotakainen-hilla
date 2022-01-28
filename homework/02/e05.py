print("Give a grade:", end="")
grade = int(input())

while grade > 5 or grade < 0:
    print("Please give a propper grade between 0-5")
    grade = int(input())

if grade == 0:
    print("Fail")
elif grade == 1 or grade == 2:
    print("Weak")
elif grade == 3 or grade == 4:
    print("Good")
elif grade == 5:
    print("Exellent")
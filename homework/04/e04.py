import random

def generate_lotto_numbers(min = 1, max = 40, amount = 7):
    if amount < 0 or min < 0 or max < 0 or amount > max :
        raise Exception("no numbers under zero and max must be biggest")
    numbers = set()
    while len(numbers) < amount:
        numbers.add(random.randint(min, max))
    return numbers

user_numbers = {1, 2, 3, 4, 5, 6, 7} 
random_number = generate_lotto_numbers(1, 40, 7)
counter = 0

while user_numbers != random_number:
    random_number = generate_lotto_numbers(1, 40, 7)
    counter = counter + 1
years = int(counter / 52)
print(f"it took {years} years to win")
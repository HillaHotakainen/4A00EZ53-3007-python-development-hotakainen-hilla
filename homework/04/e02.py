import random

def generate_lotto_numbers(amount, min, max):
    if amount < 0 or min < 0 or max < 0 or amount > max :
        raise Exception("no numbers under zero and max must be biggest")
    numbers = set()
    while len(numbers) < amount:
        numbers.add(random.randint(min, max))
    return numbers

print(generate_lotto_numbers(7, 1, 40))
print(generate_lotto_numbers(7, 1, 8))
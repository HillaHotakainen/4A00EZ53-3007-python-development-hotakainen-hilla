import random

def generate_lotto_numbers(min = 1, max = 40, amount = 7):
    if amount < 0 or min < 0 or max < 0 or amount > max :
        raise Exception("no numbers under zero and max must be biggest")
    numbers = set()
    while len(numbers) < amount:
        numbers.add(random.randint(min, max))
    return numbers

print(generate_lotto_numbers(1, 40, 7))
print(generate_lotto_numbers(min = 1, max = 40, amount = 7))
print(generate_lotto_numbers())
print(generate_lotto_numbers(min=1, max=10, amount=4))
print(generate_lotto_numbers(min=1, max=6, amount=6))
print(generate_lotto_numbers(min=1, max=6, amount=7))
import random

def lotto(amount):
    numbers = set()
    while len(numbers) < amount:
        numbers.add(random.randint(1,40))


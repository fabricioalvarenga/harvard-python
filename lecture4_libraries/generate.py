import random

coin: str = random.choice(["heads", "tails"])
print(coin)

number: int = random.randint(1, 10)
print(number)

cards: list[str] = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)

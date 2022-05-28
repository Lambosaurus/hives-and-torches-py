import random

def d(sides, times = 1):
    return sum([random.randint(1, sides) for _ in range(times)])

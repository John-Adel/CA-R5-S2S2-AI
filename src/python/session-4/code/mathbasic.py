"""
this is personal math module
"""



import random
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-=+[]{}:'\"\\/?><.,`~"
    password = ""

    for _ in range(length):
        passowrd += random.choice(characters)
    return password

def factorial(num: int) -> int:
    """
    This function returns the factorial of a number
    """
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num * factorial(num - 1)

def isPrime(num):
    import math

    if num == 0:
        print(False)
    for i in range(2, round(math.sqrt(num))):
        if num % i == 0:
            return True
        else:
            return False
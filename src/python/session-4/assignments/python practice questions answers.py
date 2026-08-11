# 1.Write a function that inputs a number and prints the multiplication table of that number
def multi_table(num: float):
    """This function prints the multiplication table(from 1 to 10) for any given number

    


    Args:
        num(float): input number
    """
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
multi_table(10)








# 2. Write a program to print twin primes less than 1000. 
# If two consecutive odd numbers are both prime then they are known as twin primes
def isPrime(num: int) -> bool:
    '''This function checks if a number is prime or not




    Args:
        num(int): any integer number for prime validation    
    
    Returns:
        True if the number is prime, False otherwise
    '''
    import math
    if num == 0 or num == 1:
        return False
    for i in range(2, round(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def twin_prime():
    '''This function prints the twin primes that are less than 1000, any two consecutive odd prime numbers are called twin primes.
    '''
    previous_prime = 2
    print("\nTwin Prime:")
    for i in range(1001):
        if isPrime(i):
            if i - previous_prime == 2:
                print(f"{previous_prime} and {i}")
            previous_prime = i
    print("\n")
twin_prime()








#3. Write a program to find out the prime factors of a number.
# Example: prime factors of 56 - 2, 2, 2, 7
def prime_factor(num: int) -> list[int]:
    '''  This function returns a list of all the prime factors for any number
    



    Args:
        num(int): the number you want to find the prime factors for

    Returns:
        list of all prime factors for that number
    '''
    import math
    output = []
    copy = num
    if isPrime(num):
        return [num]
    for i in range(2, num):
        print(i)
        while isPrime(i) and copy % i == 0:
            output.append(i)
            copy //= i
        if copy == 1:
            break
    return output
print(prime_factor(1000000))








#4. Write a function that converts a decimal number to binary number
#for the built-in function
print(bin(77)[2:])
# My function
def dec_to_bin(num: int) -> int:
    '''  This function converts a decimal number to a binary one
    



    Args:
        num(int): input number
    
    Returns:
        binary integer number
    '''
    output = []
    while num != 0:
        if num % 2 == 0:
            output.append("0")
        else:
            output.append("1")
        num //= 2
    output.reverse()
    return int("".join(output))
print(dec_to_bin(77))








#5. A number is called perfect if the sum of proper divisors of that number is equal to the number. 
# For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range
def perfect_nums(start: int, end: int = None):
    '''  This function prints all the perfect numbers between a given range
    



    Args:
        start: if one argument was provided, start would be the end limit of your range with a default of zero, if two, then start would be the start of your range
        end: if two arguments were provided, end would be the end limit of your range
    '''
    
    if end is None:
        end = start
        start = 0
    for number in range(start, end + 1):
        divisors = []
        for divisor in range(1, number):
            if number % divisor == 0:
                divisors.append(divisor)
        if sum(divisors) == number:
            print(number)
# We can also use the Euclid-Euler Theorem for much faster results
def euclid_euler(start: int, end: int = None):
    if end is None:
        end = start
        start = 0
    for p in range(start, end):
        if isPrime(p) and isPrime(((2**p) - 1)) and (2**(p-1)) * ((2**p) - 1) <= end:
            print(int((2**(p-1)) * ((2**p) - 1)))
        elif (2**(p-1)) * ((2**p) - 1) > end:
            break
        else:
            continue
#perfect_nums(10000)
euclid_euler(1000000000000)

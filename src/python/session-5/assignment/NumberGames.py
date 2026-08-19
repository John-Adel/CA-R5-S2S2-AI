class NumberGames():
    def __init__(self, num = 0):
        selfnum = num
    def multi_table(self, num):
        """This function prints the multiplication table(from 1 to 10) for any given number

        


        Args:
            num(float): input number
        """
        for i in range(1, 11):
            print(f"{num} * {i} = {num * i}")








    def isPrime(self, num: int) -> bool:
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

    def twin_prime(self):
        '''This function prints the twin primes that are less than 1000, any two consecutive odd prime numbers are called twin primes.
        '''
        previous_prime = 2
        print("\nTwin Prime:")
        for i in range(1001):
            if self.isPrime(i):
                if i - previous_prime == 2:
                    print(f"{previous_prime} and {i}")
                previous_prime = i
        print("\n")









    def prime_factor(self, num) -> list[int]:
        '''  This function returns a list of all the prime factors for any number
        self



        Args:
            num(int): the number you want to find the prime factors for

        Returns:
            list of all prime factors for that number
        '''
        import math
        output = []
        copy = num
        if self.isPrime(num):
            return [num]
        for i in range(2, num):
            while self.isPrime(i) and copy % i == 0:
                output.append(i)
                copy //= i
            if copy == 1:
                break
        return output









    def dec_to_bin(self, num) -> int:
        '''  This function converts a decimal number to a binary one
        



        Returns:
            binary integer number
        '''
        return bin(num)[2:]









    def euclid_euler(self,num, end: int = None):
        '''  This function prints all the perfect numbers between a given range
        



        Args:
            num: if one argument was provided, num would be the end limit of your range with a default of zero, if two, then num would be the num of your range
            end: if two arguments were provided, end would be the end limit of your range
        '''
        if end is None:
            end = num
            num = 0
        for p in range(num, end):
            if self.isPrime(p) and self.isPrime(((2**p) - 1)) and (2**(p-1)) * ((2**p) - 1) <= end:
                print(int((2**(p-1)) * ((2**p) - 1)))
            elif (2**(p-1)) * ((2**p) - 1) > end:
                break
            else:
                continue


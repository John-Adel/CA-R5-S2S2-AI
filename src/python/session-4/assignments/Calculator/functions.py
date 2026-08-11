def calculate(num1: float, num2: float, op: int) -> str:
    """This is a simple calculator that can do basic operations with two numbers.




    Args:
        num1(float): first number
        num2(float): second number
        op(int): the mathematical operation to be done between the two numbers

    Returns:
        A floating-point string
    """
    if op == 1:
        return f"{num1} + {num2} = {num1 + num2}\n"
    elif op == 2:
        return f"{num1} - {num2} = {num1 - num2}\n"
    elif op == 3:
        return f"{num1} * {num2} = {num1 * num2}\n"
    elif op == 4:
        return f"{num1} / {num2} = {num1 / num2}\n"








def interface() -> str:
    '''  A simple interface for the calculator
    '''
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")








def user_input_function() -> list[str]:
    '''  This function prompts the user for input
    



    Returns:
        User input
    '''
    op = input("Enter your choice (1/2/3/4) or type 'exit' to quit: ").lower()
    while op != "1" and op != "2" and op != "3" and op != "4" and op != "exit":
        op = input("Invalid input\nPlease enter your choice (1/2/3/4) or type 'exit' to quit: ").lower()
    if op == "exit":
        print("Exiting the calculator. Goodbye!")
        exit()
    else:
        num1 = input("Enter first number: ").lower()
        while not num1.isnumeric():
            if num1 == "exit":
                num1 = input("Too late 🙂\nEnter a number: ").lower()
            else:
                num1 = input("Invalid input\nPlease enter a number: ").lower()            


        num2 = input("Enter second number: ").lower()
        while True:
            if num2 == "exit":
                num2 = input("Too late 🙂\nEnter a number: ").lower()
            elif not num2.isnumeric():
                num2 = input("Invalid input\nPlease enter a number: ").lower()
            elif num2 == "0" and op == "4":
                num2 = input("Can't divide by zero\nEnter another number:").lower()
            else:
                break
        return [num1, num2, op]